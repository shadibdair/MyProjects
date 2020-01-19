# This file will have two fumction
import webbrowser
from Utils import SCORES_FILE_NAME


import pandas as pd
import requests
from bs4 import BeautifulSoup


app_url = 'http://localhost:8080/'


def test_scores_service(app_url):
    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(app_url)

    # content = ''
    # try:
    #     # try to read the scores file
    #     file = open(SCORES_FILE_NAME, 'r+')
    #     content = file.read()
    #     file.seek(0)
    # except FileNotFoundError:
    #     print(EOFError)
    # # get scores
    # if len(content) >= 0 and len(content) <= 1000:
    #     try:
    #         score = int(content)
    #     except ValueError:
    #         score = 0
    #
    # # Return if the score between 0 to 1000.
    # if score >= 0 and score <= 1000:
    #     print(0)
    # else:
    #     print(-1)

    url = 'http://localhost:8080/'
    page = requests.get(url)
    #print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')

    Rating = []
    for rate in soup.select('[id=score]'):
        Rating.append(rate.get_text())

    for i in range(0, len(Rating)):
        Rating[i] = int(Rating[i])
        ans = Rating[i]

    print(Rating)
    rng = range(0, 1000)
    if 0 <= ans and 1000 >= ans:
        print(0)
    else:
        print(-1)

def main_function():
    test_scores_service(app_url)


if __name__ == '__main__':
    main_function()