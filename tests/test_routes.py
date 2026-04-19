import pytest
from app import create_app
from app import models


@pytest.fixture(autouse=True)
def reset_store():
    """Ensure a clean task store before every test."""
    models._reset()
    yield
    models._reset()


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# ── Test 1: health endpoint ───────────────────────────────────────────────────
def test_web_ui(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Task Manager API UI" in r.data


# ── Test 2: health endpoint ───────────────────────────────────────────────────
def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


# ── Test 3: info endpoint contains version ────────────────────────────────────
def test_info_contains_version(client):
    r = client.get("/info")
    data = r.get_json()
    assert r.status_code == 200
    assert "version" in data
    assert data["version"] == "1.0.0"


# ── Test 4: create a task ─────────────────────────────────────────────────────
def test_create_task(client):
    r = client.post("/tasks", json={"title": "Buy milk", "description": "2 litres"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["title"] == "Buy milk"
    assert data["done"] is False
    assert "id" in data


# ── Test 5: create task without title returns 400 ─────────────────────────────
def test_create_task_missing_title(client):
    r = client.post("/tasks", json={"description": "No title here"})
    assert r.status_code == 400


# ── Test 6: list tasks returns all created tasks ──────────────────────────────
def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})
    r = client.get("/tasks")
    assert r.status_code == 200
    assert len(r.get_json()) == 2


# ── Test 7: get single task ───────────────────────────────────────────────────
def test_get_task(client):
    client.post("/tasks", json={"title": "Single task"})
    r = client.get("/tasks/1")
    assert r.status_code == 200
    assert r.get_json()["title"] == "Single task"


# ── Test 8: get non-existent task returns 404 ─────────────────────────────────
def test_get_task_not_found(client):
    r = client.get("/tasks/999")
    assert r.status_code == 404


# ── Test 9: mark task as done ─────────────────────────────────────────────────
def test_update_task_done(client):
    client.post("/tasks", json={"title": "Finish project"})
    r = client.patch("/tasks/1", json={"done": True})
    assert r.status_code == 200
    assert r.get_json()["done"] is True


# ── Test 10: delete task ──────────────────────────────────────────────────────
def test_delete_task(client):
    client.post("/tasks", json={"title": "Delete me"})
    r = client.delete("/tasks/1")
    assert r.status_code == 200
    assert client.get("/tasks/1").status_code == 404


# ── Test 11: delete non-existent task returns 404 ────────────────────────────
def test_delete_task_not_found(client):
    r = client.delete("/tasks/999")
    assert r.status_code == 404
