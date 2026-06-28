# Task 4: Recommendation System

movies = {
    "Action": ["Avengers", "John Wick", "Mad Max"],
    "Comedy": ["3 Idiots", "Hera Pheri", "Golmaal"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"],
    "Romance": ["Titanic", "The Notebook", "La La Land"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("===== Movie Recommendation System =====")

print("\nAvailable Categories:")
for category in movies:
    print("-", category)

choice = input("\nEnter your favorite category: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("•", movie)
else:
    print("\nSorry! Category not found.")