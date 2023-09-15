from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from loguru import logger

from state import state_user
from utils.generate_equation import generate_equation


router = Router()


@router.message(StateFilter(state_user.MathState.count_equation), F.text.isdigit())
async def count_equation(message: Message, state: FSMContext):
    equation, answer = generate_equation()
    await state.update_data(count_equation=int(message.text), resolved=0, answer=answer)
    await state.set_state(state=state_user.MathState.first_equations)
    await message.answer(f'Уравнение 1 из {message.text}\n'
                         f'<b>{equation}</b>\n'
                         f'Вид ответа:\n'
                         f'нет решения\n'
                         f'x\n'
                         f'x1;x2')


@router.message(StateFilter(state_user.MathState.count_equation))
async def wrong_num(message: Message):
    logger.info(f'Пользователь {message.from_user.username} ввел неверное число')
    await message.answer('Число не должно содержать символы')