# 📄 Project Report — Task Manager API (v1.0.0)

**Student:** rovshan_rzayev@epam.com
**Date:** 2026-04-14

---

## 1. Project Purpose & Description

**Task Manager API** is a RESTful web service built with Python and Flask.
It allows users to create, list, update, and delete tasks — a real business feature
that goes beyond a simple Hello World.

The project was designed to demonstrate a full DevOps lifecycle:
from local development and version control, through automated CI, to Docker packaging.

---

## 2. Branching & Versioning Approach

- Development was done on a **feature branch**: `feature/task-api`
- When the feature was complete, a **Pull Request** was opened to merge into `main`
- After merge, the release was **tagged**: `git tag -a v1.0.0 -m "Release 1.0.0"`
- Commit messages follow the pattern: `feat:`, `fix:`, `test:`, `docs:`, `chore:`

---

## 3. Build / Test / Quality Steps & Why They Matter

| Step    | Tool           | Why it matters                                      |
|---------|----------------|-----------------------------------------------------|
| Build   | pip install    | Ensures all dependencies resolve correctly          |
| Test    | pytest         | Verifies business logic works and catches regressions |
| Quality | flake8         | Enforces code style and catches potential bugs      |
| Package | Docker build   | Produces a reproducible, portable artifact          |

All 4 stages run automatically on every push via **GitHub Actions**.

---

## 4. Dockerfile & Image Explanation

The Dockerfile uses a **multi-stage build**:

- **Stage 1 (builder):** Installs all Python dependencies into `/install`
- **Stage 2 (runtime):** Uses a clean `python:3.11-slim` image, copies only
  the installed packages and source code — no build tools included.

This results in a **smaller, more secure image**.

A `HEALTHCHECK` is configured to call `/health` every 30 seconds,
so Docker (and orchestrators like Kubernetes) know if the container is alive.

---

## 5. Configuration & Secrets Strategy

| Variable      | Type   | Purpose                              |
|---------------|--------|--------------------------------------|
| `APP_VERSION` | Config | Displayed in `/info` endpoint        |
| `MAX_TASKS`   | Config | Limits number of tasks allowed       |
| `PORT`        | Config | Port the server listens on           |
| `SECRET_KEY`  | Secret | Would sign tokens (future feature)   |
| `DB_PASSWORD` | Secret | Would authenticate to a database     |

**Rule:** Config values are safe to store in `.env` and pass via `-e` flags.
Secrets must be stored in CI secret managers (GitHub Secrets, HashiCorp Vault)
and never committed to Git.

---

## 6. Problems Faced & Solutions

| Problem | Solution |
|---------|----------|
| Tests affecting each other (shared in-memory state) | Added `_reset()` function in models.py called in pytest `autouse` fixture |
| Docker image too large with dev dependencies | Used multi-stage build to separate build and runtime |
| Secrets management confusion | Created `.env.example` with clear comments separating config from secrets |

---

## 7. Release Summary

- **Version:** 1.0.0
- **Image Tag:** `task-manager-api:1.0.0`
- **Git Tag:** `v1.0.0`
- **Tests:** 10 passed ✅
- **Linter:** flake8 — no issues ✅
- **Docker:** Multi-stage, health-checked ✅
