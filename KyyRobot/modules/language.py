import itertools

from typing import Union, List, Dict, Callable, Generator, Any
from collections.abc import Iterable
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

import KyyRobot.modules.sql.language_sql as sql
from KyyRobot import dispatcher
from KyyRobot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from KyyRobot.language import get_string, get_languages, get_language


def paginate(iterable: Iterable, page_size: int) -> Generator[List, None, None]:
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (
            itertools.islice(i1, page_size, None),
            list(itertools.islice(i2, page_size)),
        )
        if len(page) == 0:
            break
        yield page


def gs(chat_id: Union[int, str], string: str) -> str:
    lang = sql.get_chat_lang(chat_id)
    return get_string(lang, string)


@user_admin
def set_lang(update: Update, _) -> None:
    chat = update.effective_chat
    msg = update.effective_message

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = []
    for code, name in get_languages().items():
        keyb.append(
            InlineKeyboardButton(
                text=name,
                callback_data=f"setLang_{code}",
            )
        )

    keyb = list(paginate(keyb, 2))
    keyb.append(
        [
            InlineKeyboardButton(
                text="Help us in translations",
                url="https://poeditor.com/join/project?hash=oJISpjNcEx",
            )
        ]
    )
    msg.reply_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))


@user_admin_no_reply
def lang_button(update: Update, _) -> None:
    query = update.callback_query
    chat = update.effective_chat

    query.answer()
    lang = query.data.split("_")[1]
    sql.set_lang(chat.id, lang)

    query.message.edit_text(
        gs(chat.id, "set_chat_lang").format(get_language(lang)[:-3]),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⬅️ Back",
                        callback_data=f"back_",
                    )
                ]
            ]
        )
    )
    
@user_admin
def back_button(update: Update, _) -> None:
    chat = update.effective_chat
    query = update.callback_query

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = [
        InlineKeyboardButton(
            text=name,
            callback_data=f"setLang_{code}",
        )
        for code, name in get_languages().items()
    ]
    keyb = list(paginate(keyb, 2))
    keyb.append(
        [
            InlineKeyboardButton(
                text="Help us in translations",
                url="https://poeditor.com/join/project?hash=gXVtzsSQ88",
            )
        ]
    )

    if query.data == "back_":
        query.message.edit_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))


SETLANG_HANDLER = CommandHandler("setlang", set_lang, run_async=True)
SETLANG_BUTTON_HANDLER = CallbackQueryHandler(lang_button, pattern=r"setLang_", run_async=True)
BACK_BUTTON_HANDLER = CallbackQueryHandler(back_button, pattern=r"back_")

dispatcher.add_handler(SETLANG_HANDLER)
dispatcher.add_handler(SETLANG_BUTTON_HANDLER)
dispatcher.add_handler(BACK_BUTTON_HANDLER)
