from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from loguru import logger

from state import state_user


router = Router()


@router.message(Command(commands=['equations']))
async def equations(message: Message, state: FSMContext) -> None:
    logger.info(f'Пользователь {message.from_user.username} ввел команду /equations')
    await state.set_state(state=state_user.MathState.count_equation)
    await message.answer('Введите кол-во уравнений')
