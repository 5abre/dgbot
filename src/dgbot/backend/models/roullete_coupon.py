from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from dgbot.backend.models.base import Base
from dataclasses import dataclass

@dataclass
class RouletteCoupon(Base):
    __tablename__ = 'roullete_coupons'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category: Mapped[str] = mapped_column(String(25))