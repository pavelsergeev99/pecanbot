from aiogram import types, F, Router, flags
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

import kb
import text
import utils
from states import Gen

router = Router()

"""Command("start") запускает обработчик только если входящее сообщение — команда /start"""
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "count_pecanbons")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.count_pecanbons)
    await clbck.message.edit_text(text.text_count_pecanbons.format(text.text_pecanbon_price))

@router.message(Gen.count_pecanbons)
@flags.chat_action("typing")
async def count_pecanbons_get_input(msg: Message, state: FSMContext):
    prompt = msg.text
    mesg = await msg.answer(text.gen_wait)
    res = await utils.generate_pecanbot_count(prompt)
    if res == 0:
        return await mesg.edit_text(text.text_count_pecanbons_negative, reply_markup=kb.iexit_kb)
    await mesg.edit_text(text.text_count_pecanbons_result.format(prompt, str(res)) + text.text_watermark, disable_web_page_preview=True)

@router.callback_query(F.data == "share_with_friends")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.share_with_friends)
    await clbck.message.edit_text(text.text_share_with_friends)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.iexit_kb)

"""
@router.callback_query(f.data == "")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
"""

@router.callback_query(F.data == "about")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.about)
    await clbck.message.edit_text(text.text_about)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.iexit_kb)

"""
@router.message(Gen.text_prompt)
@flags.chat_action("typing")
async def generate_text(msg: Message, state: FSMContext):
    prompt = msg.text
    mesg = await msg.answer(text.gen_wait)
    res = await utils.generate_text(prompt)
    if not res:
        return await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)
    await mesg.edit_text(res[0] + text.text_watermark, disable_web_page_preview=True)
"""