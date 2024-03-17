from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="💵 Посчитать пеканбоны", callback_data="count_pecanbons")],
    [InlineKeyboardButton(text="📝 Поделиться с друзьями", callback_data="share_with_friends")],
    [InlineKeyboardButton(text="ℹ️ Обо мне", callback_data="about")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

#   Создание динамической клавиатуры
#   builder = InlineKeyboardBuilder()
#   for i in range(15):
#       builder.button(text=f"Кнопка {i}", callback_data=f"button_{i}")
#   builder.adjust(2)
#   await msg.answer("Текст сообщения", reply_markup=builder.as_markup())