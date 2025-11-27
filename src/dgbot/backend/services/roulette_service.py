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