import pytest

from task_manager.task import Task
from task_manager.task_manager import TaskManager


def test_task_manager_init():
    task_manager = TaskManager()
    assert task_manager.tasks == []


def test_task_manager_add_task():
    task_manager = TaskManager()
    task_manager.add_task("description", "to do")
    assert task_manager.tasks[0].description == "description"
    assert task_manager.tasks[0].status == "to do"