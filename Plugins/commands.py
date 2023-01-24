import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation
import random

################################################################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply_photo(
        photo=random.choice(Config.PICS),
        caption=Translation.START,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# help command

@channelforward.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text=Translation.HELP,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
