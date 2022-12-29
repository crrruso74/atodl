import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", 24281454))
API_HASH = environ.get("API_HASH", "dbe4521b4291da85becb65c7d4d4c36c")
BOT_TOKEN = environ.get("BOT_TOKEN", "5705014422:AAFv59v7I2eecaXFAt6QC9xj7H7ExXaqZ1Y")
SESSION = environ.get("SESSION", "AQBg8J78Cv2pW_0msTWUwS6NHAUc99vCeIg2XVN0eq3lHz37ckEXFk_h4Y7dVd4P2OyU5lAPK9PflUjjCGUSG9sstMO6LknFv19n6YaLBYwEhL9CMpUvPXXM0DXzhtlRccPV_CP4bRZoBbd6m9Hx7sV9clClKk_PHAgGNMIaQw1ASn7Z2PCsJTGY8rwusbBn7P3t--0-GGdtiRqmbR2A2DnpFoxF0av5ZJeN7X0nOHOEcV8D_Vg8HKhEUq-InL2D40Xra1aR7cHqPe3RxZTOofJafbbDZILFXXO6rRDaTZx3lpV2UbgbGBlT6Dnwsfxfmqy4atQjUAcLVQ2rPaWT3rPpAAAAAVSrGWEA")
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
