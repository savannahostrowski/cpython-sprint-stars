# Core Stars

The CPython core team leaderboard, built from [Sprint Stars](https://github.com/savannahostrowski/sprint-stars).

[View the board](https://cpython-sprint-stars.fastapicloud.dev/).

`metadata.toml` contains this board’s repositories, roster, account aliases, and branding. For another team, start from the Sprint Stars template.

## Run locally

You'll need Python 3.15+ and a GitHub personal access token with public repository read access.

```sh
export GITHUB_TOKEN="your-token"
uv sync
uv run python dev.py
```

Open [localhost:8774](http://127.0.0.1:8774/). Restart after changing metadata.

## Deploy

From this repository’s root, with the existing FastAPI Cloud app linked:

```sh
uv run fastapi deploy
```

The deployed app needs its own `GITHUB_TOKEN` secret. See the [FastAPI Cloud docs](https://fastapicloud.com/docs/fastapi-cloud-cli/deploy/).
