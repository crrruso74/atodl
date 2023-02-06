import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", 24281454))
API_HASH = environ.get("API_HASH", "dbe4521b4291da85becb65c7d4d4c36c")
BOT_TOKEN = environ.get("BOT_TOKEN", "5870947316:AAFiAwbi-cEGelZ5Mac6ovgg76mBD_XZoMI")
SESSION = environ.get("SESSION", "BQApuWwJxNsN9lwA_5UYTSyU-ujcoGQY5ethBnTaJoc7EULiur_7j4pICvCL3z5SrmcOkOK3bbwArZGfCEQ3neWEYl82ExwABRW7rGWrv1YWiKMCVhwsGHAKDmQT1uBW31ZTdwo3_TORjY2GAbtyOJT3aTAkhLYdoeFaJkHit3X2L0NrMnq5sy4JoasVN3_1mifZHbp0e0mBfueQ_QateYHJ9nf37sSaScafVpH2oz7GoYYlVSmjpegaX7vSlKBfCvcd0TXL40hfUlzcNXbgOiB6RE4_1zOgx4X0UwtjqVMiYVJ3A2SOoRi7KMtOaspQVci26hXYafvY_kqIAeCt19wKAAAAAV-wO78A")
TIME = int(environ.get("TIME", 250))
GROUPS = []
for grp in environ.get("GROUPS", "-1001489648140 -1001638282030 -1001645982114").split():
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
