#!/usr/bin/python

from ansible.module_utils.basic import *
from bs4 import BeautifulSoup
import requests
import urllib2
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Retreive url')
parser.add_argument('-u', nargs='+', action="store", dest="url", type=str)
parser.add_argument('-v', nargs='+', action="store", dest="version", type=str)

cli_args = parser.parse_args()

url = cli_args.url[0]
version = cli_args.version[0]
ext = 'tgz'

def listFD(url, ext=''):
    page = requests.get(url).text
    # print page
    soup = BeautifulSoup(page, 'html.parser')
    print ([url + '/' + node.get('href') for node in soup.find_all('a', href=re.compile(version)) if node.get('href').endswith(ext)])[0].split("/")[-1]

def main():
    try:
        listFD(url, ext)
    except IndexError:
        print "Software Package not located on FTP Server. Please upload software package and run script again. Exiting Script..."

if __name__ == "__main__":
    main()
