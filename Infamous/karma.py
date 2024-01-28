# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/86d8eddb9264ed67505b0.jpg",
    "https://te.legra.ph/file/49059d553efa874c70cb3.jpg",
    "https://telegra.ph/file/86d8eddb9264ed67505b0.jpg",
    "https://te.legra.ph/file/49059d553efa874c70cb3.jpg",
    "https://telegra.ph/file/86d8eddb9264ed67505b0.jpg",
    "https://telegra.ph/file/86d8eddb9264ed67505b0.jpg",
    "https://te.legra.ph/file/49059d553efa874c70cb3.jpg",
]

HEY_IMG = "https://te.legra.ph/file/49059d553efa874c70cb3.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = """👻𝐇ᴇʏ ๏ 𝐈 𝐒ǫᴜᴀʀᴇ 𝐘ꪮᴜʀ 𝐆ʀꪮᴜᴘ 𝐓ʜᴇ 𝐌ꪮsᴛ 𝐏ꪮᴡᴇʀғᴜʟ 𝐌ᴀɴɢɴᴇɴᴛ 🦋
𝐀ι 𝐎ʀ 𝐌ᴏʀᴇ 𝐀ᴡᴇsꪮᴍᴇ 𝐅ᴇᴀᴛᴜʀᴇ. 𝐕ɪsɪᴛ 𝐓ʜᴀɴᴋs 𝐅ꪮʀ 𝐔sɪɴɢ ❤️
🥀𝐀ɴʏ 𝐇ᴇʟᴘ [⎯꯭‌🇨🇦꯭꯭ ⃪Вα꯭∂ ꯭мυη∂α_꯭آآ꯭꯭꯭꯭⎯꯭ ꯭‌🌸](https://t.me/II_BAD_MUNDA_II)💞."""


START_BTN = [
    [
        InlineKeyboardButton(
            text="─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐇𝐄𝐋𝐏 ✯", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐃𝐄𝐓𝐀𝐈𝐋𝐒 ✯", callback_data="Miko_"),
        InlineKeyboardButton(text="✯ 𝐀𝐈 ✯", callback_data="ai_handler"),
        InlineKeyboardButton(text="✯ 𝐒𝐎𝐔𝐑𝐑𝐂𝐄 ✯", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐎𝐖𝐍𝐄𝐑 ✯", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/ABOUT_SHIVANSHOP"),
        ib(text="SUPPORT", url="https://t.me/mastiwithfriendsx"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *˹ 𝗦𝙴𝙽𝙾𝚁𝙸𝚃𝙰 ✘ 𝗥𝙾𝙱𝙾 ˼* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
