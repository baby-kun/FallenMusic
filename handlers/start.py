import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("mstart") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
ʜᴇʏ {message.from_user.mention()} !
ᴛʜɪs ɪs [{bn}](t.me/{bu}), ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs...

Pᴏᴡᴇʀᴇᴅ ʙʏ : [ʜɪɴᴀᴛᴀ](t.me/{me})
Usᴇ /mhelp ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Music 1", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "Music 2", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        " Hinata ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        " Owner ", url="https://github.com/baby-kun"
                    )]
            ]
       ),
    )
