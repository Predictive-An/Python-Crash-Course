def build_profile(first_name, last_name, **additional_info):
    profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    profile.update(additional_info)
    return profile

# Creating a profile of myself
my_profile = build_profile(
    first_name="John",
    last_name="Doe",
    age=25,
    occupation="Software Engineer",
    country="United States"
)

# Printing the profile
print(my_profile)
print("\n ----------")
def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    car.update(car_info)
    return car

# Calling the function with required information and additional key-value pairs
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)

# Printing the dictionary returned by the function
print(car)