from flask import Blueprint, jsonify, request, current_app
from . import models

bp = Blueprint("tasks", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@bp.get("/info")
def info():
    return jsonify({
        "app": "Task Manager API",
        "version": current_app.config["APP_VERSION"],
        "max_tasks": current_app.config["MAX_TASKS"],
    }), 200


@bp.get("/tasks")
def list_tasks():
    return jsonify(models.get_all_tasks()), 200


@bp.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = models.get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


@bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "'title' is required"}), 400

    max_tasks = current_app.config["MAX_TASKS"]
    if len(models.get_all_tasks()) >= max_tasks:
        return jsonify({"error": f"Task limit ({max_tasks}) reached"}), 409

    task = models.create_task(title, data.get("description", ""))
    return jsonify(task), 201


@bp.patch("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    if "done" not in data:
        return jsonify({"error": "'done' field is required"}), 400
    task = models.update_task(task_id, bool(data["done"]))
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


@bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = models.delete_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted", "task": task}), 200
