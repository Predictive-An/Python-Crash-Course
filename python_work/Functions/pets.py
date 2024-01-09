def make_shirt(size, message):
    print(f"Creating a shirt of size {size} with the message: '{message}'.")

# Calling the function with positional arguments
make_shirt("Medium", "Hor-lor-lade")

# Calling the function with keyword arguments
make_shirt(size="Large", message="Python is fun!")
def make_shirt(size="Large", message="I love Python"):
    print(f"Creating a shirt of size {size} with the message: '{message}'.")

# Calling the function with default values (Large size and default message)
make_shirt()

# Calling the function with default size and default message for a medium shirt
make_shirt(size="Medium")

# Calling the function with a different size and a custom message
make_shirt(size="Small", message="Python is awesome!")
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York")  # Using the default country ("Unknown") for this call


