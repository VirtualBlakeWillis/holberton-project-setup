from bs4 import BeautifulSoup
import json
import re
from markdownify import markdownify as md

from os import walk


def makeSoup(fileName):
  projectPage = open(f'./html/{fileName}')
  soup = BeautifulSoup(projectPage, "html.parser")
  return soup


  # Title - Project Title
  # <h2> Tasks - says Tasks
  # div.panel-heading h3.panel-title - Task Title
  # div.panel-body p - Task instructions
  # div.panel-body ul(first ul only) - Task requirements/notes
  # <pre><code> - example output code
  #div.list-group div ul (last child) - project file(s)

def grabFormattedTask(task):
  result = ''
  title = task.find('h3')
  instructions = task.find('p')
  requirements = task.find('ul')
  exampleCode = task.find('pre')
  ulList = task.find_all('ul')
  projFileList = ulList[-1]
  projectFile = projFileList.contents[-2]
  result += str(title).replace('\n', '')
  result += str(instructions)
  result += str(requirements)
  result += str(exampleCode)
  result += str(projectFile)
  result += '---\n'

  return (result)

def writeReadme(list, readmeTitle):
  result = '## Overview\n *insert overview here*\n## Tasks\n'
  for x in list:
    result += x
  
  readme = open(f'./output/{readmeTitle}', 'w')
  readme.write(md(result))

def findAllTasks(soup):
  tasks = soup.find_all('div', id=re.compile('^task-num'))
  formattedTasks = []
  for x in tasks:
    formattedTasks.append(grabFormattedTask(x))
  
  return formattedTasks


def main():
  # Get list of files in html
  filesList = next(walk('./html'), (None, None, []))[2]  # [] if no file

  for fileName in filesList:
    soup = makeSoup(fileName)
    title = soup.title.string
    readmeTitle = 'README ' + title + '.md'
    formattedTasks = findAllTasks(soup)
    writeReadme(formattedTasks, readmeTitle)

main()