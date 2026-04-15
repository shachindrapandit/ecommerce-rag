def keyword_filter(df, query):
    query = query.lower()

    # simple price filter
    if "under 50000" in query or "under 50k" in query:
        df = df[df["price"] <= 50000]

    if "laptop" in query:
        df = df[df["category"] == "laptop"]

    return df


def hybrid_search(vector_store, query):
    # Step 1: Semantic search
    semantic_results = vector_store.search(query, k=5)

    # Step 2: Keyword filtering
    filtered_results = keyword_filter(semantic_results, query)

    return filtered_results