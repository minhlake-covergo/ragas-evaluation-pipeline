import pandas as pd

def load_data(file_path: str):
    """
    Đọc dữ liệu từ một file CSV và trả về một pandas DataFrame.
    
    Args:
        file_path (str): Đường dẫn tới file CSV.
        
    Returns:
        pd.DataFrame: DataFrame chứa dữ liệu từ file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Đã tải thành công dữ liệu từ: {file_path}")
        return df
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn: {file_path}")
        return None