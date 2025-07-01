import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# In-memory store for demo—swap for a real DB later
user_prefs = {}

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is live! Use /set_amount to configure.")

async def set_amount(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(ctx.args[0])
    except (IndexError, ValueError):
        return await update.message.reply_text("Usage: /set_amount 2.5")
    uid = update.effective_user.id
    user_prefs.setdefault(uid, {})['amount'] = amount
    await update.message.reply_text(f"✅ Trade amount set to ${amount}")

if __name__ == "__main__":
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("set_amount", set_amount))
    app.run_polling()
