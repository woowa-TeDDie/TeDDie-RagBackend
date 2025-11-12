from domain.rag.ragEngine import RagEngine

class RagRepository:
    def __init__(self):
        self.engine = RagEngine()

    def is_index_loaded(self) -> bool:
        return getattr(self.engine.model, "index", None) is not None

    def search_documents(self, query: str, top_k: int):
        raw = self.engine.search(query, top_k)
        results = []
        for item in raw:
            doc, score = (item[0], item[1]) if isinstance(item, (tuple, list)) else (item, 0.0)
            results.append({
                "repo": getattr(doc, "repo", "unknown"),
                "text": getattr(doc, "text", ""),
                "url": getattr(doc, "url", ""),
                "similarity_score": float(score)
            })
        return results
