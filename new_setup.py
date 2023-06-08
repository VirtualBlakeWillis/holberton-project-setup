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


def user_input():
    """
    Get user input, return username, password, project id
    """
    #username = input("Please enter your Intranet username: ")
    #password = getpass("Please enter your Intranet password: ")
    #proj_id = input("Please enter the project ID: ")
    username = "4931@holbertonstudents.com"
    password = ""
    proj_id = ""
    return username, password, proj_id

def login(browser, username, password):
    url_login = "https://intranet.hbtn.io/auth/sign_in"
    browser.open(url_login)

    browser.select_form('form[action="/auth/sign_in"]')
    browser["user[login]"] = username
    browser["user[password]"] = password

    resp = browser.submit_selected()

def get_proj_page(browser, proj_id):
    url_proj = "https://intranet.hbtn.io/projects/" + proj_id
    browser.open(url_proj)
    page = browser.get_current_page()
    return page

def save_page(page):
    """
    Save project page to file
    """
    proj_file = open("project.html", "w")
    proj_file.write(str(page))
    # open(page, "w").write(resp.html.prettify())
    proj_file.close()

def get_proj_title(soup):
    proj_title = soup.title(string=True)[0].split(" - ")[0]
    return proj_title

def get_proj_desc(soup):
    proj_desc = soup.find("div", {"id": "project-description"})
    return proj_desc

def make_readme(soup, path):
    proj_readme = open(path + '/README.md', "w")
    desc = get_proj_desc(soup)
    title = get_proj_title(soup)
    proj_readme.write("# " + mdify(str(title)) + "\n\n")
    proj_readme.write(mdify(str(desc)))

def make_dir(soup):
    proj_dir = soup.find(string="Directory: ").next_sibling.string
    path = os.getcwd() + "/" + proj_dir
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    
    return path

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


    for item in page.find_all("a", href=True):
        if item["href"].startswith('/rltoken/'):
            # print("intranet url: " + base_url + item["href"])
            try:
                browser.open(base_url + item["href"])
                resp = browser.url
                item["href"] = resp
            except:
                pass
            # print(item["href"])
            # print("browser open response: " + resp)

    #for task in page.find_all("div", id=re.compile("^task-num-")):
    #    for item in task.find('li'):
    #        if item.string == "File: ":
    #            print(item.next_sibling.string)
    path = make_dir(page)
    make_readme(page, path)
    #save_page(page)

    # desc = get_proj_desc(page)
    browser.close()
    # proj_html = get_proj_file()
    # soup = make_soup(proj_html)
    # path = make_dir(soup)
    # os.chdir(path)
    # make_readme(soup)
main()






#delete this
def get_proj_file():
    proj_path = input("Project page: ")
    proj_file = open(proj_path, "r")
    proj_html = proj_file.read()
    proj_file.close()   
    return proj_html

def make_soup(proj_html):
    soup = BeautifulSoup(proj_html, 'html.parser')
    return soup

