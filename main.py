import random
from telegram import Update, ChatMember
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
YOUR_USER_ID = 7920993084
TOKEN = "7497708488:AAH63mRkOzkoZbrBqSjrOI8cMVVrKKfqe9A"

# وضعیت فعال یا غیر فعال بودن ربات در هر گروه
group_states = {}

async def is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.effective_user.id
    if user_id == YOUR_USER_ID:
        return True  # اگه خودتی، اجازه بده
    member = await context.bot.get_chat_member(update.effective_chat.id, user_id)
    return member.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]


async def toggle_ahh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_admin(update, context):
        await update.message.reply_text("فقط ادمین‌ها می‌تونن این دستور رو بزنن.")
        return

    if context.args and context.args[0].lower() == "on":
        group_states[update.effective_chat.id] = True
        await update.message.reply_text("ربات فعال شد. از این به بعد هر پیامی بیاد جواب می‌دم.")
    elif context.args and context.args[0].lower() == "off":
        group_states[update.effective_chat.id] = False
        await update.message.reply_text("ربات غیر فعال شد. دیگه جواب نمی‌دم.")
    else:
        await update.message.reply_text("دستور نامعتبره. از /ahh on یا /ahh off استفاده کن.")

async def reply_to_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if group_states.get(chat_id, False):  # اگر فعال بود
        h_count = random.randint(1, 7)
        message = "عا" + "ح" * h_count
        if random.choice([True, False]):
            message += " 💦"
        await update.message.reply_text(message, reply_to_message_id=update.message.message_id)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # پاسخ دادن به پیام‌های متنی (وقتی ربات فعاله)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_to_messages))

    # دستور /ahh on و /ahh off
    app.add_handler(CommandHandler("ahh", toggle_ahh))

    app.run_polling()