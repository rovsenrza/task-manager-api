# 🚀 Release Notes — v1.0.0

**Release Date:** 2026-04-14
**Image Tag:** `task-manager-api:1.0.0`
**Git Tag:** `v1.0.0`

---

## 📋 What's Included

### ✅ Features
- Task CRUD: Create, Read, Update (mark done), Delete tasks
- `GET /health` — container health check endpoint
- `GET /info`   — returns app version and configuration
- Task limit enforcement via `MAX_TASKS` environment variable

### 🧪 Testing
- 10 unit tests covering all endpoints and edge cases
- All tests pass with `pytest`

### 🔍 Quality
- Code passes `flake8` static analysis (max line length: 100)

### 🐳 Docker
- Multi-stage Dockerfile (builder + slim runtime)
- Healthcheck configured
- Environment-based configuration

### ⚙️ CI Pipeline (GitHub Actions)
- Stage 1: Build — verifies app imports cleanly
- Stage 2: Test  — runs pytest suite
- Stage 3: Quality — runs flake8 linter
- Stage 4: Package — builds Docker image

---

## 🔐 Config vs Secrets

| Type   | Examples                        | How to provide        |
|--------|---------------------------------|-----------------------|
| Config | `APP_VERSION`, `MAX_TASKS`, `PORT` | `.env` / Docker `-e` |
| Secret | `SECRET_KEY`, `DB_PASSWORD`     | CI Secrets / Vault    |

---

## 🐛 Known Limitations
- Tasks are stored in-memory (no database persistence between restarts)
- No authentication layer in v1.0.0

---

## 🔮 Planned for v1.1.0
- SQLite/PostgreSQL persistence
- JWT authentication
- Pagination for task listing
