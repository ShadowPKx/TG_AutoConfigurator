HELP = '<b>Доступные команды:</b>\n' \
    '/help - список команд.\n' \
    '/get_full_logs - получить полные логи.\n' \
    '/get_last_logs [n] - получить последние n строк логов (по умолчанию 15).\n' \
    '/list или /sources_list - список источников постов\n' \
    '/remove - удалить источник постов\n' \
    '/add -  добавить источник постов\n' \
    '/get_config - получить файл конфигурации бота\n\n' \
    '/kill - команда самоуничтожения :) Завершение работы бота TG_AutoConfigurator. Ничего не делает в Windows :/'
ADD = 'Команда используется для добавления нового источника постов.\n\n' \
      'Использование:\n`/add <домен или ссылка группы ВК> <ID Telegram чата (или ссылка через @)> [ID поста ВК]`\n' \
      '`<>` - обязательный параметр\n`[]` - необязательный параметр\n' \
      '`ID поста ВК` - начиная с какого поста бот должен начать отправку постов (если не указано, бот отправит последние 11 постов)'
REMOVE = 'Команда используется для удаления источника постов.\n\n' \
         'Использование:\n`/remove <домен группы ВК>`\n' \
         '`<>` - обязательный параметр'
