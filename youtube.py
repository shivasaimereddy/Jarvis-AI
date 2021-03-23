from urllib.request import urlopen
import urllib.parse
import webbrowser
from sys import platform
import os

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def youtube(textToSearch):
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.get('chrome').open_new_tab(url)


if __name__ == '__main__':
    youtube('any text')
