from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم تفعيل البوت")
if name == "main":
    app = ApplicationBuilder().token("8511971624:AAEFzPUcM4hepdScn4KPuWcjw0zvM8iESAM").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
