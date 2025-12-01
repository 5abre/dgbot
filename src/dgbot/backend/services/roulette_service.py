import random
from sqlalchemy import select
from dgbot.backend.models import UserCoupon, RouletteCoupon
from dgbot.core.database import async_session
from datetime import datetime

class RouletteService:
    DROP_CHANCES = {
        "common": 70,
        "uncommon": 25,
        "rare": 5
    }

    @staticmethod
    def get_random_category() -> str:
        rand = random.random() * 100
        chances = RouletteService.DROP_CHANCES

        if rand < chances["common"]:
            return "common"
        elif rand < chances["common"] + chances["uncommon"]:
            return "uncommon"
        else:
            return "rare"
        
    @classmethod
    async def get_random_coupon(cls) -> RouletteCoupon:
        async with async_session() as session:
            category = cls.get_random_category()
            result = await session.execute(select(RouletteCoupon).where(RouletteCoupon.category == category))
            coupons = result.scalars().all()

            if not coupons:
                result = await session.execute(select(RouletteCoupon))
                coupons = result.scalars().all()
            if not coupons:
                raise ValueError('В базе нет купонов для выдачи')
            
            return random.choice(coupons)
        
    @classmethod    
    async def issue_coupon_to_user(cls, user_id: int) -> RouletteCoupon:
        async with async_session() as session:
            coupon = await cls.get_random_coupon()

            user_coupon = UserCoupon(
                user_id = user_id,
                coupon_id = coupon.id,
                issued_at = datetime.now(),
                is_used = False
            )

            session.add(user_coupon)
            await session.commit()

            return coupon
        
    @staticmethod
    async def get_user_coupons(user_id: int):
        async with async_session() as session:
            result = await session.execute(
                select(UserCoupon, RouletteCoupon)
                .join(RouletteCoupon, UserCoupon.coupon_id == RouletteCoupon.id)
                .where(
                    UserCoupon.user_id == user_id,
                    UserCoupon.is_used == False)
                .order_by(UserCoupon.issued_at.asc())
                )
            return result.all()
            
    @staticmethod
    async def use_coupon(user_id: int, user_coupon_id: int) -> bool:
        async with async_session() as session:
            result = await session.execute(
                select(UserCoupon)
                .where(
                    UserCoupon.id == user_coupon_id,
                    UserCoupon.user_id == user_id,
                    UserCoupon.is_used == False
                )
            )
            user_coupon = result.scalar_one_or_none()

            if not user_coupon:
                return False
            
            user_coupon.is_used = True
            await session.commit()
            return True