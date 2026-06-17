import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(project_root))

from app.database.db import engine

from app.models.metric import Base
from app.models.server import Server
from app.models.anomaly import Anomaly
from app.models.ml_prediction import MLPrediction

Base.metadata.create_all(bind=engine)