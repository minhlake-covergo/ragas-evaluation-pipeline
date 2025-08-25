import os
import datetime
from dotenv import load_dotenv

load_dotenv()

from config import DATA_FILE_PATH, EVALUATION_METRICS
from data_loader import load_data
from evaluator import Evaluator

def main():
    print("Bắt đầu quá trình...")
    dataset = load_data(DATA_FILE_PATH)

    if dataset is not None:
        print("\nXem trước 5 dòng dữ liệu đầu tiên:")
        print(dataset.head())

        print("\nBắt đầu khởi tạo bộ đánh giá (Evaluator)...")
        evaluator = Evaluator(metrics=EVALUATION_METRICS)

        results = evaluator.evaluate(dataset)

        print("\nĐánh giá hoàn tất.")
        
        results_df = results.to_pandas()
        
        print("\n----- KẾT QUẢ CHI TIẾT TỪNG DÒNG -----")
        print(results_df)

        # Lưu file 
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        file_name = f"evaluation_results_{timestamp}.csv"
        file_path = os.path.join(output_dir, file_name)

        # Lưu DataFrame thành file CSV
        results_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
        print(f"\n✅ Kết quả đã được lưu vào file: {file_path}")


if __name__ == "__main__":
    main()