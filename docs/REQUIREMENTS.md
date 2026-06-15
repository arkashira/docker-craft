# REQUIREMENTS.md

## Project Overview

**Project Name:** `docker-craft`  
**Repository:** `arkashira/docker-craft`  
**Purpose:** Provide a free, comprehensive Docker learning platform that offers tutorials, templates, and practice environments for developers of all skill levels.  
**Target Audience:** Beginners, intermediate developers, and educators looking for curated Docker resources.  
**Business Goal:** Increase user engagement and retention by delivering high‑quality, up‑to‑date Docker content while ensuring platform reliability, security, and scalability.

---

## Functional Requirements

| ID | Description | Acceptance Criteria |
|----|-------------|---------------------|
| **FR‑1** | **Content Management** | • Admins can create, edit, and delete tutorials, templates, and practice environments via a web UI.<br>• Content is versioned; previous versions are archived and viewable.<br>• Each resource has metadata: title, description, tags, difficulty level, and estimated completion time. |
| **FR‑2** | **User Authentication & Authorization** | • Users can sign up, log in, and reset passwords using email or OAuth (Google, GitHub).<br>• Roles: *Admin*, *Editor*, *Learner* with appropriate permissions.<br>• Session tokens are JWT‑based with 24‑hour expiry. |
| **FR‑3** | **Search & Filtering** | • Full‑text search across titles, descriptions, and tags.<br>• Filters by difficulty, resource type, and date added.<br>• Search results are paginated (default 20 per page). |
| **FR‑4** | **Practice Environments** | • Each tutorial can optionally launch a sandbox Docker environment via a “Run in Browser” button.<br>• Environments are isolated per user and automatically destroyed after 30 minutes of inactivity.<br>• Users can export the environment as a Dockerfile or Docker Compose file. |
| **FR‑5** | **Progress Tracking** | • Learners can mark resources as “completed.”<br>• Dashboard shows completion percentage per tutorial series.<br>• Progress is stored in a relational database and syncs across devices. |
| **FR‑6** | **Analytics & Feedback** | • Collect anonymous usage metrics (page views, time on page, environment launches).<br>• Users can submit feedback/comments on resources.<br>• Admins can view analytics dashboards (via Grafana integration). |
| **FR‑7** | **API Layer** | • RESTful API endpoints for all CRUD operations.<br>• Rate‑limit: 100 requests/minute per IP.<br>• API documentation generated via OpenAPI 3.0. |
| **FR‑8** | **CI/CD Pipeline** | • Automated tests run on every push to `main`.<br>• Docker images built and pushed to Docker Hub on successful merge.<br>• Deployments to staging and production via GitHub Actions. |
| **FR‑9** | **Internationalization (i18n)** | • Support for English and Spanish locales.<br>• All UI strings are externalized in JSON files. |
| **FR‑10** | **Accessibility** | • WCAG 2.1 AA compliance for all pages.<br>• Keyboard navigation and ARIA labels for interactive components. |

---

## Non‑Functional Requirements

| ID | Requirement | Details |
|----|-------------|---------|
| **NFR‑1** | **Performance** | • Page load time < 2 s (95th percentile).<br>• API response < 200 ms for 90 % of requests. |
| **NFR‑2** | **Scalability** | • Horizontal scaling of web & API services behind a load balancer.<br>• Docker practice environments use a Kubernetes cluster with auto‑scaling (min 2 nodes, max 20). |
| **NFR‑3** | **Reliability** | • 99.9 % uptime SLA.<br>• Automatic failover for database (PostgreSQL) using Patroni.<br>• Daily backups and point‑in‑time recovery. |
| **NFR‑4** | **Security** | • OWASP Top‑10 mitigations (e.g., CSRF tokens, input validation).<br>• HTTPS enforced everywhere.<br>• Secrets stored in HashiCorp Vault; no hard‑coded credentials. |
| **NFR‑5** | **Compliance** | • GDPR‑compliant data handling: user data can be exported or deleted on request.<br>• Data residency: all user data stored in EU‑region cloud. |
| **NFR‑6** | **Maintainability** | • Codebase follows SOLID principles.<br>• Automated linting (ESLint, Prettier) and formatting.<br>• Documentation coverage ≥ 80 %. |
| **NFR‑7** | **Observability** | • Centralized logging (ELK stack).<br>• Metrics exposed via Prometheus; alerts for anomalies. |
| **NFR‑8** | **Usability** | • Mobile‑first responsive design.<br>• Clear call‑to‑action buttons for “Run in Browser” and “Download Dockerfile.” |

---

## Constraints

1. **Technology Stack**  
   - Frontend: React 18 + TypeScript + Tailwind CSS.  
   - Backend: Node.js 20 + Express + TypeScript.  
   - Database: PostgreSQL 15 (primary), Redis for caching.  
   - Docker practice environments run on a managed Kubernetes cluster (GKE or EKS).  

2. **Hosting**  
   - All services deployed on AWS (EU‑Central).  
   - CI/CD via GitHub Actions; Docker images pushed to Docker Hub.  

3. **Licensing**  
   - All third‑party libraries must be MIT, Apache‑2.0, or BSD‑3.  
   - Content created by the team must be licensed under CC‑BY‑4.0.  

4. **Resource Limits**  
   - Each practice environment capped at 2 GB RAM and 1 CPU core.  
   - Total concurrent environments ≤ 200 to stay within budget.  

5. **Budget**  
   - Monthly cloud spend capped at $5,000.  

---

## Assumptions

- Users have a modern browser (Chrome, Firefox, Safari) with JavaScript enabled.  
- Internet connectivity is available for Docker image pulls.  
- Admins will provide initial content (tutorials, templates) before launch.  
- The platform will be open‑source; contributions will follow the existing repo’s contribution guidelines.  

---

## Deliverables

1. **Functional Codebase** – fully tested and documented.  
2. **Docker Compose** for local development.  
3. **CI/CD Pipeline** scripts.  
4. **API Documentation** (OpenAPI spec).  
5. **User & Admin Guides** (Markdown).  
6. **Security & Compliance Report** (post‑launch).  

---

## Acceptance Checklist

- [ ] All FRs implemented and unit‑tested.  
- [ ] NFRs met in performance and security audits.  
- [ ] Documentation complete and reviewed.  
- [ ] CI/CD pipeline passes all checks.  
- [ ] Deployment to staging passes smoke tests.  
- [ ] Final sign‑off from product owner.  

---
