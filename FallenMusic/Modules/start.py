# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

@app.on_message(filters.command("start") & filters.private & ~filters.edited)
async def useradd(_, message: Message):
    await message.reply_photo(
        photo=f"https:https://te.legra.ph/file/f272a9daec063f74630f6.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🚩 ʜᴇʟʟᴏ, ɪ ᴀᴍ Pᴏɪsᴏɴ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ sᴏɴɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ › : [Pᴏɪsᴏɴ](https://t.me/I_LOVE_YOU_PAGAL)
┣★ ᴜᴘᴅᴀᴛᴇs › : [ʟᴏᴠᴇʀs ᴘᴏɪɴᴛ](https://t.me/LOVERS_POINTT)
┣★ sᴜᴘᴘᴏʀᴛ › : [Pᴏɪsᴏɴ ᴄʜᴀᴛ](https://t.me/Dangerous_fighter_clan)
┣★ Bʀᴀɴᴅᴇᴅ ᴘʜᴏᴛᴏs › : [ᴘʜᴏᴛᴏs](https://t.me/LOVERS_POINTT)
┣★ ʙʀᴏᴛʜᴇʀ › : [ᴍʏ ʙʀᴏ](https://t.me/B_R_A_N_D_E_D_K_I_N_G)
┣★ ʜᴇʟᴘ › : ɴᴇᴇᴅ ʜᴇʟᴘ ʀᴜɴ /help
┗━━━━━━━━━━━━━━━━━┛
🚩 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ 🚩[ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/I_LOVE_YOU_PAGAL) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ Fɪᴅᴀᴀ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕",
                        url=f"https://t.me/FIDAA_MUSIC_BOT?startgroup=true",
                    )
                ]
            ]
        ),
    )

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from FallenMusic import BOT_MENTION, BOT_NAME, app
from FallenMusic.Helpers import gp_buttons, pm_buttons
from FallenMusic.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def fallen_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🚩jai shree ram har har Mahadev 🚩")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **ᴛʀᴀᴄᴋ ɪɴғᴏʀɴᴀᴛɪᴏɴ** 

📌 **ᴛɪᴛʟᴇ :** {title}

⏳ **ᴅᴜʀᴀᴛɪᴏɴ :** {duration} ᴍɪɴᴜᴛᴇs
👀 **ᴠɪᴇᴡs :** `{views}`
⏰ **ᴩᴜʙʟɪsʜᴇᴅ ᴏɴ :** {published}
🔗 **ʟɪɴᴋ :** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})
🎥 **ᴄʜᴀɴɴᴇʟ :** [{channel}]({channellink})

💖 sᴇᴀʀᴄʜ ᴩᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link),
                            InlineKeyboardButton(
                                text="sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await message.reply_photo(
            photo=config.START_IMG,
            caption=START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
