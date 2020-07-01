#!/usr/bin/python3


import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"

def main():

    got_charToLookup = input("What is the name of the character we should lookup? " )

    gotresp = requests.get(AOIF_CHAR + "?name=" + got_charToLookup)

    got_dj = gotresp.json()

    print(got_dj)
    print(f"The character {got_charToLookup} has the URL: {got_dj[0]['url']}")



if __name__ == "__main__":
    main()
