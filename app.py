import streamlit as st 

import joblib
import time

from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

# Search Predictions
def search(search_txt):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    qdrant = QdrantClient("http://localhost:6333")

    # Search data using search input
    hits = qdrant.search(
        collection_name="wiki",
        query_vector=encoder.encode(search_txt).tolist(),
        limit=1,
    )
    for hit in hits:
        print(hit.payload, "score:", hit.score)
    return hits

def main():
    """
    Wiki Article Suggestion

    """
    st.title("Wiki Article Suggestion with Streamlit")
    html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Wiki Article Suggestion </h2>
    </div>

    """
    st.markdown(html_temp,unsafe_allow_html=True)
 

    search_txt = st.text_input("Enter Search")
    if st.button("Search Articles"):
        results = search(search_txt)
        for hit in results:
            rtrn = f"{hit.payload['name']}, wikipedia url: https://en.wikipedia.org/wiki/{hit.payload['name']}"
        st.success(rtrn)
 

if __name__ == '__main__':
    main()