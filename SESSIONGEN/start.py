# Channel : https//t.me/ruangzeeb

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""ʜᴀʟʟᴏ {msg.from_user.mention} 🌲,

🏓ᴛʜɪs ɪs {me} 
>ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ᴀʟʟ ᴛʏᴘᴇꜱ ᴏꜰ ꜱᴇꜱꜱɪᴏɴꜱ. 
>ʟᴀᴛᴇꜱᴛ ꜱᴇᴄᴜʀɪᴛʏ ᴘᴀᴛᴄʜᴇꜱ ᴀᴘᴘʟɪᴇᴅ ꜰᴏʀ ʏᴏᴜʀ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ.
>ᴛʀʏ ᴛʜɪꜱ ʙᴏᴛ ɴᴏᴡ!!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝒢𝑒𝓃𝑒𝓇𝒶𝓉 𝒮𝑒𝓈𝓈𝒾𝑜𝓃", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝒮𝓊𝓅𝓅𝑜𝓇𝓉", url="https://t.me/The_Architect04"),
                    InlineKeyboardButton("𝒞𝒽𝑒𝓃𝓃𝒶𝓁", url="https://t.me/The_Architect04")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
