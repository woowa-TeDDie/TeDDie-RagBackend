from rag.RagSearch import WoowacourseRAG
from pathlib import Path

class RagEngine:
    def __init__(self):
        dataset = Path("../TeDDie-RagSystem/woowacourse_rag_dataset.jsonl")
        index = Path("../TeDDie-RagSystem/faiss_index.bin")
        self.model = WoowacourseRAG(str(dataset))
        if index.exists():
            self.model.load_index(str(index))
        else:
            print("[WARN] ⚠️ No FAISS index found")

    def search(self, query: str, top_k: int):
        return self.model.search(query, top_k=top_k)
