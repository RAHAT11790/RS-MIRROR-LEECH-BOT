# RS Mirror Leech Bot

A native-Python Telegram mirror/leech bot packaged under the **RS Mirror Leech Bot** project name. Docker and `.env` configuration are not used. Configure the bot in `config.py` and start it with `python3 main.py`.

## Features

- Mirror and leech tasks supported by the included bot modules
- URL-based downloads and supported source integrations from the base project
- Telegram bot, optional user session, and helper clients
- MongoDB-backed settings and task metadata
- Configurable admin, authorized chats, and logging destinations
- Native Linux setup; no Docker, Compose, or `.env` file

## Requirements

- Python 3.10 or newer (use a version supported by all installed dependencies)
- MongoDB connection URI
- Telegram Bot Token, Telegram API ID, and API Hash
- `aria2`, `ffmpeg`, and other system tools required by the enabled download/upload features

## Installation (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git build-essential aria2 ffmpeg p7zip-full curl
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```

## Configuration

Open `config.py` and fill in the values in **RS Mirror Leech Bot: simplified primary settings**. At minimum, set:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_ID = 123456
API_HASH = "YOUR_TELEGRAM_API_HASH"
DATABASE_URL = "YOUR_MONGODB_URI"
ADMIN_ID = 123456789
```

Logging and authorization fields are also available in `config.py`:

- `LOG_CHANNEL`: Telegram channel ID used for task logs
- `LOG_GROUP`: Telegram group ID used for link/task logs
- `AUTHORIZED_CHANNEL`: optional authorized channel ID
- `AUTHORIZED_GROUP`: optional authorized group ID
- `ADMIN_ID`: bot owner/admin Telegram user ID

Use numeric IDs where appropriate. Leave optional values empty if you do not need them. The project retains compatibility settings for its existing modules; all settings are in `config.py`, and there is no `.env` file.

## Start

From the project root, with the virtual environment activated:

```bash
python3 main.py
```

`main.py` is the single entry point. It launches the existing bot package; do not run Docker commands.

## Notes

- Run from the project root so relative configuration and service paths resolve correctly.
- Some optional integrations need their own API keys or external services. Enable only the integrations you actually use in `config.py`.
- This package is based on an existing open-source mirror/leech codebase. Its original `LICENSE` file is retained; changing project branding does not transfer ownership of third-party code or dependencies.
- Test first with a private Telegram chat and non-sensitive files before running large jobs.
