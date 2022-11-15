import pytest

from task_manager.task import Task
from task_manager.task_manager import TaskManager

def test_task_manager_init():
    task_manager = TaskManager()
    assert task_manager.tasks == []