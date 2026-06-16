from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.models.metric import Base

class Server(Base):

    __tablename__ = "servers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    hostname = Column(
        String,
        unique=True,
        nullable=False
    )

    os = Column(
        String,
        nullable=False
    )

    os_version = Column(
        String,
        nullable=False
    )