from datetime import datetime

_tasks = {}
_next_id = 1


def _reset():
    """Reset store – used by tests only."""
    global _tasks, _next_id
    _tasks = {}
    _next_id = 1


def get_all_tasks():
    return list(_tasks.values())


def get_task(task_id: int):
    return _tasks.get(task_id)


def create_task(title: str, description: str = ""):
    global _next_id
    task = {
        "id": _next_id,
        "title": title,
        "description": description,
        "done": False,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    _tasks[_next_id] = task
    _next_id += 1
    return task


def update_task(task_id: int, done: bool):
    if task_id not in _tasks:
        return None
    _tasks[task_id]["done"] = done
    return _tasks[task_id]


def delete_task(task_id: int):
    return _tasks.pop(task_id, None)
