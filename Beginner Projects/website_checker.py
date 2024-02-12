import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(file_name: str) -> list:
    websites: list = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

    return websites


def get_user_agent():
    ua = UserAgent()
    return ua.chrome


def get_status_desc(status_code: int) -> str:
    for status in HTTPStatus:
        if status == status_code:
            desc: str = f'{status.value} {status.name}'
            return desc
    return 'Unknown status code'


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, {'User-Agent': user_agent}).status_code
        print(website, get_status_desc(code))
    except Exception:
        print(f'*** Could not get website : {website} ***')


if __name__ == '__main__':
    websites: list[str] = get_websites("websites.csv")
    for website in websites:
        check_website(website, get_user_agent())
