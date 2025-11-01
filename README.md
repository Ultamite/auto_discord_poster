# auto_discord_poster

A small Python utility to post messages automatically to a Discord channel.

This repository contains a simple bot script (`bot.py`) that can be used to send scheduled or programmatic messages to a Discord channel using a bot token and a target channel ID. The project is deliberately minimal so you can adapt it to your needs (scheduling, reading from files, integrating with other services, etc.).

## Features

- Post messages to a Discord channel using a bot token
- Easy to configure via environment variables
- Minimal, easy-to-extend single-file implementation

## Requirements

- Python 3.8+
- A Discord bot (application) with a bot token and permission to send messages in the target channel

Optional (if you plan to extend):

- `discord.py` (if `bot.py` uses it) or the requests library for raw HTTP interactions

Note: This README assumes `bot.py` is a small script that posts messages. If your implementation uses a specific library (for example `discord.py` or `nextcord`), make sure to install that library and refer to its docs.

## Installation

1. Clone or copy this repository to your machine.
2. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies (if any). If your `bot.py` uses `discord.py`, install it:

```powershell
pip install -U discord.py
```

Alternatively, add any required packages to a `requirements.txt` and run:

```powershell
pip install -r requirements.txt
```

## Configuration

The script expects configuration via environment variables. At minimum you will need:

- `DISCORD_BOT_TOKEN` — your bot token (from the Discord Developer Portal)
- `DISCORD_CHANNEL_ID` — numeric ID of the target channel where messages will be posted

Set them in PowerShell like this:

```powershell
$env:DISCORD_BOT_TOKEN = "your_bot_token_here"
$env:DISCORD_CHANNEL_ID = "123456789012345678"
```

Or create a `.env` file and use a loader (for example `python-dotenv`) in `bot.py`.

## Usage

Run the script from the repository root:

```powershell
python bot.py
```

If `bot.py` expects command-line arguments or reads from a file, pass them as required. Example usage patterns you might add:

- Post a single message provided as an argument
- Watch a folder and post new file contents
- Schedule recurring posts using `schedule` or `APScheduler` libraries

## Example (HTTP POST using Discord API)

If `bot.py` uses direct HTTP requests, a simple example to send a message would look like this (pseudo-code):

```python
import os
import requests

token = os.getenv('DISCORD_BOT_TOKEN')
channel = os.getenv('DISCORD_CHANNEL_ID')
url = f'https://discord.com/api/v10/channels/{channel}/messages'
headers = {'Authorization': f'Bot {token}', 'Content-Type': 'application/json'}
payload = {'content': 'Hello from auto_discord_poster!'}
requests.post(url, json=payload, headers=headers)
```

If you use `discord.py`, the equivalent will use the library's Client/Bot methods.

## Troubleshooting

- 401 Unauthorized: check that `DISCORD_BOT_TOKEN` is correct and the bot has not been revoked.
- 403 Forbidden: ensure the bot has permission to send messages in the target channel and that the channel ID is correct.
- Invalid channel ID: ensure the channel ID is the numeric snowflake (not the channel name).
- Rate limits: respect Discord rate limits; if sending many messages, implement retry/backoff.

## Security

- Never commit your bot token to version control. Use environment variables or a secrets manager.
- Consider using a more restricted bot token and invite the bot with only the permissions it needs.

## Extending

- Add scheduling (cron, APScheduler) to post at intervals
- Read messages to post from a file, database, or remote API
- Add logging and error handling, and implement retries on failures

## License

Add a license file if you want to open-source the project (for example MIT). Without a license, the project is "All rights reserved" by default.

## Contact

If you want help extending this script (scheduling, using `discord.py`, or Dockerizing the bot), open an issue or ask for help.

---

Small README written to help you run and extend `bot.py`. If you want, I can:

- Inspect `bot.py` and add a tailored README with exact dependencies and usage examples
- Add a `requirements.txt` and a `.env.example` file
- Implement a simple `bot.py` example using `discord.py`

Tell me which of the above you'd like next.

