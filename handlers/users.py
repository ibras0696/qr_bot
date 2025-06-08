import os

from aiogram import Router, F
from utils.qr_maker import create_qr_cod
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(Command('start'))
async def qr_cmd(message: Message):
    await message.answer('Пришлите мне ссылку для преобразования в qr_code')


@router.message(Command('t'))
async def test_error_cmd(message: Message):
    raise Exception('Тестовая Ошибка')


@router.message(F.text)
async def qr_url_cmd(message: Message):
    if message.text:
        if message.text.startswith('http') or message.text.startswith('https'):
            url = message.text
            try:
                data = create_qr_cod(f'{message.from_user.id}_file', url)
                file = data.get('file')
                fsi = data.get('fsi')
                await message.answer_photo(caption='Вот готовый qr_code', photo=fsi)

                # Удаления файла после
                os.remove(file)

            except Exception as ex:
                await message.answer('Нужно присылать рабочую ссылку возможно ваша ссылка не правильная')
        else:
            await message.answer('Нужно присылать рабочую ссылку возможно ваша ссылка не правильная')
    else:
        await message.answer('Нужно прислать ссылку')
