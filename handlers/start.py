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
ᴛʜɪs ɪs [{bn}](t.me/{bu}) 's, ᴍᴜsɪᴄ ᴍᴏᴅᴜʟᴇ....ᴇɴᴊᴏʏ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴏɴ ᴠᴄs....

Pᴏᴡᴇʀᴇᴅ ʙʏ : [ʜɪɴᴀᴛᴀ](t.me/hinataxrobot)
Usᴇ /mhelp ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴋɪʜᴀʙᴀʀᴀ", url=f"https://t.me/AkihabaraOfficial"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "Hɪɴᴀᴛᴀ", url=f"https://t.me/hinataxrobot"
                    ),
                    InlineKeyboardButton(
                        "Mɪᴋᴇʏ", url=f"https://t.me/devilxghoul"
                    )
                ],[
                    InlineKeyboardButton(
                        "Iɴʟɪɴᴇ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ", url="https://github.com/baby-kun"
                    )]
            ]
       ),
    )
