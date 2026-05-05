# Saya Music

Saya Music is a Telegram group voice-chat music bot built with Python, Kurigram/Pyrogram, PyTgCalls, MongoDB, yt-dlp, and FFmpeg.

It is prepared for Railway deployment with a Dockerfile, Procfile, and `railway.json`.

## Features

- Music and video playback in Telegram group voice chats
- YouTube, Spotify, Apple Music, SoundCloud, Resso, Telegram, and live stream support
- Queue, pause, resume, skip, seek, loop, shuffle, and speed controls
- Group management helpers and utility commands
- MongoDB-backed settings, queues, sudo users, and bot state
- Docker/Railway ready runtime

## Required Environment Variables

Set these variables in Railway before deploying:

```env
API_ID=
API_HASH=
BOT_TOKEN=
OWNER_ID=
LOGGER_ID=
STRING_SESSION=
MONGO_DB_URI=
COOKIE_URL=
```

Optional variables:

```env
BOT_USERNAME=SayaMusicBot
BOT_NAME=Saya Music
OWNER_USERNAME=shnwazdeveloper
SUPPORT_CHANNEL=https://github.com/shnwazdeveloper/saya-music
SUPPORT_CHAT=https://github.com/shnwazdeveloper/saya-music/issues
API_URL=
VIDEO_API_URL=
API_KEY=
DEEP_API=
UPSTREAM_REPO=https://github.com/shnwazdeveloper/saya-music
UPSTREAM_BRANCH=Master
AUTO_JOIN_GROUPS=
```

Never commit real bot tokens, session strings, MongoDB URIs, or cookies.

## Railway Deployment

1. Fork or push this repository to GitHub as `saya-music`.
2. Open Railway and create a new project from the GitHub repo.
3. Add the required environment variables in the Railway service.
4. Deploy.

Railway will read `railway.json`, build with the Dockerfile, and start the worker with:

```bash
python -m SayaMusic
```

This bot is a worker process, so it does not need a public HTTP port.

## Local Docker Run

```bash
cp sample.env .env
docker build -t saya-music .
docker run --env-file .env --restart unless-stopped saya-music
```

## VPS Run

```bash
git clone https://github.com/shnwazdeveloper/saya-music
cd saya-music
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
bash setup
bash start
```

## Getting Keys

- `API_ID` and `API_HASH`: https://my.telegram.org
- `BOT_TOKEN`: https://t.me/BotFather
- `STRING_SESSION`: generate a Pyrogram/Kurigram session string for the assistant account
- `LOGGER_ID`: private group/channel ID where the bot can send logs; add the bot as admin
- `MONGO_DB_URI`: MongoDB Atlas or another MongoDB connection string
- `COOKIE_URL`: raw URL to a Netscape-format YouTube `cookies.txt`

## Repository

GitHub: https://github.com/shnwazdeveloper/saya-music

## License

Released under the MIT License.
