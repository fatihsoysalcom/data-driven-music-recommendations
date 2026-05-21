import random

def analyze_listening_history(user_history):
    """
    Analyzes a user's listening history to infer their preferred genres.
    This is the 'data analysis' part of a data-driven application, generating insights.
    """
    genre_counts = {}
    for song in user_history:
        genre = song['genre']
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    if not genre_counts:
        return []

    # Find the most frequent genres
    max_count = 0
    preferred_genres = []
    for genre, count in genre_counts.items():
        if count > max_count:
            max_count = count
            preferred_genres = [genre]
        elif count == max_count:
            preferred_genres.append(genre)

    return preferred_genres

def recommend_songs(user_history, available_songs, preferred_genres, num_recommendations=3):
    """
    Recommends songs based on preferred genres, excluding already listened songs.
    This is the 'optimization/personalization' part, providing value beyond just selling.
    """
    recommended = []
    listened_song_titles = {song['title'] for song in user_history}

    potential_recommendations = [
        song for song in available_songs
        if song['genre'] in preferred_genres and song['title'] not in listened_song_titles
    ]

    # If not enough genre-matching songs, broaden the search to any unlistened songs
    if len(potential_recommendations) < num_recommendations:
        for song in available_songs:
            if song['title'] not in listened_song_titles and song not in potential_recommendations:
                potential_recommendations.append(song)

    random.shuffle(potential_recommendations)
    return potential_recommendations[:num_recommendations]

def main():
    # Simulate a database of available songs
    available_songs_db = [
        {'title': 'Song A', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song B', 'artist': 'Artist Y', 'genre': 'Rock'},
        {'title': 'Song C', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song D', 'artist': 'Artist Z', 'genre': 'Jazz'},
        {'title': 'Song E', 'artist': 'Artist Y', 'genre': 'Rock'},
        {'title': 'Song F', 'artist': 'Artist W', 'genre': 'Electronic'},
        {'title': 'Song G', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song H', 'artist': 'Artist V', 'genre': 'Classical'},
        {'title': 'Song I', 'artist': 'Artist Y', 'genre': 'Rock'},
        {'title': 'Song J', 'artist': 'Artist U', 'genre': 'Electronic'},
    ]

    # Simulate a user's listening history (raw data collection)
    user_listening_history = [
        {'title': 'Song A', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song C', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song B', 'artist': 'Artist Y', 'genre': 'Rock'},
        {'title': 'Song G', 'artist': 'Artist X', 'genre': 'Pop'},
        {'title': 'Song E', 'artist': 'Artist Y', 'genre': 'Rock'},
    ]

    print("--- User's Listening History ---")
    for song in user_listening_history:
        print(f"- {song['title']} by {song['artist']} ({song['genre']})")
    print("\n" + "="*30 + "\n")

    # Step 1: Analyze user data to get insights
    preferred_genres = analyze_listening_history(user_listening_history)
    print(f"--- Inferred User Preferences (Data Insights) ---")
    if preferred_genres:
        print(f"Preferred genres: {', '.join(preferred_genres)}")
    else:
        print("No clear preferred genres yet.")
    print("\n" + "="*30 + "\n")

    # Step 2: Use insights to provide a personalized experience (recommendations)
    # This demonstrates value through personalization, illustrating the article's core concept
    # of going beyond direct product sales (e-commerce trap).
    recommendations = recommend_songs(user_listening_history, available_songs_db, preferred_genres)
    print("--- Personalized Song Recommendations ---")
    if recommendations:
        for i, song in enumerate(recommendations):
            print(f"{i+1}. {song['title']} by {song['artist']} ({song['genre']})")
    else:
        print("No new recommendations at this time.")
    print("\nThis example focuses on providing value through personalization based on data,")
    print("rather than directly pushing sales, illustrating the article's core concept.")

if __name__ == "__main__":
    main()
