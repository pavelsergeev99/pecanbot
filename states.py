from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    count_pecanbons = State()
    share_with_friends = State()
    about = State()