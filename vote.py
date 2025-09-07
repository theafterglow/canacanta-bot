# vote.py
from hydrogram import types
from database import data, save_data
from config import CONFIG

vote_buttons = [types.InlineKeyboardButton(str(x), callback_data=str(x)) for x in [1,2,3,4,5,6,7,8,10,12]]
vote_index = 0
vote_started = False

async def start_voting(bot):
    global vote_started, vote_index
    vote_started = True
    vote_index = 0
    await send_next_vote(bot)

async def send_next_vote(bot):
    global vote_index
    if vote_index >= len(data["vote_order"]):
        await notify_non_voters(bot)
        await bot.send_message(CONFIG["collector_id"], "Tüm oylamalar tamamlandı!")
        return

    country = data["vote_order"][vote_index]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*vote_buttons)

    for user_id in data["users"]:
        if data["users"][user_id].get("country") != country:
            await bot.send_message(int(user_id), f"{country} ülkesini puanlayın:", reply_markup=keyboard)
    vote_index += 1

async def handle_vote(bot, callback_query):
    voter_id = str(callback_query.from_user.id)
    points = int(callback_query.data)
    country_to_vote = data["vote_order"][vote_index-1]

    data["votes"].setdefault(country_to_vote, {})[voter_id] = points
    data["users"][voter_id]["has_voted"] = True
    save_data()
    await callback_query.answer(f"{country_to_vote} için {points} puan verdiniz!")

async def notify_non_voters(bot):
    non_voters = []
    for user_id, info in data["users"].items():
        if not info.get("has_voted"):
            non_voters.append(f"{info.get('country','Bilinmeyen')} ({user_id})")
    if non_voters:
        msg = "Oy vermeyen kullanıcılar:\n" + "\n".join(non_voters)
        await bot.send_message(CONFIG["collector_id"], msg)