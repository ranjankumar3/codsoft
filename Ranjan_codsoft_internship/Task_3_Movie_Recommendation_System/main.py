import pandas as pd

#using collaborative filtering

# Load dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge data
movie_ratings = pd.merge(movies, ratings, on='movieId')

# Create a user-item matrix
user_movie_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating')

# Fill missing values with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Define a function to get movie recommendations for a user
def recommend_movies(user_id, num_recommendations=5):
    user_ratings = user_movie_matrix.loc[user_id]
    similar_users = user_movie_matrix.corrwith(user_ratings)
    similar_users = similar_users.dropna()
    similar_users = similar_users.sort_values(ascending=False)
    recommended_movies = []

    for user, similarity in similar_users.iteritems():
        if len(recommended_movies) >= num_recommendations:
            break
        if user not in user_ratings.index:
            similar_user_ratings = user_movie_matrix.loc[user]
            top_movie = similar_user_ratings.idxmax()
            if top_movie not in recommended_movies:
                recommended_movies.append(top_movie)

    return recommended_movies

# Example: Get movie recommendations for user 1
user_id = 1
recommendations = recommend_movies(user_id)
print(f"Recommended movies for user {user_id}:")
for i, movie in enumerate(recommendations):
    print(f"{i+1}. {movie}")
