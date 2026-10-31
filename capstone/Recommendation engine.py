import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ratings_df = pd.read_csv("ratings.csv")
print("\nFirst 5 rows of Ratings Dataset:")
print(ratings_df.head())
movies_df = pd.read_csv("movies.csv")
print("\nFirst 5 rows of Movies Dataset:")
print(movies_df.head())
movies_df['year'] = movies_df['title'].str.extract(
    r'\((\d{4})\)', expand=False
)
movies_df['title'] = movies_df['title'].str.replace(
    r'\s*\(\d{4}\)', '', regex=True
)
movies_df['title'] = movies_df['title'].str.strip()
print("\nMovies Dataset After Cleaning Titles:")
print(movies_df.head())
movies_df['genres'] = movies_df['genres'].str.split('|')
movies_copy = movies_df.copy()
for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1
movies_copy = movies_copy.fillna(0)
print("\nMovies Dataset After Genre Encoding:")
print(movies_copy.head())
if 'timestamp' in ratings_df.columns:
    ratings_df = ratings_df.drop(['timestamp'], axis=1)
print("\nRatings Dataset After Removing Timestamp:")
print(ratings_df.head())
genre_columns = movies_copy.drop(
    ['movieId', 'title', 'genres', 'year'],
    axis=1
)
genre_counts = genre_columns.sum().sort_values(
    ascending = False
)
plt.figure(figsize=(12,6))
plt.bar(
    genre_counts,index,
    genre_counts,values,
    color='#4C9AFF'
)
plt.title('Movies Per Genre',fontsize=16)
plt.xlabel('genre',fontsize=12)
plt.ylabel('number of Movies',fontsize=12)
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()
print("Rating Dataset shape")
print(ratings_df.shape)
print("Movies Dataset shape:")
print(movies_copy.shape)
print("Centre Counts")
print(genre_counts)