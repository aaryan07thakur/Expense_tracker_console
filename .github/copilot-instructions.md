<!-- Copilot instructions for AI coding agents working on this repo -->
# Project: `expence_tracker`

Summary
- The repository currently contains a single empty `doc.txt`. No source code, build, or test files are present. Before making large changes, confirm language, framework, and scope with the human owner.

Primary goals for AI agents
- Quickly detect repository shape: list top-level files and common language indicators (`package.json`, `pyproject.toml`, `requirements.txt`, `src/`, `app/`, `README.md`). If none exist, ask the user for intended language and framework before scaffolding.
- Avoid assumptions. When in doubt, propose a minimal scaffold and wait for approval.

What to do first (handy checklist)
- Run a repo scan: list root and search for common files. Example PowerShell commands:
  - `Get-ChildItem -Path . -Force`
  - `Get-ChildItem -Recurse -Filter package.json -ErrorAction SilentlyContinue`
- If only `doc.txt` exists (as in this workspace), prompt the owner: "Which language and framework should I use?" Provide 2–3 sensible scaffolding options.

Project-specific conventions discovered
- Repo name: `expence_tracker` (note spelling). No code files found to infer conventions.
- Windows is the reported dev OS; prefer PowerShell command examples when offering terminal steps.

Scaffolding guidance (ask before creating)
- Offer minimal scaffolds per language:
  - Python: create `src/`, `tests/`, `pyproject.toml` or `requirements.txt`, and a basic `README.md` with run/test commands using the system Python.
  - Node.js: create `package.json`, `src/`, `tests/`, and `README.md` with `npm run` scripts.
- When scaffolding, include small example code and a single unit test to validate the layout.

Developer workflows to document when code is present
- Build: state the command and environment (e.g., `python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1; pip install -r requirements.txt`).
- Test: prefer a single test command (e.g., `pytest` or `npm test`).
- Lint/format: show the exact tool and invocation (e.g., `black .`, `eslint .`).

Merge strategy for existing AI instructions
- If a `.github/copilot-instructions.md` already exists, preserve sections titled `Project Overview` and `Developer Workflows`, and append or update a short "Repo state" note that reflects current files.

Communication and PR habits
- Create small, focused commits with clear messages: `feat: add initial scaffold for <language>` or `chore: add tests for <component>`.
- Open a draft PR for any non-trivial scaffold and request explicit approval before further expansion.

When to ask the user
- Confirm language/framework before adding source code.
- Ask for credentials or external service details if integration is required (do not create or store secrets in the repo).

Files to reference when present
- `README.md` — primary place for run/build/test instructions.
- `package.json`, `pyproject.toml`, `requirements.txt` — indicate language, dependencies, and scripts.
- `src/`, `app/`, `lib/` — implementation locations. Use these paths when adding new modules.

If you update these instructions
- Keep the file short (20–50 lines). Add a one-line changelog entry at the bottom with date and a short rationale.

Next step for an AI agent now
- Prompt the repo owner asking which language/framework to use and whether they want an initial scaffold. Provide two scaffolding options (Python and Node.js) as quick choices.

-- End of instructions
