# Saya Music
from pyrogram.types import InlineKeyboardButton

import config
from SayaMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add To Group", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add To Group",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="Owner", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="Commands", callback_data="open_help"),
        ],
    ]
    return buttons
