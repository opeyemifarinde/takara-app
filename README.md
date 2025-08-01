# TÀKÀRÀ – The African Writers’ Hub

TÀKÀRÀ is a mobile‑first creative writing and storytelling platform for Nigerian and African writers.  It allows authors to publish poems, essays and stories in multiple languages and enables readers to discover and follow local voices.  This repository contains the full stack implementation (React Native app, FastAPI backend), CI/CD pipeline and documentation.

## Repository Structure

```
takara-app/
├── frontend/         # React Native source code (Expo or bare workflow)
├── backend/
│   ├── app/
│   │   └── main.py   # FastAPI entry point
│   └── requirements.txt
├── docs/
│   ├── BRD.md        # Business Requirements Document
│   └── UserStories.md# Agile user stories
├── .github/workflows/
│   ├── backend.yml   # GitHub Actions for backend
│   └── frontend.yml  # GitHub Actions for frontend
└── README.md         # This file
```

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/) for the React Native app
- [Python 3.10+](https://www.python.org/) and [pip](https://pip.pypa.io/) for the backend

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
yarn install
# If using Expo
expo start
```

### Documentation

The `docs/` folder contains the Business Requirements Document (BRD) and detailed user stories.  The system architecture and DevOps plan are described in `system_architecture_report.md` in the root of this repository.

### Contributing

1. Fork the repository.
2. Create a feature branch off `dev` (e.g. `feature/new-component`).
3. Commit your changes with clear messages.
4. Open a Pull Request against `dev`.
5. Ensure tests pass and code is linted before requesting review.
