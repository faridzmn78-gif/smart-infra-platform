from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Metric(Base):

    __tablename__ = "metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    server_id = Column(
        Integer,
        ForeignKey("servers.id"),
        nullable=True
    )

    cpu = Column(
        Float,
        nullable=False
    )

    ram = Column(
        Float,
        nullable=False
    )

    disk = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    anomaly = relationship(
        "Anomaly",
        backref="metric",
        uselist=False
    )

    server = relationship(
        "Server",
        backref="metrics"
    )