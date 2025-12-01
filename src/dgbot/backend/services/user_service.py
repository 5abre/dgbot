from dgbot.core.database import async_session
from dgbot.backend.models.user import User
from sqlalchemy import select
from datetime import date, timedelta

class UserService:
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
                
            return None
        

    async def update_user_activity(tg_id):
        async with async_session() as session:
            today = date.today()
            user = await session.scalar(select(User).where(User.tg_id == tg_id))

            if not user:
                user = User(
                    tg_id = tg_id,
                    last_activity = today,
                    consecutive_days=1
                )
                session.add(user)
            else:
                if user.last_activity == today:
                    return user
                elif user.last_activity == today - timedelta(days=1):
                    user.consecutive_days += 1
                else:
                    user.consecutive_days = 1

                user.last_activity = today
            
            await session.commit()
            await session.refresh(user)
            return user
        

    async def check_consecutive(tg_id) -> bool:
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            return user and user.consecutive_days >= 3
        

    async def reset_counter(tg_id):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if user:
                user.consecutive_days = 0
                await session.commit()
                await session.refresh(user)
            return user
        
    async def get_consecutive_days(tg_id) -> int:
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            return user.consecutive_days if user else 0
        