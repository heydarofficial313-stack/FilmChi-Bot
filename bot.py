import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🔎 جستجوی فیلم", callback_data="search"),
            InlineKeyboardButton("🎬 جدیدترین‌ها", callback_data="new"),
        ],
        [
            InlineKeyboardButton("🔥 محبوب‌ترین‌ها", callback_data="popular"),
            InlineKeyboardButton("🎭 ژانرها", callback_data="genres"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 به FilmChi خوش آمدید!\n\n"
        "🍿 دنیای فیلم‌های سینمایی همین‌جاست.\n"
        "🎙️ دوبله و زیرنویس فارسی\n"
        "⭐ کیفیت بالا\n\n"
        "یکی از گزینه‌های زیر رو انتخاب کن:",
        reply_markup=reply_markup
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
