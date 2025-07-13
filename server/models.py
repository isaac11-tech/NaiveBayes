from pydantic import BaseModel
from pathlib import Path

class LoadData(BaseModel):
    data_file: str
    target_column: str
    data_point: dict

class DataManager:
    data_file: Path = None
    target_column: str = None
    data_point: dict = None