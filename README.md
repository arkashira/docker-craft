<h3 align="center">🛠️ docker-craft</h3>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Build: GitHub Actions](https://github.com/axentx/docker-craft/actions/workflows/ci.yml/badge.svg)](https://github.com/axentx/docker-craft/actions/workflows/ci.yml)
[![Stars](https://img.shields.io/github/stars/axentx/docker-craft?style=social)](https://github.com/axentx/docker-craft)

</div>

---

# 🚀 docker-craft

**Empower Python developers with a Docker-first FastAPI starter template that skips boilerplate and jumps straight to building web services.**

## Why docker-craft?

- **Minimal & Opinionated**: Clean directory structure (`src/`, `tests/`, `docs/`) with no unnecessary complexity
- **Ready for DevOps**: Multi-stage Dockerfile + GitHub Actions CI/CD workflow included out-of-the-box
- **FastAPI Powered**: Built with FastAPI and Uvicorn for high-performance, type-safe APIs
- **Poetry Integrated**: Dependency management via Poetry ensures reproducible environments
- **Learning-Friendly**: Ideal for beginners and educators to focus on logic, not setup
- **Extensible Skeleton**: Designed to be extended—add your business logic without config headaches
- **Sandbox-Tested**: Real-world tested and validated in containerized environments

## Feature Overview

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| FastAPI Web App      | Ready-to-use FastAPI app scaffold                                         |
| Docker Support       | Multi-stage Dockerfile for lightweight, production-ready containers         |
| CI/CD Pipeline       | GitHub Actions workflow for linting, testing, and image building            |
| Poetry Dependency mgmt | Uses Poetry for managing dependencies and virtual environments          |
| Test Suite           | Includes pytest setup and test directory for unit/integration testing       |
| Documentation        | Docs folder for project documentation and API specs                         |

## Tech Stack

- **FastAPI**
- **Python**
- **Docker**
- **GitHub Actions**
- **Poetry**

## Project Structure

```
.
├── business/
├── docs/
├── src/
│   └── main.py
├── tests/
├── README.md
├── pyproject.toml
└── .github/workflows/ci.yml
```

## Getting Started

### Prerequisites

Ensure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

### Installation

```bash
git clone https://github.com/axentx/docker-craft.git
cd docker-craft
poetry install
```

### Run Locally

```bash
poetry run uvicorn src.main:app --reload
```

### Run Tests

```bash
poetry run pytest tests/
```

## Deploy

Deploy using Docker:

```bash
docker build -t docker-craft .
docker run -p 8000:8000 docker-craft
```

Or deploy via GitHub Actions by pushing to the `main` branch.

## Status

This project is a **skeleton template** designed for rapid prototyping and learning.  
Latest commit: `b4250c4 feat(docker-craft): real, sandbox-tested implementation`

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.