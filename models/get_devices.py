# from ansible.module_utils.basic import *
# from bs4 import BeautifulSoup
# import requests
# import urllib2
# import os
# import re
# import argparse


inventory = ['mx80',
'qfx5100',
'ex2300',
'ex4300',
'ex2200',
'ex3300',
'ex3400',
'ex4200',
'ex4550',
'ex4600',
'ex9204',
'ex9208',
'ex9251',
'jatp700',
'mx104',
'mx10k3',
'mx150',
'mx2020',
'mx204',
'mx240',
'mx480',
'mx960',
'nfx250',
'ptx10k8',
'ptx1k',
'ptx3k',
'ptx5k',
'qfx10k2-60c',
'qfx10k2-36q-72q',
'qfx10k8',
'qfx3500',
'qfx5110',
'qfx5200',
'qfx5210',
'srx1400',
'srx1500',
'srx210',
'srx220',
'srx240',
'srx320',
'srx3400',
'srx345',
'srx3600',
'srx4100',
'srx4200',
'srx4600',
'srx5400',
'srx550',
'srx5600',
'srx650',
'ex9214',
'vsrx',
'openconfig',
'acx500',
'acx5k'
]



for item in inventory:
    if item == "mx240" or item == "mx480" or item == "mx960":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/mx240_480_960/install_package \n".format(item))
        f.close()

    elif item == "ex2300" or item == "ex3400":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/ex2300-3400/install_package \n".format(item))
        f.close()

    elif item == "ex9204" or item == "ex9208" or item == "ex9214":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/ex9204-9208-9214/install_package \n".format(item))
        f.close()

    elif item == "ex2300" or item == "ex3400":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/ex2300-3400/install_package \n".format(item))
        f.close()

    elif item == "ptx3k" or item == "ptx5k":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/ptx3k-5k/install_package \n".format(item))
        f.close()

    elif item == "srx4100" or item == "srx4200":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/srx4100,4200/install_package \n".format(item))
        f.close()


    elif item == "srx300" or item == "srx320" or item == "srx340" or item == "srx345":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/SRX300%20Series/install_package \n".format(item))
        f.close()

    elif item == "qfx10k2-60c":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/qfx10k2-60c/install_package \n")
        f.close()

    elif item == "qfx10k2-36q-72q":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/qfx10k2-36q-72q/install_package \n")
        f.close()

    elif item == "qfx10k8":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/qfx10k8/install_package \n")
        f.close()

    elif item == "ptx10k8":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/ptx10k8/install_package_vmhost \n")
        f.close()

    elif item == "vsrx":
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/vSRX/vSRX \n")
        f.close()

    else:
        f= open('{0}.yml'.format(item), "w+")
        f.write("url: http://172.25.124.17/files/Software/{0}/install_package \n".format(item))
        f.close()
