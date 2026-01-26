from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import settings


class Base(DeclarativeBase):
    pass 


class RentApartments(Base):
    __tablename__ = settings.rent_apartment_table_name

    address: Mapped[str] = mapped_column(VARCHAR(255), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[float] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR(50))
    storage: Mapped[str] = mapped_column(VARCHAR(50))
    parking: Mapped[str] = mapped_column(VARCHAR(50))
    furnished: Mapped[str] = mapped_column(VARCHAR(50))
    garage: Mapped[str] = mapped_column(VARCHAR(50))
    garden: Mapped[str] = mapped_column(VARCHAR(50))
    energy: Mapped[str] = mapped_column(VARCHAR(5))
    facilities: Mapped[str] = mapped_column(VARCHAR(255))
    zip: Mapped[str] = mapped_column(VARCHAR(20))
    neighborhood: Mapped[str] = mapped_column(VARCHAR(100))
    rent: Mapped[int] = mapped_column(INTEGER())
