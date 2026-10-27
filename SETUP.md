# Set up your team's leaderboard

You need Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/). No database or frontend build is required.

## 1. Configure your copy

On GitHub, select **Use this template → Create a new repository**, then clone your new repository and enter its directory. You can also start from a separate copy of this project. If copying an existing deployment's directory, omit `.venv/`, `.env`, and `.fastapicloud/`; the last folder links to that deployment's app.

From the project directory:

```sh
cp metadata.example.toml metadata.toml
```

Edit `metadata.toml`:

- Set `name` and optionally `brand`.
- Replace `your-org` in `organizations`, or use `organizations = []` and list individual `owner/repo` names in `repositories`. Only public repositories are supported.
- Replace `alice` and `bob` in `contributors` with your participants' GitHub usernames. Display names are optional. Only the people you list will be ranked unless you configure a CSV roster.
- Optionally configure account aliases, your timezone, or the refresh interval. Leave the optional CSV roster commented out for a fixed participant list.

The app reads and validates this file at startup. Restart or redeploy after edits. Membership applies to every date range, including historical ranges.

## 2. Authenticate and start

For dependable GitHub API limits, either set a `GITHUB_TOKEN` environment variable in your shell, or use an existing [GitHub CLI](https://cli.github.com/) login. To sign in with the CLI:

```sh
gh auth login
```

Then run:

```sh
uv sync
uv run python dev.py
```

Open [localhost:8774](http://127.0.0.1:8774/). `dev.py` automatically uses your GitHub CLI token when `GITHUB_TOKEN` is absent. It reports whether authentication is configured. A `.env` file is not automatically loaded by this runner; keep tokens out of metadata and committed files.

The first load fetches your team's data. Saved activity snapshots are excluded from Git; a locally supplied snapshot is ignored when its configuration differs. The page defaults to the current week. Change the date fields for an inclusive range of up to 93 days. The All, Closures, PRs, and Reviews tabs rank the configured participants.

## 3. Deploy your own app (optional)

Set up a separate FastAPI Cloud app for your copy and set its `GITHUB_TOKEN` environment secret. Do not reuse the original project's `.fastapicloud/cloud.json` app identity. From your project's directory, use:

```sh
uv run fastapi deploy
```

The project already specifies `main:app` as the entrypoint and exposes `/health`. Include `metadata.toml`, `config.py`, and the static assets in the deployment.

Keep at least one replica running for background refreshes without visitors. One worker/replica shares its cache across viewers; multiple processes or replicas fetch independently. Server data and open browser pages refresh every 20 minutes by default, as configured by `refresh_minutes`.

See [README.md](README.md) for scoring rules, CSV roster configuration, caching, and outage handling.
