from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔴 Yahan apna Telegram Bot Token paste karo
BOT_TOKEN = "8322059364:AAGKMp1Kzm4A1x5xA-izrgHuo-gg43Rbd5g
"

# User state store karne ke liye
user_state = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Namaskar 👋\n"
        "Mi tumcha Daily Order Boost Planner aahe.\n\n"
        "Aajcha plan milavayla /plan type kara."
    )

# /plan command
async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_state[update.effective_user.id] = {"step": 1}

    await update.message.reply_text(
        "Step 1️⃣: Aajcha goal select kara:\n\n"
        "1. Aaj slow day aahe (orders kami aahet)\n"
        "2. Weekend sales maximize karaycha aahe\n"
        "3. Orders recovery karaychi aahe\n"
        "4. Rainy day special plan\n\n"
        "Number reply kara (1-4)"
    )

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if user_id not in user_state:
        await update.message.reply_text("Please /start or /plan type kara 🙂")
        return

    step = user_state[user_id].get("step")

    # Step 1: Goal
    if step == 1:
        if text not in ["1", "2", "3", "4"]:
            await update.message.reply_text("Kripya 1 te 4 madhla number select kara.")
            return

        goals = {
            "1": "Slow day boost",
            "2": "Weekend maximize",
            "3": "Low orders recovery",
            "4": "Rainy day special"
        }

        user_state[user_id]["goal"] = goals[text]
        user_state[user_id]["step"] = 2

        await update.message.reply_text(
            "Step 2️⃣: Tumcha restaurant type select kara:\n\n"
            "1. Cafe\n"
            "2. Family Restaurant\n"
            "3. Cloud Kitchen\n\n"
            "Number reply kara (1-3)"
        )

    # Step 2: Restaurant type
    elif step == 2:
        if text not in ["1", "2", "3"]:
            await update.message.reply_text("Kripya 1 te 3 madhla number select kara.")
            return

        types = {
            "1": "Cafe",
            "2": "Family Restaurant",
            "3": "Cloud Kitchen"
        }

        user_state[user_id]["type"] = types[text]
        user_state[user_id]["step"] = 3

        await update.message.reply_text(
            "Step 3️⃣: Aaj kay push karaycha?\n\n"
            "1. Bestseller item\n"
            "2. High-margin item (jasta profit)\n"
            "3. New item\n"
            "4. Slow-moving item\n"
            "5. Chef special\n\n"
            "Number reply kara (1-5)"
        )

    # Step 3: Menu focus
    elif step == 3:
        if text not in ["1", "2", "3", "4", "5"]:
            await update.message.reply_text("Kripya 1 te 5 madhla number select kara.")
            return

        focus_items = {
            "1": "Bestseller item",
            "2": "High-margin item",
            "3": "New item",
            "4": "Slow-moving item",
            "5": "Chef special"
        }

        focus = focus_items[text]
        goal = user_state[user_id]["goal"]
        rtype = user_state[user_id]["type"]

        # Simple strategy logic
        strategy = "Bestseller + small freebie / light offer"
        message = "Aaj special offer! Limited time sathi available. Ata order kara 🍕🔥"

        reply = (
            "✅ Aajcha Plan Ready aahe!\n\n"
            f"🎯 Goal: {goal}\n"
            f"🏪 Restaurant Type: {rtype}\n"
            f"🍽️ Focus Item: {focus}\n\n"
            f"📢 Strategy: {strategy}\n"
            f"📝 Promo Message:\n\"{message}\"\n\n"
            "📍 Use kara: Zomato, Swiggy, WhatsApp\n\n"
            "Parat navin plan sathi /plan type kara 😄"
        )

        await update.message.reply_text(reply)

        # Reset user state
        user_state.pop(user_id, None)

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("plan", plan))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
