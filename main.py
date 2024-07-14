import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import asyncio

# Включение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Глобальная переменная для отслеживания времени старта
start_time = None
# Разница во времени с сервером (в часах)
time_offset = datetime.timedelta(hours=3)
# ID администратора для отправки уведомлений
admin_chat_id = "ADMIN_CHAT_ID"
# Словарь для отслеживания состояния команды /start для каждого пользователя
users_started = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global start_time
    chat_id = update.message.chat_id

    if users_started.get(chat_id, False):
        await update.message.reply_text('Вы уже запускали команду /start. Бот уже работает.')
        return

    # Помечаем, что пользователь запустил команду /start
    users_started[chat_id] = True
    # Устанавливаем текущее время как время старта
    start_time = datetime.datetime.now()
    await update.message.reply_text('Бот запущен! Я буду отправлять сообщение каждые 60 минут.')

    # Функция для отправки сообщения каждые 60 минут
    async def send_message():
        try:
            while True:
                if start_time:
                    # Рассчитываем время работы бота
                    now = datetime.datetime.now()
                    delta = now - start_time
                    # Корректируем текущее время для отображения
                    now_with_offset = now + time_offset
                    # Формируем сообщение с текущим временем
                    message = f"Бот работает уже: {delta}. Время: {now_with_offset.strftime('%d.%m.%Y %H:%M:%S')}"
                    # Отправляем сообщение пользователю
                    await context.bot.send_message(chat_id=update.message.chat_id, text=message)
                # Ожидаем 60 минут
                await asyncio.sleep(3600)
        except Exception as e:
            # Отправляем сообщение администратору в случае сбоя
            error_message = f"Сбой сервера: {str(e)}"
            await context.bot.send_message(chat_id=admin_chat_id, text=error_message)
            raise e  # Повторно генерируем исключение, чтобы оно не прошло незамеченным

    # Запускаем задачу для отправки сообщений каждые 60 минут
    asyncio.create_task(send_message())

def main() -> None:
    # Создаем экземпляр ApplicationBuilder и передаем ему токен вашего бота
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()