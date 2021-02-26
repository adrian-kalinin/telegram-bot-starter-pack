from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


class States:
    prepare_mailing = 1
    received_mailing = 2


class CallbackData:
    statistics = 'statistics'
    mailing = 'mailing'


class ReplyButtons:
    send_mailing = 'Разослать'
    preview_mailing = 'Предпросмотр'
    cancel_mailing = 'Отменить'


class Keyboard:
    main = ReplyKeyboardMarkup([
        ['/start']
    ])

    admin = InlineKeyboardMarkup([
        [InlineKeyboardButton('Посмотреть статистику', callback_data=CallbackData.statistics)],
        [InlineKeyboardButton('Создать рассылку', callback_data=CallbackData.mailing)]
    ])

    mailing = ReplyKeyboardMarkup([
        [ReplyButtons.send_mailing],
        [ReplyButtons.preview_mailing, ReplyButtons.cancel_mailing]
    ])


class Message:
    start = '<b>Приветствую в боте :)</b>'

    admin = 'Добро пожаловать в админскую панель!'

    statistics = (
        'Статистика бота:\n\n'
        'Всего пользователей: <b>{total_users}</b>\n'
        'Активных пользователей: <b>{active_users}</b>'
    )

    mailing = 'Отправьте сообщение для рассылки'

    received_mailing = 'Сообщение для рассылки получено. Что делать дальше?'

    mailing_canceled = 'Рассылка отменена'

    mailing_started = 'Рассылка успешно началась'

    mailing_finished = (
        'Сообщение было успешно отправлено:\n\n'
        'Пользователи, получившие сообщение: {sent_count}'
    )

    unexpected_error = '<code>Telegram Error: {error}.\n\n{update}</code>'

