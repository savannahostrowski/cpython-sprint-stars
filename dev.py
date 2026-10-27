"""Local preview using existing GitHub CLI authentication, without saving a token."""
import os
import shutil
import subprocess

import uvicorn

if __name__ == "__main__":
    if not os.getenv("GITHUB_TOKEN") and shutil.which("gh"):
        auth = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if auth.returncode == 0 and auth.stdout.strip():
            os.environ["GITHUB_TOKEN"] = auth.stdout.strip()
    print("GitHub authentication: " + ("configured" if os.getenv("GITHUB_TOKEN") else "unauthenticated"), flush=True)
    uvicorn.run("main:app", host="127.0.0.1", port=8774)
