from app.database.db import engine

from app.models.metric import Base

# Import all models so SQLAlchemy registers them
from app.models.server import Server
from app.models.anomaly import Anomaly
from app.models.ml_prediction import MLPrediction


def init_database():
    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully")


if __name__ == "__main__":
    init_database()