from typing import Final

import requests

"""
File that shortens any url given by user. This is achieved by using api from https://cutt.ly/api/api.php
To learn more from cutt.ly you can check the documentation -> https://cutt.ly/api-documentation/regular-api
"""

API_KEY: Final[str] = "aaa5f56268368e03c59c46c95968aaee6fcc1"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(complete_url: str):
    payload: dict = {"key": API_KEY, "short": complete_url}
    request = requests.get(BASE_URL, params=payload)

    data: dict = request.json()

    if url_data := data["url"]:
        if url_data["status"] == 7:
            print(f'shorter link -> {url_data["shortLink"]}')
        else:
            print(f'Error: {url_data["status"]}')


if __name__ == "__main__":
    while True:
        url: str = input("Enter the url you want to shorten (ctrl + C to exit): ")
        shorten_link(url)
        print()
