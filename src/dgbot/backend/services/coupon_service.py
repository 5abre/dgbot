from sqlalchemy import select
from dgbot.backend.models.coupon import Coupon
from dgbot.core.database import async_session
from datetime import date

class CouponService:
    async def get_coupon_by_date(target_date: date) -> list[Coupon]:
        async with async_session() as session:
            result = await session.execute(
                select(Coupon)
                .where(Coupon.coupon_date == target_date)
                .where(Coupon.coupon_date.isnot(None))
            )
            coupons = result.scalars().all()
            return coupons

    def day_check(check_date: date = None) -> bool:
        if check_date is None:
            check_date = date.today()

        weekday = check_date.weekday()

        if weekday == 3:
            return "thursday"
        elif weekday == 6:
            return "sunday"