import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", 24281454))
API_HASH = environ.get("API_HASH", "dbe4521b4291da85becb65c7d4d4c36c")
BOT_TOKEN = environ.get("BOT_TOKEN", "5801828691:AAFNuWAz1nL3I8qherfvf3knLioKrVSF7EA")
SESSION = environ.get("SESSION", "AQBiMZkAF_UXN9tmXvtZkfSpSo518pKVvK6QCb061ZFplG8B3EZwimCEwcu7PFvyhwxBX7fkqlAJiBXp8GVA-1JbU0lyd1SEdvIO5W6TDqOcxl-KmQaOSOqne_P0NCcgDk4NGw7YS90G70KHRWBySic6Wr_tIee5Xo0kVp1d1KXvg8DpnIWzUNGwCBrdN7mBFSkhQu4_Te9goORVL4zvoynCxOV-nsHWZJnkajDkRS6pTDbdp8o33AN6uCMMDtZLxvYF7mVFja5A6vAJOKOlXwi79w0Q2QNfLNeHLUns8HrSo86BPMlUSELcpqfIBgg-6VmRLVkE1LO74ubnKwJ0V_oPydfnRgAAAAFUqxlhAA")
TIME = int(environ.get("TIME", 10))
GROUPS = []
for grp in environ.get("GROUPS", "-1001638282030").split():
    GROUPS.append(int(grp))
ADMINS = [5650200786]
for usr in environ.get("ADMINS", "5650200786").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
