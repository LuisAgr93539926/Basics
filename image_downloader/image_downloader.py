import os
import urllib.request

import requests


def get_extension(url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    for extension in extensions:
        if extension in url:
            return extension


def download_image(url: str, file_name: str, folder: str = None):
    extension = get_extension(url)
    if extension:
        if folder:
            path: str = f'{folder}/{file_name}{extension}'
        else:
            path: str = f'{file_name}{extension}'
    else:
        raise Exception('No exception found...')

    if os.path.isfile(path):  # Check if name already exists
        raise Exception(f'File already exists ({path})')

    # Download image
    try:
        image_content: bytes = requests.get(url).content
        with open(path, 'wb') as image:
            image.write(image_content)
            print(f'Downloaded {file_name} succesffuly in {path}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    url: str = input('Enter a URL to download -> ')
    name: str = input('Enter a name for the image -> ')
    print('\nDownloading...')
    download_image(url, name, 'images')