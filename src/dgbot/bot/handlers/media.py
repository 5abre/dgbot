import os
from pathlib import Path
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

router_r = Router()

media_dir = Path(__file__).parent.parent.parent / "mediafiles"

@router_r.message(Command('send_photo'))
async def cmd_photo(message: Message):
     photo_file = FSInputFile(path=os.path.join(media_dir, 'outside.jpg'))
     msg_id = await message.answer_photo(photo=photo_file, parse_mode="HTML")
     print(msg_id.photo[-1].file_id)