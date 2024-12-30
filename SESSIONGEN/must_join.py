from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://envs.sh/5gF.jpg", caption=f"» 𝒯𝑜 𝓊𝓈𝑒 𝓉𝒽𝒾𝓈 𝒷𝑜𝓉, 𝓎𝑜𝓊 𝓂𝓊𝓈𝓉 [𝒿𝑜𝒾𝓃]({link}) 𝒻𝒾𝓇𝓈𝓉 𝑔𝑜 𝓉𝑜 𝓈𝓊𝓅𝓅𝑜𝓇𝓉 𝒸𝒽𝒶𝓉, 𝒾𝒻 𝒶𝓁𝓇𝑒𝒶𝒹𝓎 𝒸𝓁𝒾𝒸𝓀𝑒𝒹 /start 𝓇𝑒𝓉𝓊𝓇𝓃!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝒥𝑜𝒾𝓃 𝒩𝑜𝓌", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"𝒟𝑜𝓃'𝓉 𝓂𝒾𝓈𝓈 𝑜𝓊𝓉—𝒸𝑜𝓂𝑒 𝒿𝑜𝒾𝓃 𝓊𝓈 𝑜𝓃 𝓉𝒽𝑒 𝒸𝒽𝒶𝓃𝓃𝑒𝓁!")
