from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome 👋\n"
        "Main aapka Daily Order Boost Planner hoon.\n\n"
        "Aaj ka plan paane ke liye /plan type karo."
    )

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Step 1️⃣: Aaj ka goal select karo:\n\n"
        "1. Slow day boost\n"
        "2. Weekend maximize\n"
        "3. Low orders recovery\n"
        "4. Rainy day\n\n"
        "Reply with number (1-4)"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("plan", plan))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
