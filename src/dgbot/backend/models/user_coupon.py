from sqlalchemy import Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from dgbot.backend.models import Base

class UserCoupon(Base):
    __tablename__ = "user_coupons"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    coupon_id: Mapped[int] = mapped_column(ForeignKey('roullete_coupons.id'))
    issued_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)