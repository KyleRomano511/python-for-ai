import ollama
from pymongo import MongoClient

# Setup Connection

uri = "mongodb+srv://read:123@cluster0.df0fbnh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["sample_mflix"]
collection = db["movies"]


def ask_movie_expert():
    movie_name = input("\n🎬 Enter a movie title to analyze: ")

    # Search MongoDB
    movie_data = collection.find_one({"title": {"$regex": movie_name, "$options": "i"}})

    if not movie_data:
        print(f"❌ Could not find '{movie_name}' in the database.")
        return

    # Prepare the Context
    context = (
        f"Title: {movie_data.get('title')}\n"
        f"Year: {movie_data.get('year')}\n"
        f"Plot: {movie_data.get('fullplot')}\n"
        f"Cast: {', '.join(movie_data.get('cast', []))}"
    )

    print(f"🔎 Found data for {movie_data['title']}. Asking Ollama...")

    # Chat
    response = ollama.chat(
        model="gemma3",
        messages=[
            {
                "role": "system",
                "content": "You are a professional film critic. Use the provided movie data to give a deep analysis. If information is missing, say you dont know.",
            },
            {"role": "user", "content": f"Analyze this movie for me:\n\n{context}"},
        ],
    )

    print("\n--- AI ANALYSIS ---")
    print(response["message"]["content"])


if __name__ == "__main__":
    try:
        # Check connection
        client.admin.command("ping")
        print("✅ Successfully connected to MongoDB!")

        while True:
            ask_movie_expert()
    except Exception as e:
        print(f"❌ Connection Error: {e}")
