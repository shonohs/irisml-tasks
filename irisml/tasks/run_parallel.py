import dataclasses
import multiprocessing
import typing
import queue
import irisml.core


class Task(irisml.core.TaskBase):
    """Run the given tasks in parallel. A new process will be forked for each task. Each task must have an unique name."""
    @dataclasses.dataclass
    class Config:
        tasks: typing.List[irisml.core.TaskDescription]

    def execute(self, inputs):
        tasks = [irisml.core.Task(t) for t in self.config.tasks]
        names_set = set(t.name for t in tasks)
        print(names_set)
        if len(names_set) != len(tasks):
            raise ValueError("The child task names must be unique.")

        def run(task, context, q, index):
            task.load_module()
            outputs = task.execute(context)
            q.put((index, outputs))

        mp_ctx = multiprocessing.get_context('fork')
        q = mp_ctx.Queue(len(tasks))
        processes = [mp_ctx.Process(target=run, args=(t, self.context, q, i)) for i, t in enumerate(tasks)]
        for p in processes:
            p.start()

        for p in processes:
            p.join()

        for i in range(len(tasks)):
            try:
                index, outputs = q.get_nowait()
            except queue.Empty:
                raise RuntimeError("Failed to retrieve child outputs.")
            self.context.add_outputs(tasks[index].name, outputs)

        return self.Outputs()
