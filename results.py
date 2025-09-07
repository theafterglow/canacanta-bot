# results.py
from database import data

async def show_results(bot, message):
    scores = {}
    for country, votes in data["votes"].items():
        scores[country] = sum(votes.values())
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    result_text = "🏆 SONUÇLAR 🏆\n\n"
    for country, score in sorted_scores:
        result_text += f"{country}: {score} puan\n"
    
    await message.reply(result_text)
