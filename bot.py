# bot.py
import asyncio
from hydrobot import Client, filters
from config import CONFIG
from database import load_data, save_data
from register import register_country, register_song
from scheduler import set_time, wait_for_vote_time
from vote import start_voting, handle_vote
from results import show_results

load_data()

bot = Client("eurobot", api_id=CONFIG["api_id"], api_hash=CONFIG["api_hash"], bot_token=CONFIG["bot_token"])

# Komutlar
@bot.on_message(filters.command("start"))
async def cmd_start(client, message):
    await message.reply("Hoşgeldiniz! Önce ülkenizi seçin: /country veya şarkınızı ekleyin: /song")

@bot.on_message(filters.command("country"))
async def cmd_country(client, message):
    await register_country(bot, message)

@bot.on_message(filters.command("song"))
async def cmd_song(client, message):
    await register_song(bot, message)

@bot.on_message(filters.command("settime"))
async def cmd_settime(client, message):
    await set_time(bot, message)

@bot.on_message(filters.command("results"))
async def cmd_results(client, message):
    await show_results(bot, message)

# Callback query (inline tuş)
@bot.on_callback_query()
async def cb_query(client, callback_query):
    await handle_vote(bot, callback_query)

# Zamanlayıcı başlat
async def scheduler():
    await wait_for_vote_time(bot, start_voting)

async def main():
    asyncio.create_task(scheduler())
    await bot.start()
    print("Bot çalışıyor...")
    await bot.idle()

if __name__ == "__main__":
    asyncio.run(main())
