import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path):
        self._data = None
        self.file_path = file_path

    import pandas as pd
    import os

    def load_file(self,):
        file_type = os.path.splitext(self.file_path)[1].lower()

        try:
            if file_type == ".csv":
                self._data = pd.read_csv(self.file_path)
            elif file_type in [".xls", ".xlsx"]:
                self._data = pd.read_excel(self.file_path)
            elif file_type == ".json":
                self._data = pd.read_json(self.file_path)
            elif file_type == ".sql":

                self._data = pd.read_sql("SELECT * FROM your_table_name", self.connection)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")

            print(f"Data loaded successfully. Length: {len(self._data)}")
            return self._data

        except Exception as e:
            print(f"Error while loading file: {e}")
            return None

    def get_data(self):
        return self._data
