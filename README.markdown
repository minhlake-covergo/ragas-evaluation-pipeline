# Pipeline Đánh giá RAG

Đây là pipeline đơn giản để đánh giá chất lượng của các hệ thống RAG (Retrieval-Augmented Generation) bằng thư viện **ragas**.

## Các Metric đang sử dụng

Pipeline này hiện đang được cấu hình để đánh giá dựa trên 2 metric chính:

- **Faithfulness (Tính trung thực)**: Đo lường mức độ nhất quán về mặt thực tế của câu trả lời so với ngữ cảnh được truy xuất. Điểm số dao động từ 0 đến 1, điểm càng cao cho thấy tính nhất quán càng tốt.
- **Response Relevancy (Sự liên quan của câu trả lời)**: Đo lường mức độ liên quan của câu trả lời so với câu hỏi của người dùng. Điểm cao cho thấy sự phù hợp tốt với câu hỏi, trong khi điểm thấp được đưa ra nếu câu trả lời không đầy đủ hoặc chứa thông tin thừa.

## Yêu cầu về dữ liệu đầu vào

- **Định dạng file**: CSV
- **Vị trí**: File dữ liệu cần được đặt trong thư mục `data/`.
- **Các cột bắt buộc**: File CSV phải chứa 3 cột với tên chính xác là `question`, `answer`, và `context`.

## Hướng dẫn sử dụng

### 1. Cài đặt môi trường

Clone repository và cài đặt các thư viện cần thiết.

```bash
# Cài đặt các thư viện từ file requirements.txt
pip install -r requirements.txt
```

### 2. Cấu hình API Key

Tạo một file có tên `.env` ở thư mục gốc của dự án và thêm Google API Key. 

```plaintext
# File: .env
GOOGLE_API_KEY="your_google_api_key_here"
```

### 3. Chạy Pipeline

Sau khi cài đặt xong, chạy file `main.py` từ thư mục gốc.

```bash
python pipeline/main.py
```

### 4. Xem kết quả

- Một file CSV chứa toàn bộ kết quả sẽ được tự động lưu vào thư mục `output/`.
