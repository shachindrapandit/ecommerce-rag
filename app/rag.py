from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.data = None

    def load_data(self, path):
        self.data = pd.read_csv(path)

    def build_index(self):
        texts = (self.data["name"] + " " + self.data["description"]).tolist()
        embeddings = self.model.encode(texts)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def search(self, query, k=3):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), k)

        return self.data.iloc[indices[0]]