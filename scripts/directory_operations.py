#!/usr/bin/env python3
""" placeholder """

import os
import mechanicalsoup
from bs4 import BeautifulSoup
from markdownify import markdownify as mdify
from scripts.page_obj_operations import *


def make_readme(soup, path):
    proj_readme = open(path + '/README.md', "w")
    desc = get_proj_desc(soup)
    title = get_proj_title(soup)
    proj_readme.write("# " + mdify(str(title)) + "\n\n")
    proj_readme.write(mdify(str(desc)))

def make_dir(soup):
    proj_dir = soup.find(string="Directory: ").next_sibling.string
    path = os.getcwd() + "/" + proj_dir

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)

    return path