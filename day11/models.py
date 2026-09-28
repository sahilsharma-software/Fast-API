from sqlalchemy.orm import DeclarativeBase , mapped_column, Mapped

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )
    password_hash: Mapped[str] = mapped_column(nullable=False)
    role:Mapped[str] = mapped_column(default="user",nullable=False)