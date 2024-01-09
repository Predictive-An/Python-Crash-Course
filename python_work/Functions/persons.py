def city_country(city, country):
    return f"{city}, {country}"

# Calling the function with three city-country pairs
result1 = city_country("Santiago", "Chile")
result2 = city_country("Tokyo", "Japan")
result3 = city_country("Berlin", "Germany")

# Printing the returned values
print(result1)
print(result2)
print(result3)

def make_album(artist, title):
    return {'artist': artist, 'title': title}

# Creating three dictionaries representing different albums
album1 = make_album("Taylor Swift", "Fearless")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Ed Sheeran", "Divide")

# Printing each return value to show the stored album information
print(album1)
print(album2)
print(album3)
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

# Function calls with different scenarios
album1 = make_album("Taylor Swift", "Fearless", num_songs=16)
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Ed Sheeran", "Divide", num_songs=12)

# Printing each return value to show the stored album information
print(album1)
print(album2)
print(album3)
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

# Interactive input using a while loop
while True:
    artist_input = input("Enter the artist's name (or 'quit' to exit): ")
    
    if artist_input.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    title_input = input("Enter the album title: ")
    
    # Allowing the user to optionally enter the number of songs
    num_songs_input = input("Enter the number of songs (or press Enter to skip): ")
    if num_songs_input.strip():  # Check if the input is not empty
        num_songs = int(num_songs_input)
    else:
        num_songs = None
    
    # Calling make_album() with user input and printing the result
    album_info = make_album(artist_input, title_input, num_songs)
    print(album_info)
def show_messages(messages):
    for message in messages:
        print(message)
