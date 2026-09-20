from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import os
from dotenv import load_dotenv


# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


# Create Engine
engine = create_engine(DATABASE_URL)


# Base class
class Base(DeclarativeBase):
    pass


# ORM Model
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    category: Mapped[str]


# Test database connection
with engine.connect() as connection:
    print("PostgreSQL connected successfully!")


# Session
with Session(engine) as session:

    # =========================
    # READ - All Products
    # =========================

    stmt = select(Product)

    products = session.scalars(stmt).all()

    for product in products:
        print(
            product.id,
            product.name,
            product.price,
            product.category
        )


    # =========================
    # WHERE
    # =========================

    stmt = select(Product).where(
        Product.category == "electronics"
    )

    products = session.scalars(stmt).all()

    print("\nElectronics:")

    for product in products:
        print(product.name, product.price)


    # =========================
    # AND
    # =========================

    stmt = select(Product).where(
        Product.category == "electronics",
        Product.price > 100000
    )

    products = session.scalars(stmt).all()

    print("\nElectronics with price > 100000:")

    for product in products:
        print(product.name, product.price)


    # =========================
    # OR
    # =========================

    stmt = select(Product).where(
        or_(
            Product.category == "electronics",
            Product.category == "MOTOR"
        )
    )

    products = session.scalars(stmt).all()

    print("\nElectronics OR MOTOR:")

    for product in products:
        print(product.name, product.category)


    # =========================
    # IN
    # =========================

    stmt = select(Product).where(
        Product.category.in_(["electronics", "MOTOR"])
    )

    products = session.scalars(stmt).all()

    print("\nIN example:")

    for product in products:
        print(product.name, product.category)


    # =========================
    # ORDER BY
    # =========================

    stmt = select(Product).order_by(
        Product.price.desc()
    )

    products = session.scalars(stmt).all()

    print("\nSorted by price:")

    for product in products:
        print(product.name, product.price)


    # =========================
    # LIMIT
    # =========================

    stmt = select(Product).order_by(
        Product.price.desc()
    ).limit(2)

    products = session.scalars(stmt).all()

    print("\nTop 2 expensive products:")

    for product in products:
        print(product.name, product.price)


    # =========================
    # OFFSET + LIMIT
    # =========================

    stmt = (
        select(Product)
        .order_by(Product.price.desc())
        .offset(2)
        .limit(2)
    )

    products = session.scalars(stmt).all()

    print("\nPagination example:")

    for product in products:
        print(product.name, product.price)


print("\nSQLAlchemy Day 7 completed!")