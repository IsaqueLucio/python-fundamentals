"""
Challenge 4: Top Tier Movie Analyzer
File: 13_movie_ratings.py

Rules:
1. Create a function called 'analyze_ratings' that takes 'category' (with a default value of "General") and '**movies' 
for dynamic movie-rating pairs.
2. Inside the function, print "--- Top Movies in [category] ---".
3. Convert the '**movies' dictionary into a list of tuples.
4. Task 1 (Filter): Use 'filter()' and a lambda to create a new list containing ONLY movies with a rating of 7.0 or higher. 
5. Task 2 (Sort): Use the .sort() method with a lambda function on the *filtered list* to sort it by rating. 
Use 'reverse=True' for highest to lowest.
6. Loop through the final sorted list and print each movie and its rating.
7. Call the function testing the logic: 
   analyze_ratings("Sci-Fi", interstellar=9.5, matrix=8.7, moonfall=5.2, inception=8.8, geostorm=4.3)
"""

def analyze_ratings(category="General", **movies):
    print(f"--- Top Movies in {category} ---")
    movie_list = list(movies.items())
    new_movie_list = list(filter(lambda rating: rating[1] >= 7.0, movie_list))
    new_movie_list.sort(key=lambda rating: rating[1], reverse=True)
    for key, value in new_movie_list:
        print(f"Film: {key} | Rating: {value}")

analyze_ratings("Sci-Fi", interstellar=9.5, matrix=8.7, moonfall=5.2, inception=8.8, geostorm=4.3)


