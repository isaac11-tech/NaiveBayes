from pydantic import BaseModel

class LoadData(BaseModel):
    data_file: str
    target_column: str
