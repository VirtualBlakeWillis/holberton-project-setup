#!/usr/bin/env python3
""" placeholder """

import mechanicalsoup


def get_proj_page(browser, proj_id):
    url_proj = "https://intranet.hbtn.io/projects/" + proj_id
    browser.open(url_proj)
    page = browser.get_current_page()
    return page

def get_proj_title(soup):
    proj_title = soup.title(string=True)[0].split(" - ")[0]
    return proj_title

def get_proj_desc(soup):
    proj_desc = soup.find("div", {"id": "project-description"})
    return proj_desc


def fixlinks(base_url, page):
    """
    Find all links that start with /rltoken/ and replace with full url
    """
    base_url = "https://intranet.hbtn.io"
    for item in page.find_all("a", href=True):
        if item["href"].startswith('/rltoken/'):
            print("intranet url: " + base_url + item["href"])
            try:
                browser.open(base_url + item["href"])
                resp = browser.url
                item["href"] = resp
            except:
                pass
    return page