# 📝 Task Manager API — v1.0.0

A production-ready REST API for managing tasks, built with **Python + Flask**.
Demonstrates full DevOps practices: CI pipeline, Docker packaging, versioning, and quality checks.

---

## 🚀 Features

| Endpoint               | Method | Description            |
|------------------------|--------|------------------------|
| `/health`              | GET    | Health check           |
| `/info`                | GET    | App version & config   |
| `/tasks`               | GET    | List all tasks         |
| `/tasks`               | POST   | Create a new task      |
| `/tasks/<id>`          | GET    | Get a specific task    |
| `/tasks/<id>`          | PATCH  | Mark task done/undone  |
| `/tasks/<id>`          | DELETE | Delete a task          |

---

## ⚙️ Environment Variables

| Variable      | Default   | Description                    |
|---------------|-----------|--------------------------------|
| `APP_VERSION` | `1.0.0`   | Application version (visible)  |
| `MAX_TASKS`   | `100`     | Max number of tasks allowed    |
| `PORT`        | `5000`    | Port the app listens on        |

> 🔐 **Secrets** (e.g. `SECRET_KEY`, `DB_PASSWORD`) must never be hardcoded.
> Use `.env` locally and CI secret managers in production.

---

## 🖥️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourname/task-manager-api.git
cd task-manager-api

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy env file
cp .env.example .env

# 5. Run the app
python run.py
```

Visit:
- Web UI: http://localhost:5000/
- API info: http://localhost:5000/info

---

## 🧪 Run Tests

```bash
pytest tests/ -v
```

## 🌐 Web Interface

The project includes a simple browser UI for real-time API usage.

- Open: `http://localhost:5000/`
- Create tasks with form
- Mark tasks done/undone
- Delete tasks
- Refresh list

---

## 🔍 Run Linter

```bash
flake8 app/ run.py
```

---

## 🐳 Docker

```bash
# Build image
docker build -t task-manager-api:1.0.0 .

# Run container
docker run -d -p 5000:5000 \
  -e APP_VERSION=1.0.0 \
  -e MAX_TASKS=50 \
  --name task-api \
  task-manager-api:1.0.0

# Check health
curl http://localhost:5000/health

# Stop & remove
docker stop task-api && docker rm task-api
```

---

## 🌿 Git Workflow

```
main
└── feature/task-api      ← developed here
    └── merged via PR → main
        └── tagged: v1.0.0
```

```bash
# Tag the release
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

---

## 📦 Release

See [release-notes.md](release-notes.md) for v1.0.0 details.
