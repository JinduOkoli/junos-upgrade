#!/usr/bin/python

from ansible.module_utils.basic import *
from bs4 import BeautifulSoup
from itertools import izip
import requests
import urllib2
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Retreive model')
parser.add_argument('-m', nargs='+', action="store", dest="model", type=str)

cli_args = parser.parse_args()
mod = cli_args.model[0]
if '-' in mod:
    model = (mod.split('-'))[0].lower()
else:
    model = mod.lower()


url = 'https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476&actp=METADATA'

def ex_series(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    ex_series = (soup.find(class_='jTable', id ='Ja')).find_all('td')
    return ex_series

def acx_series(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    acx_series = (soup.find(class_='jTable', id ='Jb')).find_all('td')
    return acx_series

def mx_ptx_series(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    mx_ptx_series = (soup.find(class_='jTable', id ='Jc')).find_all('td')
    return mx_ptx_series

def srx_series(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    srx_series = (soup.find(class_='jTable', id ='Je')).find_all('td')
    return srx_series

def qfx_series(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    qfx_series = (soup.find(class_='jTable', id ='Jd')).find_all('td')
    return qfx_series

#get text from tags from first and second column
def strip_tags(series):
    table = []
    for i, v in enumerate(series):
        if i in range(0,len(series)):
            table.append(v.get_text())
        elif i in range(1,len(series)):
            table.append(v.get_text())
        else:
            table.append(v)
    return table


def call_table(url_table):
    # strip third column
    if 'ex' in model or 'qfx' in model:
        table_data = [v for i, v in enumerate(url_table) if i not in range(2,len(url_table),3)]
    # strip third and fourth column
    else:
        table_1= [v for i, v in enumerate(url_table) if i not in range(2,len(url_table),4)]
        table_data = [w for i, w in enumerate(table_1) if i not in range(2,len(table_1),3)]

    # convert list to dictionary
    table_list = iter(table_data)
    table_dict = dict(izip(table_list, table_list))

    # get jtac_version
    for key in table_dict:
        if model in key.lower():
            jtac_version = table_dict[key]
            break
    else:
        if 'mx' in model:
            jtac_version = table_dict['MX Series']

        elif 'ptx' in model:
            jtac_version = table_dict['PTX Series']

        elif 'acx' in model:
            jtac_version = 'Junos 17.3R3'

    jtac_mod = jtac_version.strip('Junos ')

    if '/' in jtac_mod:
        jtac_mod_1 = jtac_mod.split('/')
        if 'S' in jtac_mod_1[0]:
            return (jtac_mod_1[1]).strip()
        elif 'S' in jtac_mod[1]:
            return (jtac_mod_1[0]).strip()
        else:
            return (jtac_mod_1[0]).strip()
    elif ' ' in jtac_mod:
        jtac_mod_2 = jtac_mod.split(' ')
        return (jtac_mod_2[0]).strip()
    else:
        return (jtac_mod).strip()

def main():
    if 'acx' in model:
        url_table = acx_series(url)
        print call_table(strip_tags(url_table))

    elif 'ex' in model:
        url_table = ex_series(url)
        print call_table(strip_tags(url_table))

    elif 'mx' in model:

        url_table = mx_ptx_series(url)
        print call_table(strip_tags(url_table))

    elif 'ptx' in model:
        url_table = mx_ptx_series(url)
        print call_table(strip_tags(url_table))

    elif 'srx' in model:
        url_table = srx_series(url)
        print call_table(strip_tags(url_table))

    elif 'qfx' in model:
        url_table = qfx_series(url)
        print call_table(strip_tags(url_table))


if __name__ == '__main__':
    main()
