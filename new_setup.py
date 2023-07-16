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


# def user_input():
#     """
#     Get user input, return username, password, project id
#     """
#     parser = argparse.ArgumentParser(description='Setup project directory')
#     parser.add_argument('-u', '--username', help='Intranet username')
#     parser.add_argument('-p', '--password', help='Intranet password')
#     parser.add_argument('-i', '--project_id', help='Project ID')
#     args = parser.parse_args()
#     username = args.username
#     password = args.password
#     project_id = args.project_id

#     if not username:
#         username = input("Please enter your Intranet username: ")
#     if not password:
#         password = getpass("Please enter your Intranet password: ")
#     if not project_id:
#         project_id = input("Please enter the project ID: ")

#     return username, password, project_id

# def login(browser, username, password):
#     url_login = "https://intranet.hbtn.io/auth/sign_in"
#     browser.open(url_login)

#     browser.select_form('form[action="/auth/sign_in"]')
#     browser["user[login]"] = username
#     browser["user[password]"] = password

#     resp = browser.submit_selected()

# def get_proj_page(browser, proj_id):
#     url_proj = "https://intranet.hbtn.io/projects/" + proj_id
#     browser.open(url_proj)
#     page = browser.get_current_page()
#     return page

# def get_proj_title(soup):
#     proj_title = soup.title(string=True)[0].split(" - ")[0]
#     return proj_title

# def get_proj_desc(soup):
#     proj_desc = soup.find("div", {"id": "project-description"})
#     return proj_desc

# def make_readme(soup, path):
#     proj_readme = open(path + '/README.md', "w")
#     desc = get_proj_desc(soup)
#     title = get_proj_title(soup)
#     proj_readme.write("# " + mdify(str(title)) + "\n\n")
#     proj_readme.write(mdify(str(desc)))

# def make_dir(soup):
#     proj_dir = soup.find(string="Directory: ").next_sibling.string
#     path = os.getcwd() + "/" + proj_dir
#     try:
#         os.mkdir(path)
#     except OSError:
#         print ("Creation of the directory %s failed" % path)
    
#     return path

# def fixlinks(base_url, page):
#     """
#     Find all links that start with /rltoken/ and replace with full url
#     """
#     for item in page.find_all("a", href=True):
#         if item["href"].startswith('/rltoken/'):
#             # print("intranet url: " + base_url + item["href"])
#             try:
#                 browser.open(base_url + item["href"])
#                 resp = browser.url
#                 item["href"] = resp
#             except:
#                 pass

# def main():
#     base_url = "https://intranet.hbtn.io/"
#     browser = mechanicalsoup.StatefulBrowser(
#         soup_config={'features': 'lxml'},
#         raise_on_404=True,
#         # user_agent='MyBot/0.1: mysite.example.com/bot_info',
#     )
#     username, password, proj_id = user_input()
    
#     # Login to Intranet
#     login(browser, username, password)
#     # Retrieve project page
#     page = get_proj_page(browser, proj_id)
#     # Fix links
#     fixlinks(base_url, page)


#     # getting each task 

#     #for task in page.find_all("div", id=re.compile("^task-num-")):
#     #    for item in task.find('li'):
#     #        if item.string == "File: ":
#     #            print(item.next_sibling.string)

#     path = make_dir(page)
#     make_readme(page, path)

#     browser.close()

# main()
