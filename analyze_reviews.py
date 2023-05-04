import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file and set the type of the date column
reviews = pd.read_csv("branch_reviews.csv", index_col=0, parse_dates=["date"])

# Display a histogram of the number of reviews by date
reviews["date"].hist()
#plt.show()

# Create a new dataframe from reviews with the average rating for each date
reviews_by_date = reviews.groupby("date").mean()

# Plot a 30-day moving average rating per date
reviews_by_date[90:].rolling(30).mean().plot()
#plt.show()

# Print the number of reviews by rating
print(reviews["rating"].value_counts())

# Describe reviews
print(reviews.describe())