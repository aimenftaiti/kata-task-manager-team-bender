from task_manager.task import Task

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
        self.counter = 1

    def add_task(self, description, status) -> None:
        task = Task(self.counter, description, status)
        self.tasks.append(task)
        self.counter += 1

    def parse_command(self, command) -> None:
        if command.startswith("+ "):
            self.add_task(command[2:], "to do")
        else:
            raise ValueError("Unknown command")
