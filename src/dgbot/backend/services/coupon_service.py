from sqlalchemy import select
from dgbot.backend.models.coupon import Coupon
from dgbot.core.database import async_session
from datetime import date

async def get_coupon_by_date(target_date: date) -> list[Coupon]:
     async with async_session() as session:
         result = await session.execute(
             select(Coupon)
             .where(Coupon.coupon_date == target_date)
             .where(Coupon.coupon_date.isnot(None))
         )
         coupons = result.scalars().all()
         return coupons

def is_duet_day(check_date: date = None) -> bool:
    if check_date is None:
        check_date = date.today()
    return check_date.weekday() == 3