#!/usr/bin/python3


import requests

TIMEURL = "http://date.jsontest.com"

IPURL = "http://ip:jsontest.com"

VALIDURL = "http://validate.jsontest.com"

def main():

    resp  = requests.get(TIMEURL)


    mytime = resp.json()


    with open 
