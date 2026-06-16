from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.models.metric import Base

class Anomaly(Base):

    __tablename__ = "anomalies"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    metric_id = Column(
        Integer,
        ForeignKey("metrics.id")
    )

    cpu_status = Column(String)

    ram_status = Column(String)

    disk_status = Column(String)