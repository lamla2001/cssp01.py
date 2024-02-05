# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:07:52 2024

@author: velle
"""

import pandas as pd 
import matplotlib.pyplot as plt

file = pd.read_csv("movie_dataset.csv")

file.columns  = file.columns.str.strip().str.replace(" ", "_")

file["Metascore"].fillna(file["Metascore"].mean(),inplace=True)
file["Revenue_(Millions)"].fillna(file["Revenue_(Millions)"].mean(),inplace=True)

#print(file.head())

x = file["Title"]
y = file["Rating"]

#plt.scatter(x,y)

#plt.show()

Revanue = file["Revenue_(Millions)"]
rev_sum = sum(Revanue)
rev_size = len(Revanue)

rev_avg =rev_sum/rev_size
print("The average revenue of all movies is:", rev_avg)


filtered_range = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]
rev_sum = filtered_range['Revenue_(Millions)'].sum()
rev_size = len(filtered_range)
rev_avg = rev_sum / rev_size
print("The average Rev for 2015:2017 movies is:",rev_avg)

movies_2016 = file[file["Year"] == 2016]
num =len(movies_2016)
print("2016 Movies are:", num)

director = file[file["Director"] == "Christopher Nolan"]
num =len(director )
print("Movies directed by Christopher Nolan are:", num)

movies_ratting = file[file["Rating"] >= 8.0]
num =len(movies_ratting)
print("Movies with 8.0 rating are:", num)

Christopher_movies = file[file["Director"] == "Christopher Nolan"]
Median_rating = Christopher_movies["Rating"].median()
print("Average median fo movies directed by Christopher Nolan is:", Median_rating)
 
highest_average_rating = file.groupby("Year")["Rating"].mean()
highest_year_rating = highest_average_rating.idxmax()
print("The year with the highest rating is:",highest_year_rating)


filtered_range = file[(file["Year"] >= 2006) & (file["Year"] <= 2016)]
movies_2006=len(filtered_range[filtered_range["Year"]== 2006])
movies_2016=len(filtered_range[filtered_range["Year"]== 2016])

percentage = ((movies_2016-movies_2006)/movies_2006) *100
print ("The Percentage increase is:",percentage )

actors = file["Actors"].str.split(", ").explode()
common_actor = actors.value_counts().idxmax()
print("the most commen actor is :",common_actor)

genre = file["Genre"].str.split(", ").explode()
number_of_genre = genre.nunique()
print("The unique genre is:", number_of_genre)

num_file = file.select_dtypes(include=["float64","int64"])
correlation_matrix =num_file.corr()

print("Correlation metrics:", correlation_matrix)

