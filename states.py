from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    count_pecanpons = State()
    share_with_friends = State()
    about = State()