User Query
   ↓
run_query()
   ↓
Hybrid Search
   ↓
 ┌────────────────────────────┐
 │ Semantic Search (FAISS)    │
 └────────────┬───────────────┘
              ↓
     Top-K Similar Products
              ↓
 ┌────────────────────────────┐
 │ Keyword Filter (price etc) │
 └────────────┬───────────────┘
              ↓
     Filtered Products
              ↓
        generate_response()
              ↓
     ┌───────────────┐
     │   LLM Call    │
     └──────┬────────┘
            │ success
            ▼
      Rich Answer

            │ failure
            ▼
      Fallback Answer