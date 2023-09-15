from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from loguru import logger

from state import state_user
from utils.generate_equation import generate_equation
from filters.check_solution import CheckSolution


router = Router()


@router.message(StateFilter(state_user.MathState.first_equations), CheckSolution())
async def solution_equations(message: Message, state: FSMContext):
    data = await state.get_data()
    equation, answer = generate_equation()
    await state.update_data(resolved=data['resolved'] + 1, answer=answer)
    if data['resolved'] + 1 == data['count_equation']:
        await message.answer('Вы решили все уравнения!\n'
                             'Повторите команду, чтобы решать новые уравнения')

    else:
        await state.set_state(state=state_user.MathState.first_equations)
        await message.answer(f'Уравнение {data["resolved"] + 2} из {data["count_equation"]}\n\n'
                             f'<b>{equation}</b>\n\n'
                             f'Вид ответа:\n'
                             f'нет решения\n'
                             f'x\n'
                             f'x1;x2')


@router.message(StateFilter(state_user.MathState.first_equations))
async def wrong_solution(message: Message):
    await message.answer('Ответ неверный')
