import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(query, products_df):
    try:
        context = "\n".join(
            [
                f"{row['name']} - Rs {row['price']} - {row['description']}"
                for _, row in products_df.iterrows()
            ]
        )

        prompt = f"""
        Recommend best products.

        Products:
        {context}

        Query:
        {query}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Recommend best products."},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Fallback response:\n{products_df[['name','price']].to_string(index=False)}"