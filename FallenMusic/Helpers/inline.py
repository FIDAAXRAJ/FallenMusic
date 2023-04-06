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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)
buttons = InlineKeyboardMarkup(
    [
      [           
InlineKeyboardButton(text="🚩resume🚩", callback_data="resume_cb"), InlineKeyboardButton(text="🚩pause🚩", callback_data="pause_cb"),
           
InlineKeyboardButton(text="🚩skip", callback_data="skip_cb"), InlineKeyboardButton(text="🚩end🚩", callback_data="end_cb"),
            
InlineKeyboardButton(text="🚩end🚩", callback_data="end_cb"), 
        ]
       ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="🚩 ᴄʜᴀɴɴᴇʟ 🚩", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🚩 sᴜᴩᴩᴏʀᴛ 🚩", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🚩 sᴏᴜʀᴄᴇ 🚩", url="https://telegra.ph/file/63111a1dff1ef295f3d84.jpg"
        ),
        InlineKeyboardButton(text="🚩 ᴘᴏɪsᴏɴ 🚩 ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🚩 ᴄʜᴀɴɴᴇʟ 🚩", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🚩 sᴜᴩᴩᴏʀᴛ 🚩", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🚩 sᴏᴜʀᴄᴇ 🚩", url="https://I_LOVE_YOU_PAGAL"
        ),
        InlineKeyboardButton(text="🚩 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🚩", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="sᴜᴅᴏ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_home"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="🚩 sᴜᴩᴩᴏʀᴛ 🚩", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_help"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]
