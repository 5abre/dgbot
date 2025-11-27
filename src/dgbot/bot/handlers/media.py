# import os
# from pathlib import Path

# media_dir = Path(__file__).parent.parent.parent / "mediafiles"

# @router.message(Command('send_photo'))
# async def cmd_photo(message: Message):
#     photo_file = FSInputFile(path=os.path.join(media_dir, 'dg_outside.webp'))
#     msg_id = await message.answer_photo(photo=photo_file, parse_mode="HTML")
#     print(msg_id.photo[-1].file_id)