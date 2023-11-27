import json
f = open("stemmed.json")
test_file = json.load(f)

import json

from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)
COLLECTION_NAME ="wikiSummary"
qdrant.recreate_collection(
      collection_name=COLLECTION_NAME,
      vectors_config=models.VectorParams(
          size=encoder.get_sentence_embedding_dimension(),
          distance=models.Distance.COSINE,
          on_disk=True
      ),
      shard_number=4,
    optimizers_config=models.OptimizersConfigDiff(
        indexing_threshold=0,
    ),
  )

qdrant.upload_records(
  collection_name=COLLECTION_NAME,
  records=[
    models.Record(
        id=idx, vector=encoder.encode(doc["summary"]).tolist(), payload=doc
     )
     for idx, doc in enumerate(test_file)
  ],
 )
