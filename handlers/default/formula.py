from aiogram.types import FSInputFile, Message
from aiogram import Router
from aiogram.filters import Command


router = Router()


@router.message(Command(commands=['formula']))
async def formula(message: Message):
    formula_image = FSInputFile('formula.jpg')
    await message.answer_photo(formula_image)
