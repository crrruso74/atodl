import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", 24281454))
API_HASH = environ.get("API_HASH", "dbe4521b4291da85becb65c7d4d4c36c")
BOT_TOKEN = environ.get("BOT_TOKEN", "5460795442:AAGn6kth_XPCMO1KIOpB8-odZX_h21Ujl1g")
SESSION = environ.get("SESSION", "AQADj04oubY81Vz_FviOhDCZTJQeNeE0mAyVSGQGudDuY5ztF-vQzipdTYuDzz44oasUGJx302iZMi-gDxnFJHG-ukiLW_CT91Iceo9bh3VjFwZ3vsyxt2CuE1f9s-hCwyw5cXyqDRj1OtafeRSLE9TKxiDWhpuAeUqtkQ6q_KxJJyOKVJaOFmgKq7E9ve9tfZUTGGndsCQ8MDS5uyZ5_lf4w2ERnXR5TQV5Vw_EhvN0WEyaNdHmB0Lp9n-EgplmiC8rTOZZ_Nwnf8W7B4q9knHGd7fL5bY7py3HiQShrQ8GY2YaJPJvWcHFYieRpJxG5sdRzkpXRB3YflgfUhbCIFg3AAAAAVcsK8MA")
TIME = int(environ.get("TIME", 3))
GROUPS = []
for grp in environ.get("GROUPS", "-1001652878224 -1001762138428").split():
    GROUPS.append(int(grp))
ADMINS = [5650200786]
for usr in environ.get("ADMINS", "1119774110").split():
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
