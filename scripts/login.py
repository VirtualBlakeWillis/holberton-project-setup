#!/usr/bin/env python3
""" module handles user input and login """
from getpass import getpass
import argparse
import os



def user_input():
    """
    Get user input, return username, password, project id
    """
    # parser = argparse.ArgumentParser(description='Setup project directory')
    # parser.add_argument('-u', '--username', help='Intranet username')
    # parser.add_argument('-p', '--password', help='Intranet password')
    # parser.add_argument('-i', '--project_id', help='Project ID')
    # args = parser.parse_args()
    username = os.getenv('USERNAME')
    print(username)
    password = os.getenv('PASSWORD')
    project_id = os.getenv('PROJECT_ID')

    if not username:
        username = input("Please enter your Intranet username: ")
    if not password:
        password = getpass("Please enter your Intranet password: ")
    if not project_id:
        project_id = input("Please enter the project ID: ")

    return username, password, project_id

def login(browser, username, password):
    url_login = "https://intranet.atlasschool.com/auth/sign_in"
    browser.open(url_login)

    browser.select_form('form[action="/auth/sign_in"]')
    browser["user[login]"] = username
    browser["user[password]"] = password

    resp = browser.submit_selected()
    print(resp)
