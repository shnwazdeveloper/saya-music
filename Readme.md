# Saya Music

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" />
</p>

<h3 align="center">Telegram Voice Chat Music Bot</h3>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00BFFF&width=680&lines=Saya+Music+-+Fast+and+Clean+Telegram+Music+Bot;Built+with+Pyrogram+%2B+PyTgCalls+for+Group+Voice+Chats" />
</p>

<p align="center">
  <a href="https://github.com/shnwazdeveloper/saya-music">
    <img src="https://raw.githubusercontent.com/shnwazdeveloper/saya-music/Master/SayaMusic/assets/saya/saya.jpg" width="720" alt="Saya Music Banner" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/shnwazdeveloper/saya-music/stargazers"><img src="https://img.shields.io/github/stars/shnwazdeveloper/saya-music?style=flat-square" /></a>
  <a href="https://github.com/shnwazdeveloper/saya-music/network/members"><img src="https://img.shields.io/github/forks/shnwazdeveloper/saya-music?style=flat-square" /></a>
  <a href="https://github.com/shnwazdeveloper/saya-music/issues"><img src="https://img.shields.io/github/issues/shnwazdeveloper/saya-music?style=flat-square" /></a>
  <a href="https://github.com/shnwazdeveloper/saya-music/commits/Master"><img src="https://img.shields.io/github/last-commit/shnwazdeveloper/saya-music?style=flat-square" /></a>
</p>

<p align="center">
  <a href="https://github.com/shnwazdeveloper/saya-music">Repository</a> |
  <a href="https://github.com/shnwazdeveloper/saya-music/issues">Support</a>
</p>

## About

Saya Music is a Telegram group voice chat bot focused on stable playback and easy deployment.
It uses Python with Pyrogram/Kurigram, PyTgCalls, MongoDB, yt-dlp, and FFmpeg.

The project is ready for Railway with `Dockerfile`, `Procfile`, and `railway.json`.

## Feature Set

| Module | Details |
| --- | --- |
| Music Playback | Audio/video streaming in Telegram voice chats |
| Sources | YouTube, Spotify, Apple Music, SoundCloud, Resso, Telegram files, live links |
| Queue Controls | Queue, pause, resume, skip, stop, seek, loop, shuffle, speed |
| Group Tools | Admin and utility commands |
| Persistence | MongoDB for settings, queue state, and user data |
| Deployment | Docker + Railway compatible |

## Required Environment Variables

```env
API_ID=
API_HASH=
BOT_TOKEN=
OWNER_ID=
LOGGER_ID=
STRING_SESSION=
MONGO_DB_URI=
COOKIE_URL=https://pastebin.com/YfK14h8y
```

Optional:

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

Do not commit real tokens, sessions, cookies, or database URIs.

## Key Sources

- `API_ID` and `API_HASH`: [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN`: [@BotFather](https://t.me/BotFather)
- `STRING_SESSION`: generate a Pyrogram/Kurigram session string for assistant account
- `LOGGER_ID`: private channel/group ID for logs (bot should be admin there)
- `MONGO_DB_URI`: [MongoDB Atlas](https://www.mongodb.com/atlas/database) or other MongoDB host
- `COOKIE_URL`: unlisted raw URL of Netscape `cookies.txt` (Pastebin/Batbin supported)

## Deploy on Railway

1. Push this repository to your GitHub account.
2. Create a new Railway project from this repo.
3. Add all required environment variables.
4. Deploy.

Runtime command:

```bash
python -m SayaMusic
```

This is a worker service and does not require a public web port.

## VPS Setup

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

## Docker Setup

```bash
cp sample.env .env
docker build -t saya-music .
docker run -d --name saya-music --env-file .env --restart unless-stopped saya-music
```

## Credits

- Base ecosystem inspired by open Telegram music bot projects
- Maintained by [shnwazdeveloper](https://github.com/shnwazdeveloper)

## License

MIT License
