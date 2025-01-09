import requests  # For making HTTP requests to fetch Billboard data
from pprint import pprint  # For pretty-printing JSON or dictionary data
from bs4 import BeautifulSoup  # For parsing HTML to extract song data
from spotipy.oauth2 import SpotifyOAuth  # For Spotify authentication
import spotipy  # For interacting with the Spotify Web API

# Spotify API credentials (replace with your CLIENT_ID and CLIENT_SECRET)
CLIENT_ID = ""
CLIENT_SECRET = ""

# Prompt user to input the desired date in YYYY-MM-DD format to fetch Billboard data
# date = input("What date would you like to travel to? Enter the date in YYYY-MM-DD format")
date = ""  # Replace with the desired date in the format YYYY-MM-DD
year = date.split("-")[0]  # Extract the year from the date

# Fetch the Billboard Hot 100 page for the specified date
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
webpage = response.text  # Get the raw HTML content of the webpage

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Select all song titles from the parsed HTML using CSS selectors
song_names_spans = soup.select("li ul li h3")  # Select the h3 elements containing song names
# Extract and clean the song names
song_names = [song.get_text().strip() for song in song_names_spans]

# Initialize the Spotify client with authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Scope for creating and modifying private playlists
        redirect_uri="http://example.com",  # Redirect URI specified in Spotify app settings
        client_id=CLIENT_ID,  # Spotify CLIENT_ID
        client_secret=CLIENT_SECRET,  # Spotify CLIENT_SECRET
        show_dialog=True,  # Display dialog for user to authorize access
        cache_path="token.txt"  # Cache file for storing the access token
    )
)

# List to store Spotify track URIs for the songs
spotify_uris = []

# Search for each song on Spotify and retrieve its URI
for song in song_names:
    query = f"track:{song} year:{year}"  # Construct a query for the song and year
    try:
        result = sp.search(q=query, type='track')  # Search for the track on Spotify
        if result['tracks']['items']:  # Check if any tracks were found
            track = result['tracks']['items'][0]  # Get the first result
            spotify_uris.append(track['uri'])  # Append the track URI to the list
    except Exception as e:
        print(f"An error occurred while searching for {song}: {e}")  # Handle any errors during search

# pprint(spotify_uris)  # Debug: Print the list of Spotify track URIs

# Retrieve the current user's Spotify user ID
user_id = sp.current_user()["id"]

# Create a new Spotify playlist with the specified name
playlist_name = f"{date} Billboard 100"  # Name the playlist based on the date
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)  # Create a private playlist
playlist_id = playlist["id"]  # Get the playlist ID

# Add tracks to the playlist if any URIs were found
if spotify_uris:
    sp.playlist_add_items(playlist_id, spotify_uris)  # Add all tracks to the playlist

# Pretty-print the created playlist details
pprint(playlist)
