# Download the Qdrant Docker image and repo
FROM qdrant/qdrant

# Expose the port on which the model will be served
EXPOSE 6333 6334

#Copy qdrant_storage directory to Docker Image after indexing data
COPY  qdrant_storage/ /qdrant/storage/

