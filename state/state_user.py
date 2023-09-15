from aiogram.fsm.state import StatesGroup, State


class MathState(StatesGroup):
    count_equation = State()
    sending_equations = State()
    first_equations = State()
