#!/usr/bin/env python

import requests
import urllib3
import sys
import time

print(""" 

     _______. __    __  .______    _______   ______   .___  ___.      ___       __  .__   __. 
    /       ||  |  |  | |   _  \  |       \ /  __  \  |   \/   |     /   \     |  | |  \ |  | 
   |   (----`|  |  |  | |  |_)  | |  .--.  |  |  |  | |  \  /  |    /  ^  \    |  | |   \|  | 
    \   \    |  |  |  | |   _  <  |  |  |  |  |  |  | |  |\/|  |   /  /_\  \   |  | |  . `  | 
.----)   |   |  `--'  | |  |_)  | |  '--'  |  `--'  | |  |  |  |  /  _____  \  |  | |  |\   | 
|_______/     \______/  |______/  |_______/ \______/  |__|  |__| /__/     \__\ |__| |__| \__| 
 
                                        ┌─┐┬ ┌┐┌┌┬┐┌─┐┬─┐
                                        ├┤ │ │││ ││├┤ ├┬┘
                                        └  ┴ ┘└┘─┴┘└─┘┴└─
                                                                                               
\n """)

string = "Coded By Ashpak pinjaree"
new_string = string.center(100, '-')
version = " 2.2"
new_version = version.center(100, '-')
instagram = " https://www.instagram.com/ashpak.pinjari/"
new_instagram = instagram.center(100,'-')
print("author: ", new_string)
print("version: ", new_version)
print("instagram: ", new_instagram)

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True,  help='target domain')
    parser.add_argument('-o', '--output', type=str, required=False, help='output file.')
    return parser.parse_args()

#parse host from scheme, to use for certificate transparency abuse

def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print(" [+] Invalid domain name, try without http or https for example: example.com...")
        sys.exit(1)
    return host

def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        fp.close()


def main():

    subdomains = []      

    args = parse_args()
    target = parse_url(args.domain)
    output = args.output

    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

    if req.status_code != 200:
        print(' [+] informatin is not available !')
        sys.exit(1)

    for (key,value) in enumerate(req.json()):
        subdomains.append (value['name_value'])

    print(f"\n [!] ********* TARGET: {target}  ****** [!] \n")

    subs = sorted(set(subdomains))

    for s in subs:
        print(f'[*] {s}\n')
        if output is not None:
               write_subs_to_file(s, output)
    print("\n\n[**] subdomain finding is commpleted, possible subdomain founded")        

if __name__=="__main__":
       main()