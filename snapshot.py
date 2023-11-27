from qdrant_client import models, QdrantClient

qdrant = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)
COLLECTION_NAME ="wikiFull"

snapshot_info = qdrant.create_snapshot(collection_name=COLLECTION_NAME)
print(snapshot_info)
snapshots = qdrant.list_snapshots(collection_name=COLLECTION_NAME)
print(snapshots)
print(snapshots)
print("Upload file complete")