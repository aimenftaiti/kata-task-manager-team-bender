import pytest

from task_manager.task import Task
from task_manager.task_manager import TaskManager


def test_task_manager_init():
    task_manager = TaskManager()
    assert task_manager.tasks == []


def test_task_manager_add_task():
    task_manager = TaskManager()
    task = Task(1, "description", "to do")
    task_manager.add_task(task)
    assert task_manager.tasks == [task]
