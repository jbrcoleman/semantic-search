from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)

SEARCH_TEXT = "A Nintendo fighting game allow you to play as Nintendo charachters like Mario to fight."

# Search data using search input
hits = qdrant.search(
    collection_name="wikiFull",
    query_vector=encoder.encode("test").tolist(),
    limit=1,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)