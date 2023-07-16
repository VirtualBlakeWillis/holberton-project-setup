#!/usr/bin/env python3
"""
Setup project directory / Enviroment
Step 1: parse project page, set variables + create directory:
    - directory name
    - Project README.md
    - Project main files
    - Project task files
"""
from bs4 import BeautifulSoup
import mechanicalsoup
import requests
from markdownify import markdownify as mdify
import os
from getpass import getpass
import argparse
import re

from scripts.login import user_input, login
from scripts.page_obj_operations import get_proj_page, fixlinks
from scripts.directory_operations import make_dir, make_readme



def main():
    base_url = "https://intranet.hbtn.io/"
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        # user_agent='MyBot/0.1: mysite.example.com/bot_info',
    )
    username, password, proj_id = user_input()
    
    # Login to Intranet
    login(browser, username, password)
    # Retrieve project page
    page = get_proj_page(browser, proj_id)
    # Fix links
    new_page = fixlinks(base_url, page)
    # for item in page.find_all("a", href=True):
    #     if item["href"].startswith('/rltoken/'):
    #         print("intranet url: " + base_url + item["href"])
    #         try:
    #             browser.open(base_url + item["href"])
    #             resp = browser.url
    #             item["href"] = resp
    #         except:
    #             pass

    # getting each task 

    #for task in page.find_all("div", id=re.compile("^task-num-")):
    #    for item in task.find('li'):
    #        if item.string == "File: ":
    #            print(item.next_sibling.string)

    path = make_dir(page)
    make_readme(page, path)

    browser.close()

main()