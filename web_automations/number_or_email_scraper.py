# Note: Website to test scraping -> https://www.randomlists.com/
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Final

# Regex used for finding e-mails in text
EMAIL_REGEX: Final[
    str
] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Regex used for finding phone numbers in text
PHONE_REGEX: Final[str] = r"""\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"""

# Regex for phone numbers in different formats
# PHONE_REGEX: Final[str] = (
#     r"""\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|
# 2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|
# 4[987654310]|3[9643210]|2[70]|7|1)
# \W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*\d\W*(\d{1,2})$"""
# )
# PHONE_REGEX: Final[str] = r"""\(\d{3}\)\s\d{3}-\d{4}$"""


class Browser:
    def __init__(self) -> None:
        print("Starting up browser...")
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")

        self.browser = webdriver.Chrome(options=self.chrome_options)

    def scrape_emails(self, url: str) -> set | None:
        print(f"Scraping {url} for emails...")
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_emails.add(re_match.group())

        if list_emails == set():
            return
        return list_emails

    def scrape_phone_numbers(self, url: str) -> set | None:
        print(f"Scraping {url} for phone numbers...")
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_phones: set = set()
        for re_match in re.finditer(PHONE_REGEX, page_source):
            list_phones.add(re_match.group())

        if list_phones == set():
            return
        return list_phones


def ask_user(browser):
    choice: str = ""
    while choice not in ["1", "2"]:
        choice = input(
            """
            Choose from the following options:
                    (1) email scraping
                    (2) phone scraping
            """
        )
        if choice in ["1", "2"]:
            break
        else:
            print("Wrong input (valid inputs are 1 and 2)")

    url: str = input("Input the url to scrape =>")
    if choice == "1":
        return browser.scrape_emails(url)
    elif choice == "2":
        return browser.scrape_phone_numbers(url)


if __name__ == "__main__":
    browser = Browser()
    answers = ask_user(browser)

    if answers:
        for i, answer in enumerate(answers, start=1):
            print(i, answer, sep=":  ")
    else:
        print("No items scraped")
