from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters

from settings import ADMINS
from .constants import CallbackData, States, ReplyButtons
from .callbacks import *


# command handlers
admin_handler = CommandHandler(
    command='admin', callback=admin_command_callback,
    filters=Filters.user(user_id=ADMINS) & Filters.private
)

start_handler = CommandHandler(
    command='start', callback=start_command_callback,
    filters=Filters.private
)

# admin handlers
statistics_handler = CallbackQueryHandler(
    pattern=CallbackData.statistics,
    callback=statistics_callback
)

backup_handler = CallbackQueryHandler(
    pattern=CallbackData.backup,
    callback=backup_callback
)

# mailing handlers
mailing_conversation_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=CallbackData.mailing, callback=mailing_callback)],
    states={
        States.prepare_mailing: [MessageHandler(callback=mailing_message_callback, filters=Filters.all)],
        States.received_mailing: [
            MessageHandler(
                filters=Filters.text(ReplyButtons.preview_mailing) & Filters.private,
                callback=preview_mailing_callback
            ),
            MessageHandler(
                filters=Filters.text(ReplyButtons.cancel_mailing) & Filters.private,
                callback=cancel_mailing_callback
            ),
            MessageHandler(
                filters=Filters.text(ReplyButtons.send_mailing) & Filters.private,
                callback=send_mailing_callback
            )
        ]
    },
    fallbacks=[]
)

# core handlers
...
