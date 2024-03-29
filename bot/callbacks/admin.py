from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from datetime import datetime
import os

from settings import SQLITE_PATH
from ..models import User
from ..constants import Message, States


def statistics_callback(update: Update, context: CallbackContext):
    total_users = User.select().count()
    active_users = User.select().where(User.active == True).count()

    response = Message.statistics.format(total_users=total_users, active_users=active_users)

    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=response, parse_mode=ParseMode.HTML
    )


def mailing_callback(update: Update, context: CallbackContext):
    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=Message.mailing
    )

    return States.prepare_mailing


def backup_callback(update: Update, context: CallbackContext):
    date = datetime.today().strftime('%d.%m.%Y')

    context.bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id
    )

    if os.path.isfile(SQLITE_PATH):
        with open(SQLITE_PATH, 'rb') as file:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                caption=Message.backup.format(date),
                document=file
            )

    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.database_not_found
        )
