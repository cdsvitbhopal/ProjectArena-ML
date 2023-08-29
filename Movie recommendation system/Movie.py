import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.metrics import average_precision_score

# Load movie credits and details datasets
movie_credits = pd.read_csv(r"C:\Users\HP\Documents\Data Science Project\Movie recommendation system\tmdb_5000_credits.csv")
movie_details = pd.read_csv(r"C:\Users\HP\Documents\Data Science Project\Movie recommendation system\tmdb_5000_movies.csv")

# Rename the 'movie_id' column in the credits dataset
credits_renamed = movie_credits.rename(index=str, columns={"movie_id": "id"})

# Merge movie details and credits datasets on the 'id' column
merged_data = movie_details.merge(credits_renamed, on='id')

# Remove unnecessary columns from the merged dataset
cleaned_data = merged_data.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])

# Fill missing values in the 'overview' column with an empty string
cleaned_data['overview'].fillna('', inplace=True)

# Create a TF-IDF vectorizer for text processing
tfidf_vectorizer = TfidfVectorizer(
    min_df=3,
    max_features=None,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'\w{1,}',
    ngram_range=(1, 3),
    stop_words='english'
)

# Fit the TF-IDF vectorizer on the 'overview' text and transform it into a TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_data['overview'])

# Compute the sigmoid kernel for the TF-IDF matrix
sigmoid_scores = sigmoid_kernel(tfidf_matrix, tfidf_matrix)

# Create a mapping of movie titles to their indices in the cleaned dataset
movie_indices = pd.Series(cleaned_data.index, index=cleaned_data['original_title']).drop_duplicates()

# Define a function to provide movie recommendations
def get_movie_recommendations(title, sigmoid_scores=sigmoid_scores):
    # Get the index corresponding to the original_title
    idx = movie_indices[title]

    # Get the pairwise similarity scores
    similarity_scores = list(enumerate(sigmoid_scores[idx]))

    # Sort the movies by similarity scores
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get scores of the 10 most similar movies
    top_scores = sorted_scores[1:11]

    # Get movie indices
    recommended_movie_indices = [i[0] for i in top_scores]

    # Get top 10 most similar movie titles
    return cleaned_data['original_title'].iloc[recommended_movie_indices]

# Take user input for movie name and provide recommendations
user_movie_name = input("Enter movie name here: ")
print(get_movie_recommendations(user_movie_name))

ground_truth_indices = np.array([...])  # Replace with actual ground truth movie indices for the user
recommended_indices_1 = np.array([...])  # Replace with actual predicted recommended movie indices (recommendation 1)
recommended_indices_2 = np.array([...])  # Replace with actual predicted recommended movie indices (recommendation 2)

# Creating binary relevance arrays
true_relevance = np.isin(recommended_indices_1, ground_truth_indices).astype(int)
predicted_relevance = np.ones_like(true_relevance)  # Assuming all recommended items are relevant

# Calculate Average Precision (AP) for the recommendation
average_precision = average_precision_score(true_relevance, predicted_relevance)
print("Average Precision:", average_precision)

