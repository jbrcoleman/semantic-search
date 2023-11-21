import json

from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")

# Opening JSON file
f = open('books_data.json')

documents = json.load(f)
qdrant = QdrantClient(":memory:")

qdrant.recreate_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE,
    ),
)

qdrant.upload_records(
    collection_name="my_books",
    records=[
        models.Record(
            id=idx, vector=encoder.encode(doc["description"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

# Read search file
data = open("search.txt", 'r').read()

# Replacing all occurrences of newline in data with ''
search_data = data.replace('\n', '')

# Search data using search input
hits = qdrant.search(
    collection_name="my_books",
    query_vector=encoder.encode(search_data).tolist(),
    limit=3,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)

# Narrow down search to certain year
hits = qdrant.search(
    collection_name="my_books",
    query_vector=encoder.encode(search_data).tolist(),
    query_filter=models.Filter(
        must=[models.FieldCondition(key="year", range=models.Range(gte=2000))]
    ),
    limit=1,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)