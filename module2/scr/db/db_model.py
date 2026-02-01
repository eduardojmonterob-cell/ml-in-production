from sqlalchemy import INTEGER, REAL, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config.config import settings


class RentApartments(DeclarativeBase):
    """
    Modelo ORM que representa apartamentos en alquiler.

    Esta clase mapea la tabla de apartamentos en alquiler dentro de la base
    de datos y define las características principales del inmueble, tales
    como ubicación, dimensiones, comodidades y precio de renta.

    Se utiliza como entidad persistente en operaciones de lectura y escritura
    mediante SQLAlchemy.

    Attributes:
        address (str): Dirección completa del apartamento. Clave primaria.
        area (float): Superficie total del apartamento en metros cuadrados.
        constraction_year (int): Año de construcción del edificio.
        rooms (int): Número total de ambientes.
        bedrooms (int): Cantidad de dormitorios.
        bathrooms (float): Número de baños.
        balcony (str): Indica si el apartamento posee balcón.
        storage (str): Indica si dispone de espacio de almacenamiento.
        parking (str): Indica si cuenta con estacionamiento.
        furnished (str): Indica si el apartamento se entrega amueblado.
        garage (str): Indica si posee garaje.
        garden (str): Indica si dispone de jardín.
        energy (str): Clasificación energética del inmueble.
        facilities (str): Lista o descripción de comodidades adicionales.
        zip (str): Código postal.
        neighborhood (str): Barrio o zona donde se ubica el apartamento.
        rent (int): Precio de alquiler mensual.
    """

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

