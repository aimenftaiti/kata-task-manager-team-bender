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


def test_task_manager_can_parse_add_task_command():
    task_manager = TaskManager()
    task_manager.parse_command("+ Learn Python")
    assert task_manager.tasks[0].description == "Learn Python"
    assert task_manager.tasks[0].status == "to do"
    assert task_manager.tasks[0].id == 1


def test_task_manager_can_parse_remove_task_command():
    task_manager = TaskManager()
    task_manager.parse_command("+ Learn Python")
    task_manager.parse_command("- 1")
    assert task_manager.tasks == []


def test_task_manager_can_parse_done_task_command():
    task_manager = TaskManager()
    task_manager.parse_command("+ Learn Python")
    task_manager.parse_command("x 1")
    assert task_manager.tasks[0].status == "done"


def test_task_manager_can_parse_todo_task_command():
    task_manager = TaskManager()
    task_manager.parse_command("+ Learn Python")
    task_manager.parse_command("o 1")
    assert task_manager.tasks[0].status == "to do"


def test_task_manager_can_parse_quit_task_command():
    task_manager = TaskManager()
    command_type = task_manager.parse_command("q")["type"]
    assert command_type == "quit"
