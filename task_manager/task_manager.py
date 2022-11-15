from task_manager.task import Task


class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
