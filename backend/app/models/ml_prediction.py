from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.models.metric import Base

class MLPrediction(Base):

    __tablename__ = "ml_predictions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    metric_id = Column(
        Integer,
        ForeignKey("metrics.id"),
        nullable=False
    )

    prediction = Column(
        String,
        nullable=False
    )