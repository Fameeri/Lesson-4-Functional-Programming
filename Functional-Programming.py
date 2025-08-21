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


# Filter Function with Customer Data

customers = [
    {"name": "Alice Johnson", "total_spent": 1250, "orders": 8, "vip_member": True},
    {"name": "Bob Smith", "total_spent": 750, "orders": 12, "vip_member": False},
    {"name": "Carol Davis", "total_spent": 2100, "orders": 15, "vip_member": True},
    {"name": "David Wilson", "total_spent": 450, "orders": 3, "vip_member": False},
    {"name": "Emma Brown", "total_spent": 980, "orders": 7, "vip_member": False},
    {"name": "Frank Miller", "total_spent": 1800, "orders": 20, "vip_member": True},
]

# TODO: Use filter() to find customers who qualify for premium promotion
# Criteria: (total_spent >= 1000 AND orders >= 5) OR vip_member == True
premium_customers = list(
    filter(
        lambda c: (c["total_spent"] >= 1000 and c["orders"] >= 5) or c["vip_member"],
        customers,
    )
)  # YOUR CODE HERE, customers))

# Test your result
print("Premium Customers for Special Promotion:")
for customer in premium_customers:
    print(
        f"  {customer['name']} - Spent: ${customer['total_spent']}, Orders: {customer['orders']}"
    )

# List Comprehensions with Sales Data

sales_data = [
    {"product": "Laptop", "q1": 150, "q2": 180, "q3": 160, "q4": 200},
    {"product": "Mouse", "q1": 300, "q2": 280, "q3": 320, "q4": 350},
    {"product": "Keyboard", "q1": 200, "q2": 190, "q3": 210, "q4": 230},
    {"product": "Monitor", "q1": 80, "q2": 95, "q3": 85, "q4": 110},
    {"product": "Headphones", "q1": 120, "q2": 140, "q3": 130, "q4": 160},
]

# TODO: Use list comprehension to create a new list with annual totals
# Include product name and total_sales
# [{'product': <product name>, 'total_sales': q1 + q2 + q3 + q4}]

annual_sales = [
    {
        "product": p["product"],
        "total_sales": p["q1"] + p["q2"] + p["q3"] + p["q4"],
    }  # YOUR CODE HERE for product in sales_data]
    for p in sales_data
]

# Test your result
print("Annual Sales Totals:")
for item in annual_sales:
    print(f"  {item['product']}: {item['total_sales']} units")

# Task 4b: Find High-Performing Products

# TODO: Use list comprehension to find products with total sales > 600
# Return just the product names
high_performers = [  # YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]
    p["product"] for p in sales_data if (p["q1"] + p["q2"] + p["q3"] + p["q4"]) > 600
]

# Test your result
print("High-Performing Products (>600 units):")
for product in high_performers:
    print(f"  {product}")

# Task 4c: Growth Analysis
# TODO: Use list comprehension to calculate Q4 vs Q1 growth percentage
# Formula: ((Q4 - Q1) / Q1) * 100
# Include products that had positive growth
growth_analysis = [  # YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]
    {
        "product": p["product"],
        "growth_percentage": ((p["q4"] - p["q1"]) / p["q1"]) * 100,
    }
    for p in sales_data
    if p["q4"] > p["q1"]
]

# Test your result
print("Products with Positive Growth (Q4 vs Q1):")
for item in growth_analysis:
    print(f"  {item['product']}: {item['growth_percentage']:.1f}% growth")
