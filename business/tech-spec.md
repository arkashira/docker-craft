# tech‑spec.md – Docker‑Craft v1  

---  

## 1. Stack  

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **Language** | **TypeScript (Node.js 20)** | Strong typing reduces bugs in a learning‑platform; huge ecosystem for CLI & Docker SDK. |
| **Web Framework** | **Fastify** (with `fastify‑swagger` plugin) | Ultra‑fast, low‑overhead, built‑in schema validation – ideal for API‑first product. |
| **Docker Integration** | **dockerode** (Node Docker SDK) | Mature wrapper around Docker Engine API; works locally & on remote Docker hosts. |
| **Template Engine** | **Handlebars** (for tutorial markdown → HTML) | Simple, logic‑less templating; easy to embed code snippets. |
| **Database** | **PostgreSQL 15** (hosted on **Supabase** free tier) | Relational model fits tutorials, users, tags; Supabase gives instant auth + realtime. |
| **Cache / Session Store** | **Redis 7** (managed on **Upstash** free tier) | Low‑latency storage for JWT revocation list & short‑lived practice‑env metadata. |
| **Runtime** | **Docker** (containerised services) | Guarantees reproducible dev/prod environments; aligns with product domain. |
| **Package Manager** | **pnpm** (workspace monorepo) | Faster installs, deterministic lockfile, ideal for multi‑package repo (API, CLI, UI). |
| **Static Front‑end** | **React 18 + Vite** (TS) | Fast dev HMR, easy static export for docs/tutorials. |
| **CI/CD** | **GitHub Actions** + **Docker Buildx** | Native to repo; supports multi‑arch images for Linux/ARM. |

---  

## 2. Hosting (Free‑Tier‑First)  

| Component | Provider (Free Tier) | Deployment Model |
|-----------|----------------------|------------------|
| **API / Backend** | **Railway** (up to 500 hrs/mo, 1 GB RAM) | Docker image `ghcr.io/arkashira/docker-craft-api:latest` |
| **PostgreSQL** | **Supabase** (free tier: 500 MB storage, 2 GB bandwidth) | Managed DB, auto‑SSL |
| **Redis** | **Upstash** (free tier: 10 k ops/s, 256 MB) | Serverless Redis, env‑var endpoint |
| **Static Front‑end** | **Vercel** (free hobby) | `npm run build && vercel --prod` |
| **Docker‑Practice‑Envs** | **GitHub Codespaces** (free for public repos) **or** **Play with Docker** (web‑based sandbox) | On‑demand containers launched via Docker Engine API on a **self‑hosted runner** (low‑cost EC2 t4g.micro) – fallback to GitHub Actions self‑hosted runner for scaling. |
| **Observability** | **Logtail** (free tier 10 GB/mo) + **Prometheus‑Grafana Cloud** (free tier) | Logs streamed via `pino` → Logtail; metrics scraped by Prometheus remote‑write. |

*All secrets stored in GitHub Encrypted Secrets; runtime env vars injected by Railway/Vercel.*  

---  

## 3. Data Model  

| Table / Collection | Key Fields | Description |
|--------------------|------------|-------------|
| **users** | `id (uuid PK)`, `email (unique)`, `password_hash`, `role (enum: learner, contributor, admin)`, `created_at` | Authenticated accounts; role‑based IAM. |
| **tutorials** | `id (uuid PK)`, `slug (unique)`, `title`, `description`, `markdown_body`, `author_id (FK → users)`, `tags (array)`, `created_at`, `updated_at` | Public learning modules. |
| **templates** | `id (uuid PK)`, `name`, `dockerfile_path`, `compose_yaml`, `description`, `author_id`, `public (bool)`, `created_at` | Boiler‑plate Docker projects that can be instantiated. |
| **practice_sessions** | `id (uuid PK)`, `user_id (FK)`, `template_id (FK)`, `container_id (Docker Engine ID)`, `status (enum: pending, running, stopped, error)`, `started_at`, `ended_at`, `logs_url` | Ephemeral envs; TTL = 24 h. |
| **tags** | `id (uuid PK)`, `name (unique)` | Normalised tag list for tutorials/templates. |
| **api_keys** (optional) | `id (uuid PK)`, `key (hashed)`, `owner_id (FK)`, `scopes (json)`, `expires_at` | For third‑party integrations (e.g., VSCode extension). |

Indexes:  
- `users.email` (unique)  
- `tutorials.slug` (unique)  
- `templates.name` + `author_id` (unique)  
- `practice_sessions.user_id + status` (for dashboard queries)  

---  

## 4. API Surface  

All endpoints are versioned under `/api/v1`. JSON request/response bodies; OpenAPI 3.1 generated via `fastify‑swagger`.  

| Method | Path | Purpose | Request Body / Params | Response |
|--------|------|---------|-----------------------|----------|
| **POST** | `/auth/register` | Create new learner account | `{email, password}` | `{userId, token}` |
| **POST** | `/auth/login` | Issue JWT | `{email, password}` | `{token, refreshToken}` |
| **GET** | `/tutorials` | List public tutorials (paginated) | `?page=&limit=&tag=` | `{items:[...], total, page, limit}` |
| **GET** | `/tutorials/:slug` | Retrieve single tutorial (markdown + rendered HTML) | – | `{id, title, html, tags, author}` |
| **POST** | `/templates` *(admin/ contributor)* | Publish a new Docker template | `{name, dockerfile, compose, description, public}` | `{templateId}` |
| **GET** | `/templates/:id` | Fetch template definition | – | `{id, name, dockerfile, compose, description}` |
| **POST** | `/sessions` | Spin up a practice environment from a template | `{templateId}` (JWT required) | `{sessionId, containerId, status, expiresAt}` |
| **GET** | `/sessions/:id` | Get status / logs URL of a running session | – | `{status, logsUrl, createdAt, expiresAt}` |
| **DELETE** | `/sessions/:id` | Terminate a running container early | – | `{deleted:true}` |
| **GET** | `/healthz` | Liveness / readiness probe (K8s) | – | `{status:"ok", uptimeSec}` |
| **GET** | `/metrics` | Prometheus‑compatible metrics endpoint | – | `# HELP ...` |

*All mutating endpoints require `Authorization: Bearer <JWT>`; admin‑only routes enforce `role === "admin"`.*  

---  

## 5. Security Model  

| Aspect | Implementation |
|--------|----------------|
| **Authentication** | **JWT (HS256)** signed with a 256‑bit secret stored in Railway env (`JWT_SECRET`). Access token TTL = 1 h; refresh token stored in HttpOnly Secure cookie. |
| **Authorization (IAM)** | Role‑based checks in Fastify hooks (`preHandler`). Roles: `learner` (read‑only), `contributor` (can create templates), `admin` (full CRUD). |
| **Secrets Management** | All secrets (DB URL, Redis URL, Docker Engine socket endpoint, JWT secret) kept in provider‑specific secret stores (Railway env, Vercel env). No secret in repo. |
| **Container Isolation** | Practice sessions run in **user‑namespace‑isolated Docker containers** with limited CPU/memory (`--cpus=0.5 --memory=512m`). Network is sandboxed (no outbound internet). |
| **Input Validation** | Fastify schema validation for every request; Dockerfile/compose content sanitized via `dockerfile‑lint` before container creation. |
| **Rate Limiting** | `fastify‑rate-limit` – 60 req/min per IP for public endpoints; 200 req/min for authenticated. |
| **CORS** | Strict whitelist: `https://docker-craft.vercel.app` + `https://api.docker-craft.com`. |
| **Data Encryption** | At rest: PostgreSQL Transparent Data Encryption (managed by Supabase). In transit: enforced HTTPS everywhere (Railway & Vercel provide TLS). |
| **Audit Logging** | Every auth event, template creation, and session launch logged with userId, timestamp, IP, and outcome to Logtail. |

---  

## 6. Observability  

| Layer | Tool / Technique |
|-------|------------------|
| **Logging** | `pino` logger → JSON → Logtail (free tier). Include requestId, userId, endpoint, latency, error stack. |
| **Metrics** | `prom-client` library exposing `/metrics`. Key metrics: `http_requests_total`, `http_request_duration_seconds`, `active_sessions`, `session_start_total`, `session_error_total`. Remote‑write to **Prometheus Cloud** (free tier). |
| **Tracing** | **OpenTelemetry** (Node SDK) → Export to **Jaeger** (hosted on Railway via Docker). Trace spans for auth, DB queries, Docker SDK calls. |
| **Health Checks** | `/healthz` returns `status`, `uptime`, DB connectivity, Redis ping. Integrated with Railway auto‑restart. |
| **Dashboards** | Grafana Cloud dashboards pre‑built for request latency, error rates, container count. |
| **Alerting** | Prometheus alerts → Slack webhook (via Alertmanager) on: `session_error_total > 5/min`, `http_5xx_rate > 1%`, `cpu_usage > 80%` on API host. |

---  

## 7. Build / CI  

**GitHub Actions Workflow (`.github/workflows/ci.yml`)**  

```yaml
name: CI / CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - name: Install deps
        run: pnpm install --frozen-lockfile
      - name: Lint
        run: pnpm lint
      - name: Unit Tests
        run: pnpm test --coverage
      - name: Build API Docker image
        uses: docker/build-push-action@v5
        with:
          context: ./api
          push: false
          tags: docker-craft-api:ci-${{ github.sha }}
          cache-from: type=registry,ref=ghcr.io/arkashira/docker-craft-api:cache
          cache-to: type=registry,ref=ghcr.io/arkashira/docker-craft-api:cache,mode=max

  deploy:
    needs: lint-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - name: Install deps
        run: pnpm install --frozen-lockfile
      - name: Build & push API image
        uses: docker/build-push-action@v5
        with:
          context: ./api
          push: true
          tags: ghcr.io/arkashira/docker-craft-api:latest
          platforms: linux/amd64,linux/arm64
      - name: Deploy to Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: |
          curl -X POST https://backboard.railway.app/v1/projects/${{ secrets.RAILWAY_PROJECT_ID }}/deploy \
            -H "Authorization: Bearer $RAILWAY_TOKEN" \
            -H "Content-Type: application/json" \
            -d '{"image":"ghcr.io/arkashira/docker-craft-api:latest"}'
```

*Key points*  

- **pnpm** for deterministic lockfile.  
- Linting via **ESLint** + **Prettier**.  
- Tests using **Jest** with coverage > 80 %.  
- Docker multi‑arch build to support both x86_64 and ARM (GitHub Actions runners).  
- Deploy step uses Railway CLI (via API) – no manual SSH.  
- Separate workflow (`e2e.yml`) can spin up a temporary Railway preview environment for integration tests (using `railway up` in a container).  

---  

**End of tech‑spec.md**.  