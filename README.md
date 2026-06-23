<h3 align="center">🛠️ docker-craft</h3>

<div align="center">
  <a href="https://github.com/your-org/docker-craft"><img src="https://img.shields.io/github/license/your-org/docker-craft?color=blue" alt="License"></a>
  <a href="https://github.com/your-org/docker-craft"><img src="https://img.shields.io/github/languages/top/your-org/docker-craft?color=orange&logo=python" alt="Language"></a>
  <a href="https://github.com/your-org/docker-craft/actions"><img src="https://img.shields.io/github/actions/workflow/status/your-org/docker-craft/ci.yml?branch=main&label=CI&logo=github" alt="Build"></a>
  <a href="https://github.com/your-org/docker-craft"><img src="https://img.shields.io/github/stars/your-org/docker-craft?style=social" alt="Stars"></a>
</div>

---

# 🚀 docker-craft
**Power developers with a ready‑to‑extend Dockerized web‑app skeleton.** Jump‑start your project with built‑in CI/CD and a clean, opinionated layout.

## Why docker-craft?
- **Zero‑setup scaffolding** – All directories (`src/`, `tests/`, `docs/`) are pre‑created, letting you focus on business logic from day 1.  
- **CI/CD ready** – GitHub Actions workflow ships with lint, test, and Docker image build steps out of the box.  
- **Docker‑first** – The repo is structured for a multi‑stage Dockerfile, so you can containerize your app in a single `docker build` command.  
- **Python‑centric** – A minimal `pyproject.toml` gives you a reproducible environment with only the essentials (`fastapi`, `uvicorn`).  
- **Learner‑friendly** – Designed for developers who want a hands‑on template to experiment, learn, and iterate without boilerplate distractions.  
- **Extensible** – Add your own source files, Dockerfile, or extra services without fighting the existing layout.  
- **Open‑source & free** – MIT‑licensed, no hidden fees, perfect for personal projects, startups, or classroom labs.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Skeleton Layout** | Pre‑populated `src/`, `tests/`, `docs/`, and `business/` directories. |
| **GitHub Actions CI** | Lint → Test → Docker build pipeline that runs on every push. |
| **Python Project Config** | `pyproject.toml` with Poetry‑compatible metadata and minimal deps. |
| **Docker‑Ready** | Ready for a multi‑stage `Dockerfile`; `docker-compose.yml` placeholder included. |
| **Testing Boilerplate** | `pytest` configuration and example test file. |
| **Documentation Stubs** | `README.md`, `docs/` folder, and placeholders for API docs. |
| **License** | MIT – free for commercial and non‑commercial use. |

## Tech Stack
- **Python** – Core language for the application code.  
- **Docker** – Container runtime; the template expects a Dockerfile.  
- **GitHub Actions** – CI/CD pipeline for linting, testing, and image building.

## Project Structure
```
docker-craft/
├─ business/          # Business‑logic stubs & future service modules
├─ docs/              # Documentation assets (API spec, guides)
├─ src/               # Application source code (empty placeholder)
├─ tests/             # Test suite (pytest ready)
├─ README.md          # ← you are here
└─ pyproject.toml     # Project metadata & dependencies
```

## Getting Started
```bash
# 1️⃣ Clone the repo
git clone https://github.com/your-org/docker-craft.git
cd docker-craft

# 2️⃣ Install Python dependencies (editable mode)
pip install -e .

# 3️⃣ Run the test suite
pytest

# 4️⃣ Build the Docker image (replace <your-tag> as needed)
docker build -t your-org/docker-craft:<your-tag> .

# 5️⃣ Run the container locally
docker run -p 8000:8000 your-org/docker-craft:<your-tag>
```

## Deploy
The repository ships with a GitHub Actions workflow that pushes the built image to Docker Hub on every tag push.

```yaml
# .github/workflows/ci.yml (excerpt)
name: CI

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install -e .
      - name: Run tests
        run: pytest
      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USER }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build & push image
        run: |
          docker build -t ${{ secrets.DOCKERHUB_USER }}/docker-craft:${{ github.ref_name }} .
          docker push ${{ secrets.DOCKERHUB_USER }}/docker-craft:${{ github.ref_name }}
```

Push a new tag to trigger the pipeline:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## Status
🟢 Actively maintained – latest commit `eb48f4c` adds a sandbox‑tested implementation and updates CI.

## Contributing
Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose enhancements or report issues.

## License
This project is licensed under the **MIT License**.