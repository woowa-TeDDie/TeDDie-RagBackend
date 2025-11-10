from functools import lru_cache
from rag.RagSearch import WoowacourseRAG
from pathlib import Path

@lru_cache(maxsize=1)
def get_rag_system() -> WoowacourseRAG:
    dataset_path = Path("../TeDDie-RagSystem/woowacourse_rag_dataset.jsonl")
    index_path = Path("../TeDDie-RagSystem/faiss_index.bin")

    rag = WoowacourseRAG(str(dataset_path))

    if index_path.exists():
        try:
            rag.load_index(str(index_path))
            print("[INFO] ✅ RAG index successfully loaded.")
        except Exception as e:
            print(f"[WARN] ⚠️ Failed to load RAG index: {e}")
    else:
        print("[WARN] ⚠️ No FAISS index found. Run build_index() manually.")

    return rag
