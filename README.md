# Constantly Every Hour
ConstantlyEveryHourBot - это проект представляет собой телеграм-бота, который отправляет пользователю сообщения каждые 60 минут с информацией о времени работы бота. Если сервер, на котором запущен бот, останавливается, бот отправляет сообщение администратору о сбое.

## Основные функции
- Запуск бота с командой `/start`.
- Отправка сообщения пользователю каждые 60 минут с информацией о времени работы бота.
- Уведомление администратора о сбоях сервера.
- Предотвращение повторного запуска команды `/start` одним и тем же пользователем.

### Установка
1. Склонируйте репозиторий:
```bash
   git clone https://github.com/WhenYouAreStrange/ConstantlyEveryHourBot.git
   cd ConstantlyEveryHourBot
   python main.py
   ```
2. Создайте виртуальное окружение и активируйте его (если это необходимо):
```bash
   python3 -m venv venv
   source venv/bin/activate  # для Linux/MacOS
   venv\Scripts\activate  # для Windows
   ```
3. Установите необходимые библиотеки:
```bash
   pip install -r requirements.txt
```

### Используемые библиотеки
-   `python-telegram-bot`: библиотека для создания телеграм-ботов.
-   `logging`: стандартная библиотека Python для логирования.
-   `datetime`: стандартная библиотека Python для работы с датой и временем.
-   `asyncio`: стандартная библиотека Python для работы с асинхронным кодом.

### Настройка
-   В коде замените `"YOUR_TELEGRAM_BOT_TOKEN"` на ваш токен бота.
-   Получите `chat_id` администратора для этого отправьте команду `/get_chat_id` вашему боту и запишите `chat_id`, который он вернет.
-   В коде замените `"ADMIN_CHAT_ID"` на `chat_id` администратора в файле **main.ру**.
 
### Post Scriptum
Этот бот был написан, только для того что бы отслеживать работу сервера на сервисе pythonanywhere.com по причине того, что он иногда "отваливается".