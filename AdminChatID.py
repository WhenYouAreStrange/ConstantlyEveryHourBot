import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Включение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Ваш chat_id: {chat_id}")

def main() -> None:
    # Создаем экземпляр ApplicationBuilder и передаем ему токен вашего бота
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Регистрируем обработчик команды /get_chat_id
    application.add_handler(CommandHandler("get_chat_id", get_chat_id))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()