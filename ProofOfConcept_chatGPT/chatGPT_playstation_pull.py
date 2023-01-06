import requests
from bs4 import BeautifulSoup

# Set the URL for the Playstation login page
login_url = 'https://auth.api.sonyentertainmentnetwork.com/login.do'

# Set the URL for the Playstation games list page
games_url = 'https://www.playstation.com/en-us/my/games/'

# Set the login credentials
payload = {
    'j_username': 'YOUR_USERNAME',
    'j_password': 'YOUR_PASSWORD'
}

# Create a session to store the login cookies
with requests.Session() as session:
    # Send a POST request to the login page with the login credentials
    response = session.post(login_url, data=payload)

    # If the login was successful, send a GET request to the games list page
    if response.status_code == 200:
        games_page = session.get(games_url)

        # Parse the games list page HTML with Beautiful Soup
        soup = BeautifulSoup(games_page.text, 'html.parser')

        # Find all the elements with the 'div' tag and the 'game-tile' class
        game_tiles = soup.find_all('div', {'class': 'game-tile'})

        # Iterate through the game tiles and extract the game title and platform
        for tile in game_tiles:
            title = tile.find('div', {'class': 'title'}).text
            platform = tile.find('div', {'class': 'platform'}).text
            print(f'Title: {title}\nPlatform: {platform}\n---')
    else:
        print('Login failed')
