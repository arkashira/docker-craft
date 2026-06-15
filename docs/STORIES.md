# STORIES.md

## Project: docker‑craft  
**Goal** – Deliver a fully‑functional, free Docker learning platform that offers tutorials, templates, and sandboxed practice environments.  
**MVP** – A web portal where users can browse curated tutorials, launch ready‑to‑run Docker templates, and experiment in isolated containers.

---

## Epics & Story Backlog

| Epic | Story | Acceptance Criteria |
|------|-------|---------------------|
| **User Onboarding & Discovery** | **S1** As a **new learner**, I want to **register** with email or social login, so that I can **save progress** and **access personalized content**. | • Registration form validates email, password strength.<br>• Social OAuth (Google, GitHub) works.<br>• Confirmation email sent; account activated after click.<br>• User can log in/out. |
| | **S2** As a **new learner**, I want to **view a curated list of tutorials**, so that I can **pick a topic** that interests me. | • Tutorials are fetched from the public API.<br>• Each card shows title, brief description, difficulty, and tags.<br>• Pagination or infinite scroll loads 20 items at a time.<br>• Search bar filters by keyword or tag. |
| | **S3** As a **new learner**, I want to **bookmark** tutorials, so that I can **return to them later**. | • Bookmark icon toggles state.<br>• Bookmarked items appear in a dedicated “My Bookmarks” section.<br>• Bookmarking persists across sessions. |
| **Tutorial Consumption** | **S4** As a **learner**, I want to **read a tutorial** in a clean, responsive layout, so that I can **focus on learning**. | • Markdown rendered correctly (headings, code blocks, images).<br>• Syntax highlighting for code snippets.<br>• Table of contents auto‑generated and scroll‑spy enabled.<br>• Page is mobile‑friendly. |
| | **S5** As a **learner**, I want to **download a Dockerfile** and related assets, so that I can **run the example locally**. | • “Download ZIP” button downloads all files.<br>• ZIP contains Dockerfile, docker‑compose.yml, and any needed assets.<br>• README inside ZIP explains build/run steps. |
| | **S6** As a **learner**, I want to **launch a Docker template** directly from the browser, so that I can **experiment without local setup**. | • “Launch in Sandbox” button triggers a serverless container instance.<br>• Sandbox runs for 30 min, auto‑terminates after idle.<br>• User sees a live terminal (xterm.js) connected to the container.<br>• Logs and output are persisted for 24 h. |
| **Practice Environment** | **S7** As a **learner**, I want to **edit code** in the sandbox, so that I can **practice and test changes**. | • In‑browser editor (Monaco) supports Dockerfile, shell scripts, and application code.<br>• “Build & Run” button rebuilds the container and restarts services.<br>• Build output is displayed in a log panel.<br>• Errors are highlighted in the editor. |
| | **S8** As a **learner**, I want to **share my sandbox session** with peers, so that I can **collaborate**. | • “Share” button generates a unique URL.<br>• Shared session is read‑only for collaborators.<br>• Session expires after 48 h. |
| **Content Management** | **S9** As a **content curator**, I want to **create and edit tutorials** via a CMS, so that I can **keep the library up‑to‑date**. | • Admin panel lists tutorials with edit/delete options.<br>• Rich‑text editor supports Markdown and image uploads.<br>• Version history shows changes and can revert.<br>• Publishing toggles visibility to public. |
| | **S10** As a **content curator**, I want to **upload Docker templates** (Dockerfile + assets), so that learners can launch them. | • Upload form accepts ZIP or individual files.<br>• Validation checks for required files (Dockerfile, docker‑compose.yml).<br>• On success, template appears in the public list. |
| **Analytics & Feedback** | **S11** As a **product manager**, I want to **track tutorial views and sandbox usage**, so that I can **measure engagement**. | • Page views, unique visitors, and time‑on‑page logged.<br>• Sandbox creation, duration, and exit reason recorded.<br>• Data exported to a CSV via admin panel. |
| | **S12** As a **learner**, I want to **rate and comment** on tutorials, so that I can **share feedback**. | • 1–5 star rating system.<br>• Comment thread per tutorial.<br>• Moderation queue for inappropriate content. |
| **Performance & Security** | **S13** As a **system administrator**, I want to **limit sandbox CPU/memory**, so that **resource abuse is prevented**. | • Sandbox instances capped at 1 CPU, 512 MB RAM.<br>• Requests exceeding limits are throttled and logged.<br>• Idle timeout of 30 min. |
| | **S14** As a **security engineer**, I want to **sanitize user uploads**, so that **malicious code cannot harm the host**. | • File type and size validation.<br>• Virus scan (ClamAV) on uploads.<br>• Sandboxed containers run with non‑privileged user. |
| **Future Enhancements** | **S15** As a **learner**, I want to **track my progress** across tutorials, so that I can **see a learning roadmap**. | • Progress bar per tutorial (completed steps).<br>• Dashboard aggregates overall completion rate.<br>• Exportable progress report. |

---

## MVP Release Order

1. **S1 – S3** (Onboarding & Discovery)  
2. **S4 – S6** (Tutorial Consumption)  
3. **S7 – S8** (Practice Environment)  
4. **S9 – S10** (Content Management)  
5. **S11 – S12** (Analytics & Feedback)  
6. **S13 – S14** (Performance & Security)  
7. **S15** (Progress Tracking – future)

---

### Notes

- All user‑facing features must be fully responsive and accessible (WCAG 2.1 AA).  
- API endpoints should follow REST conventions and return JSON.  
- Docker sandboxing will use a lightweight orchestration layer (e.g., Docker‑Compose on a dedicated VM) with per‑session isolation.  
- CI/CD pipeline will run unit tests, linting, and integration tests on every PR.  

---
