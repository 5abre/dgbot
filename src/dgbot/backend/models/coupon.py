from sqlalchemy import String, Date
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dgbot.backend.models.base import Base
from dataclasses import dataclass

@dataclass
class Coupon(Base):
    __tablename__ = 'coupons'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    coupon_date: Mapped[date] = mapped_column(Date())