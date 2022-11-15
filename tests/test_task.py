import pytest

from task_manager.task import Task

def test_task_init():
    task = Task(1, "description", "to do")
    assert task.id == 1
    assert task.description == "description"
    assert task.status == "to do"