from rag import VectorStore
from hybrid_search import hybrid_search
from llm import generate_response

# init
vs = VectorStore()
vs.load_data("../data/products.csv")
vs.build_index()


def run_query(query):
    results = hybrid_search(vs, query)

    if results.empty:
        return "No products found."

    return generate_response(query, results)


if __name__ == "__main__":
    query = "Best laptop under 50k"

    print("User Query:", query)
    print("\nResponse:\n")
    print(run_query(query))