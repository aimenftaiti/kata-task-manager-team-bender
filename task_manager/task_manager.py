from task_manager.task import Task

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
        self.counter = 1

    def add_task(self, description, status) -> None:
        task = Task(self.counter, description, status)
        self.tasks.append(task)
        self.counter += 1

    def remove_task(self, id) -> None:
        id = int(id)
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                break
        else:
            raise ValueError("Unknown task id")
        
    def change_task_status(self, id, status) -> None:
        id = int(id)
        for task in self.tasks:
            if task.id == id:
                task.status = status
                break
        else:
            raise ValueError("Unknown task id")

    def parse_command(self, command) -> None:
        if command.startswith("+ "):
            self.add_task(command[2:], "to do")
        elif command.startswith("- "):
            self.remove_task(command[2:])
        elif command.startswith("x "):
            self.change_task_status(command[2:], "done")
        else:
            raise ValueError("Unknown command")
