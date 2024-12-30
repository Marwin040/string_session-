# Channel : https//t.me/ruangzeeb

from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**𝒮𝑒𝓁𝑒𝒸𝓉 𝓉𝒽𝑒 𝑜𝓃𝑒 𝓎𝑜𝓊 𝓌𝒶𝓃𝓉 𝓉𝑜 𝒸𝓇𝑒𝒶𝓉𝑒 𝒶 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒻𝑜𝓇.**"
buttons_ques = [
    [
        InlineKeyboardButton("𝓅𝓎𝓇𝑜𝑔𝓇𝒶𝓂𝒱2 📚", callback_data="pyrogram"),
        InlineKeyboardButton("𝓉𝑒𝓁𝑒𝓉𝒽𝑜𝓃 💻", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝒫𝓎𝓇𝑜𝑔𝓇𝒶𝓂 𝐵𝑜𝓉 🤖", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝒯𝑒𝓁𝑒𝓉𝒽𝑜𝓃 𝐵𝑜𝓉 🤖", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="🔥 𝒢𝑒𝓃𝑒𝓇𝒶𝓉𝑒 𝒮𝑒𝓈𝓈𝒾𝑜𝓃𝓈 🔥", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭"
    else:
        ty = "𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬"
        if not old_pyro:
            ty += " 𝖵2"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"» 𝒮𝓉𝒶𝓇𝓉𝒾𝓃𝑔 **{ty}** 𝒮𝑒𝓈𝓈𝒾𝑜𝓃 𝒢𝑒𝓃𝓇𝒶𝓉𝑜𝓇...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝒢𝒾𝓋𝑒**API_ID** anda.\n\n𝐼𝒻 𝓎𝑜𝓊 𝒹𝑜𝓃'𝓉 𝒽𝒶𝓋𝑒 **API_ID** 𝒸𝓁𝒾𝒸𝓀 /skip 𝓉𝑜 𝒸𝑜𝓃𝓉𝒾𝓃𝓊𝑒.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝖠𝖯𝖨_𝖨𝖣** 𝒻𝒶𝒾𝓁𝑒𝒹 𝓉𝑜 𝓁𝑜𝒶𝒹, 𝓅𝓁𝑒𝒶𝓈𝑒 /start 𝓇𝑒𝓉𝓊𝓇𝓃.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "<i>𝒩𝑒𝓍𝓉 𝑔𝒾𝓋𝑒 **API_HASH** 𝓎𝑜𝓊 𝓉𝑜 𝒸𝑜𝓃𝓉𝒾𝓃𝓊𝑒.</i>", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "<i>𝒫𝓁𝑒𝒶𝓈𝑒 𝓅𝓇𝑜𝓋𝒾𝒹𝑒 𝓎𝑜𝓊𝓇 𝒶𝒸𝒸𝑜𝓊𝓃𝓉 𝓅𝒽𝑜𝓃𝑒 𝓃𝓊𝓂𝒷𝑒𝓇.__\n𝐸𝓍𝒶𝓂𝓅𝓁𝑒 :</i> `+62 95xxxxxxXX`'"
    else:
        t = "<i>𝒢𝒾𝓋𝑒**Bot_Token** 𝓉𝑜 𝒸𝑜𝓃𝓉𝒾𝓃𝓊𝑒.\n𝐸𝓍𝒶𝓂𝓅𝓁𝑒  :</i> `6810174902:AAGQVElsBPTNe6Rj16miPbCrDGikscfarYY`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("<i>» 𝒮𝑒𝓃𝒹𝒾𝓃𝑔 𝒪𝒯𝒫 𝒸𝑜𝒹𝑒...</i>")
    else:
        await msg.reply("<i>» 𝒯𝓇𝓎𝒾𝓃𝑔 𝓉𝑜 𝓁𝑜𝑔𝒾𝓃 𝓋𝒾𝒶 𝒷𝑜𝓉 𝓉𝑜𝓀𝑒𝓃...</i>")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("**API_ID** 𝒜𝓃𝒹 **API_HASH** 𝒴𝑜𝓊𝓇 𝒸𝑜𝓂𝒷𝒾𝓃𝒶𝓉𝒾𝑜𝓃 𝒹𝑜𝑒𝓈 𝓃𝑜𝓉 𝓂𝒶𝓉𝒸𝒽 𝓉𝒽𝑒 𝓉𝑒𝓁𝑒𝑔𝓇𝒶𝓂 𝒶𝓅𝓅𝓁𝒾𝒸𝒶𝓉𝒾𝑜𝓃 𝓈𝓎𝓈𝓉𝑒𝓂. \n\nKlik /start 𝒯𝑜 𝓇𝑒𝓅𝑒𝒶𝓉.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("<i>**𝒫𝒽𝑜𝓃𝑒 𝓃𝓊𝓂𝒷𝑒𝓇** 𝓌𝒽𝒶𝓉 𝓌𝒶𝓈 𝓈𝑒𝓃𝓉 𝒾𝓈 𝓃𝑜𝓉 𝓎𝑜𝓊𝓇𝓈.\n\nKlik /start 𝒯𝑜 𝓇𝑒𝓅𝑒𝒶𝓉.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "<i>𝒫𝓁𝑒𝒶𝓈𝑒 𝒞𝒽𝑒𝒸𝓀 𝓉𝒽𝑒 𝒸𝑜𝒹𝑒 **OTP** 𝒻𝓇𝑜𝓂 𝑜𝒻𝒻𝒾𝒸𝒾𝒶𝓁 𝒯𝑒𝓁𝑒𝑔𝓇𝒶𝓂 𝒜𝒸𝒸𝑜𝓊𝓃𝓉.\n\n𝐼𝒻 OTP 𝒾𝓈 `12345`, **𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝑒𝓃𝒹 𝒾𝓃 𝓉𝒽𝑒 𝒻𝑜𝓇𝓂𝒶𝓉** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» 𝒯𝒽𝑒 𝓁𝒾𝓂𝒾𝓉 𝓇𝑒𝒶𝒸𝒽 𝑜𝒻 10 𝓂𝒾𝓃𝓊𝓉𝑒𝓈.\n\n𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝓉𝒶𝓇𝓉 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝓃𝑔 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒶𝑔𝒶𝒾𝓃 𝒷𝓎 𝓉𝒶𝓅𝓅𝒾𝓃𝑔.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» 𝒯𝒽𝑒 𝑜𝓉𝓅 𝓎𝑜𝓊'𝓋𝑒 𝓈𝑒𝓃𝒹 𝒾𝓈 **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ 𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝓉𝒶𝓇𝓉 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝓃𝑔 𝓎𝑜𝓊𝓇 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒶𝑔𝒶𝒾𝓃.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» 𝒯𝒽𝑒 𝑜𝓉𝓅 𝓎𝑜𝓊'𝓋𝑒 𝓈𝑒𝓃𝒹 𝒾𝓈 **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ 𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝓉𝒶𝓇𝓉 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝓃𝑔 𝓎𝑜𝓊𝓇 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒶𝑔𝒶𝒾𝓃.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» 𝒫𝓁𝑒𝒶𝓈𝑒 𝑒𝓃𝓉𝑒𝓇 𝓎𝑜𝓊𝓇 **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** 𝒫𝒶𝓈𝓈𝓌𝑜𝓇𝒹 𝓉𝑜 𝒸𝑜𝓃𝓉𝒾𝓃𝓊𝑒.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» 𝒯𝒾𝓂𝑒 𝓁𝒾𝓂𝒾𝓉 𝓇𝑒𝒶𝒸𝒽𝑒𝒹 𝑜𝒻 5 𝑀𝒾𝓃𝓊𝓉𝑒𝓈.\n\nᴩʟᴇᴀsᴇ 𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝓉𝒶𝓇𝓉 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝓃𝑔 𝓎𝑜𝓊𝓇 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒶𝑔𝒶𝒾𝓃.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» 𝒯𝒽𝑒 𝓅𝒶𝓈𝓈𝓌𝑜𝓇𝒹 𝓎𝑜𝓊'𝓋𝑒 𝓈𝑒𝓃𝒹 𝒾𝓈 𝓌𝓇𝑜𝓃𝑔.\n\n𝒫𝓁𝑒𝒶𝓈𝑒 𝓈𝓉𝒶𝓇𝓉 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝓃𝑔 𝓎𝑜𝓊𝓇 𝓈𝑒𝓈𝓈𝒾𝑜𝓃 𝒶𝑔𝒶𝒾𝓃.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**𝒯𝒽𝒾𝓈 𝒾𝓈 𝓎𝑜𝓊𝓇 {ty} 𝓈𝓉𝓇𝒾𝓃𝑔 𝓈𝑒𝓈𝓈𝒾𝑜𝓃** \n\n`{string_session}` \n\n**𝑀𝒶𝒹𝑒 𝒷𝓎:[𝒯𝒽𝑒 𝒜𝓇𝒸𝒽𝒾𝓉𝑒𝒸𝓉](https://t.me/The_Architect04) 𝒲𝒶𝓇𝓃𝒾𝓃𝑔 :** 𝒟𝑜𝓃'𝓉 𝓈𝒽𝒶𝓇𝑒 𝓌𝒾𝓉𝒽 𝒶𝓃𝓎𝑜𝓃𝑒 𝑒𝓋𝑒𝓃 𝒾𝒻  𝓌𝒾𝓉𝒽 𝓎𝑜𝓊𝓇 𝑔𝒻 🏴‍☠️"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "𝒮𝓊𝒸𝒸𝑒𝓈𝓈𝒻𝓊𝓁𝓁𝓎 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝑒𝒹 𝓎𝑜𝓊𝓇 {} 𝓈𝓉𝓇𝒾𝓃𝑔 𝓈𝑒𝓈𝓈𝒾𝑜𝓃.\n\n𝒫𝓁𝑒𝒶𝓈𝑒 𝒸𝒽𝑒𝒸𝓀 𝓎𝑜𝓊𝓇 𝓈𝒶𝓋𝑒𝒹 𝓂𝑒𝓈𝓈𝒶𝑔𝑒𝓈 𝒻𝑜𝓇 𝑔𝑒𝓉𝓉𝒾𝓃𝑔 𝒾𝓉.\n\nᴀ 𝒮𝓉𝓇𝒾𝓃𝑔 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝑜𝓇 𝒷𝑜𝓉 𝒷𝓎 [𝒯𝒽𝑒 𝒜𝓇𝒸𝒽𝒾𝓉𝑒𝒸𝓉](https://t.me/The_Architect04)".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» 𝒞𝒶𝓃𝒸𝑒𝓁𝓁𝑒𝒹 𝓉𝒽𝑒 𝑜𝓃𝑔𝑜𝒾𝓃𝑔 𝓈𝓉𝓇𝒾𝓃𝑔 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝑜𝓃 !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» 𝒮𝓊𝒸𝒸𝑒𝓈𝓈𝒻𝓊𝓁𝓁𝓎 𝑅𝑒𝓈𝓉𝒶𝓇𝓉𝑒𝒹 𝓉𝒽𝒾𝓈 𝒷𝑜𝓉 𝒻𝑜𝓇 𝓎𝑜𝓊 !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**»  𝒞𝒶𝓃𝒸𝑒𝓁𝓁𝑒𝒹 𝓉𝒽𝑒 𝑜𝓃𝑔𝑜𝒾𝓃𝑔 𝓈𝓉𝓇𝒾𝓃𝑔 𝑔𝑒𝓃𝑒𝓇𝒶𝓉𝒾𝑜𝓃 𝓅𝓇𝑜𝒸𝑒𝓈𝓈 !**", quote=True)
        return True
    else:
        return False
