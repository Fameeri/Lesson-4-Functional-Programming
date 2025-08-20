movies = [
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi"},
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Thriller"},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime"},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime"},
    {"title": "Avatar", "year": 2009, "rating": 7.8, "genre": "Sci-Fi"},
    {"title": "Titanic", "year": 1997, "rating": 7.8, "genre": "Romance"},
]

# TODO: Sort movies by rating (highest first)
by_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)  # YOUR CODE HERE)

# TODO: Sort movies by year (newest first)
by_year = sorted(movies, key=lambda m: m["year"], reverse=True)  # YOUR CODE HERE)

# Test your sorting
print("Highest rated:", by_rating[0]["title"])
print("Newest movie:", by_year[0]["title"])


# Movie Classification
# TODO: Create a lambda to classify movies by era
# - Year >= 2000: 'Modern'
# - Year >= 1990: 'Recent'
# - Otherwise: 'Classic'
classify_era = lambda year: (
    "Modern" if year >= 2000 else "Recent" if year >= 1990 else "Classic"
)  # YOUR CODE HERE

# TODO: Create a lambda to determine rating category
# - Rating >= 9.0: 'Masterpiece'
# - Rating >= 8.0: 'Excellent'
# - Otherwise: 'Good'
rating_category = lambda rating: (
    "Masterpiece" if rating >= 9.0 else "Excellent" if rating >= 8.0 else "Good"
)  # YOUR CODE HERE

# Test your lambdas
print("Movie Classifications:")
for movie in movies:
    era = classify_era(movie["year"])
    category = rating_category(movie["rating"])
    print(f"{movie['title']}: {era}, {category}")


# Map Function with Tempreature Data

weather_data = [
    {"city": "New York", "temp_celsius": 22, "humidity": 65},
    {"city": "London", "temp_celsius": 15, "humidity": 80},
    {"city": "Tokyo", "temp_celsius": 28, "humidity": 70},
    {"city": "Sydney", "temp_celsius": 18, "humidity": 60},
    {"city": "Dubai", "temp_celsius": 35, "humidity": 45},
]

# TODO: Use map() with lambda or user defined function to add Fahrenheit and Kelvin temperatures
# Formula: Fahrenheit = (Celsius × 9/5) + 32
# Formula: Kelvin = Celsius + 273.15
weather_converted = list(
    map(
        lambda data: {
            **data,
            "temp_fahrenheit": (data["temp_celsius"] * 9 / 5) + 32,
            "temp_kelvin": data["temp_celsius"] + 273.15,
        },
        weather_data,
    )
)  # YOUR CODE HERE, weather_data))

# Test your result
print("Temperature Conversions:")
for data in weather_converted:
    print(f"{data['city']}:")
    print(f"  Celsius: {data['temp_celsius']}°C")
    print(f"  Fahrenheit: {data['temp_fahrenheit']:.1f}°F")
    print(f"  Kelvin: {data['temp_kelvin']:.1f}K")
