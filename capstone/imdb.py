import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("imdb.csv")
print("Movie DataSet")
print(movies)

ratings = movies["Rating"]
average_rating = ratings.mean()
print("\nAverage Rating")
print(average_rating)

variance = np.var(ratings)
print("\nVariance")
print(variance)

std = np.std(ratings)
print(std)

best_movie = movies.loc[movies["rating"].idxmax()]

print("\nHighest Rated Movie")
print("best_Month")
plt.hist(
    ratings,
    bins=5
)

plt.title("IMDB Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()