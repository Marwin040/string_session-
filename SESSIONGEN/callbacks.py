# Channel : https://t.me/ruangzeeb

import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from SESSIONGEN.generate import generate_session, ask_ques, buttons_ques

ERROR_MESSAGE = """𝐼𝒻 𝓎𝑜𝓊 𝑔𝑒𝓉 𝒶𝓃 𝑒𝓇𝓇𝑜𝓇 !
𝒴𝑜𝓊 𝒽𝒶𝓋𝑒 𝓂𝒶𝒹𝑒 𝓈𝑜𝓂𝑒 𝓂𝒾𝓈𝓉𝒶𝓀𝑒𝓈 𝓌𝒽𝒾𝓁𝑒 𝒸𝓇𝑒𝒶𝓉𝒾𝓃𝑔. 
𝑅𝑒𝓂𝑒𝓂𝒷𝑒𝓇𝒾𝓃𝑔 𝓌𝓇𝑜𝓃𝑔 𝒹𝒶𝓉𝒶 𝒻𝓇𝑜𝓂 𝑜𝓉𝒽𝑒𝓇𝓈. 
𝒯𝓇𝓎 𝒶𝑔𝒶𝒾𝓃 𝒾𝒻 𝓎𝑜𝓊 𝒸𝒶𝓃. 
𝒪𝓇 𝒾𝒻 𝓎𝑜𝓊 𝒽𝒶𝓋𝑒 𝒻𝒾𝓁𝓁𝑒𝒹 𝑒𝓋𝑒𝓇𝓎𝓉𝒽𝒾𝓃𝑔 𝒸𝑜𝓇𝓇𝑒𝒸𝓉𝓁𝓎 𝒷𝓊𝓉 𝑔𝑒𝓉 𝒶𝓃 𝑒𝓇𝓇𝑜𝓇, 
𝒯𝒽𝑒𝓃 𝒻𝑜𝓇𝓌𝒶𝓇𝒹 𝓉𝒽𝑒 𝑒𝓇𝓇𝑜𝓇 𝓂𝑒𝓈𝓈𝒶𝑔𝑒 𝓉𝑜 [ZeebFly](https://t.me/zeebdisini) !"""

@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    try:
        if query == "generate":
            await callback_query.answer()
            await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
        elif query == "pyrogram":
            await callback_query.answer()
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
