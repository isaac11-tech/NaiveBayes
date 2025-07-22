import pandas as pd
import os


class DataLoader:

    @staticmethod
    def load_file(file_path):
        df = None
        file_type = os.path.splitext(file_path)[1].lower()

        try:
            if file_type == ".csv":
                df = pd.read_csv(file_path)
            elif file_type in [".xls", ".xlsx"]:
                df = pd.read_excel(file_path)
            elif file_type == ".json":
                df = pd.read_json(file_path)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")

            print(f"Data loaded successfully. Length: {len(df)}")
            return df

        except Exception as e:
            print(f"Error while loading file: {e}")
            return None

