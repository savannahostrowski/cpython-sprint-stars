# Core Stars

A leaderboard for issues closed, PRs opened, and code reviews across GitHub repositories. Configure it with your team and public repos.

## Getting started

Create a repo with **Use this template**, then clone it. You'll need Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
cp metadata.example.toml metadata.toml
```

Edit `metadata.toml` with your organizations, repositories, and participants:

```toml
name = "Our team leaderboard"
organizations = ["our-org"]
repositories = ["another-org/shared-project"]
contributors = ["alice", "bob"]
refresh_minutes = 20
```

Use `organizations = []` to track only specific repos. An org includes all its public repos, including forks and archives. Overlapping repo lists count once.

Then start the app:

```sh
uv sync
uv run python dev.py
```

Open [localhost:8774](http://127.0.0.1:8774/). The dev server uses your GitHub CLI login, or `GITHUB_TOKEN` if you've set it. For larger orgs, you'll want authentication to avoid GitHub's unauthenticated rate limits.

The [setup guide](SETUP.md) covers authentication and deployment. [metadata.example.toml](metadata.example.toml) shows display names, account aliases, timezones, and an optional CSV roster. Restart the app after changing metadata.

## What counts

The board defaults to the current Monday–Sunday week. You can select any inclusive date range up to 93 days.

- **Closures:** issues and PRs closed during the range, credited to the person who closed them. Merged PRs count; reopened items don't.
- **PRs:** PRs opened during the range, credited to the author.
- **Reviews:** one point per person per PR reviewed during the range. Repeated reviews of the same PR count once. Reviews of your own PRs don't count.
- **All:** the sum of those three.

Reviewing and merging a PR count as separate actions. Backport PRs count too. Comments, commits, and branch pushes don't. Human closures and reviews of bot-created PRs count, but bots don't appear on the board.

Only configured participants earn points. The participant list applies to historical ranges too.

## Refreshing data

The server fetches from GitHub every 20 minutes by default, and open pages update automatically. Viewers share a cache within each server process. During GitHub outages or failed fetches, the app keeps the previous results and marks them stale.

The cache is in memory. Keep at least one worker running for background refreshes; multiple workers or replicas each maintain their own cache.

## Development

FastAPI backend, plain HTML/CSS/JavaScript frontend. No database or frontend build step.

```sh
uv run python -m pytest
node --test tests/test_frontend.mjs
```

For FastAPI Cloud, the entrypoint is `main:app` and the health endpoint is `/health`. See the [deployment instructions](SETUP.md#3-deploy-your-own-app-optional) before deploying your copy.
