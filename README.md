# Telegram Bot Start Pack
Starter pack for Telegram bot that contains well done architecture, database for users, admin panel, broadcasting and error handling.

## Project Structure Explained

`main.py` — entry point, bound handlers, setup database and webhook.

`config.ini` — configuration variables.

`settings.py` — reads config and creates corresponding python variables.

`bot` — package with core logic: models, handlers, callbacks, utils and constants.  

`bot/models.py` — database models.

`bot/constants.py` — messages, buttons, keyboards and callback data.

`bot/utils.py` — code not related to main bot logic.

`bot/handlers.py` — bound callbacks to different updates using filters.

`bot/callbacks` — core logic.

`bot/callbacks/admin.py` — admin panel with statistics, broadcasting and database backup.

`bot/callbacks/commands.py` — all commands from users.

`bot/callbacks/mailing.py` — broadcasting a message to all users.

`bot/callbacks/service.py` — single callback to handle errors.
