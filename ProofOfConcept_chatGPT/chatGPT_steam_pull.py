import requests
import json
import csv

# Replace YOUR_STEAM_ID with the Steam ID of the user
steam_id = "YOUR_STEAM_ID"

# Set the API endpoint URL
endpoint = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

# Set the API parameters
params = {"key": "YOUR_API_KEY", "steamid": steam_id, "format": "json"}

# Make the API request
response = requests.get(endpoint, params=params)

# Parse the response as JSON
data = response.json()

# Get the list of games from the response
games = data["response"]["games"]

# Open a CSV file for writing
with open("games.csv", "w", newline="") as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(["Game", "Playtime", "Achievements", "Unlocked"])
    
    # Iterate through the list of games
    for game in games:
        # Get the game's name, playtime, and achievement data
        name = game["name"]
        playtime = game["playtime_forever"]
        achievements = game["achievements"]
        num_achievements = achievements["total"]
        num_unlocked = achievements["unlocked"]
        
        # Check if the game has any playtime
        if playtime > 0:
            # Write the game data to the CSV
            writer.writerow([name, playtime, num_achievements, num_unlocked])