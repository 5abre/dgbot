from dgbot.core.database import async_session
from dgbot.backend.models.user import User
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_user_by_tg_id(tg_id) -> User:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        return result.scalar_one_or_none()
    

async def upd_user(tg_id, phone_number: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            user.phone_number = phone_number

            await session.commit()
            await session.refresh(user)
            
        return user