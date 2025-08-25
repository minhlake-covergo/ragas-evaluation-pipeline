import pandas as pd
from datasets import Dataset
from ragas import evaluate

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
)
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from ragas.run_config import RunConfig

class Evaluator:
    def __init__(self, metrics: list[str]):
        self.metric_names = metrics
        self.metrics = self._initialize_metrics()
        print(f"Evaluator đã được khởi tạo với các metric: {', '.join(self.metric_names)}")

    def _initialize_metrics(self):
        metric_map = {
            "faithfulness": faithfulness,
            "answer_relevancy": answer_relevancy,
        }
        initialized_metrics = []
        for name in self.metric_names:
            if name in metric_map:
                initialized_metrics.append(metric_map[name])
            else:
                print(f"Cảnh báo: Metric '{name}' không được hỗ trợ và sẽ bị bỏ qua.")
        return initialized_metrics
        
    def evaluate(self, dataset: pd.DataFrame):
        print("Đang chuẩn bị dữ liệu cho Ragas...")
        dataset_copy = dataset.copy()
        dataset_copy['contexts'] = dataset_copy['context'].apply(lambda x: [x])
        hf_dataset = Dataset.from_pandas(dataset_copy)
        
        print("Khởi tạo model Gemini (ChatGoogleGenerativeAI)...")
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash") # Hoặc gemini-1.5-flash
        
        print("Khởi tạo mô hình embedding của Google...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        run_config = RunConfig(max_workers=1)

        print("Bắt đầu chạy đánh giá Ragas với Gemini...")
        result = evaluate(
            dataset=hf_dataset,
            metrics=self.metrics,
            llm=llm,
            embeddings=embeddings, 
            run_config=run_config
        )
        
        print("Đánh giá hoàn tất.")
        return result