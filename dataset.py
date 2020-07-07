#!/usr/bin/python

"""

http://zetcode.com/python/prettytable/

"""

import requests
import json
from prettytable import PrettyTable


# print(response.status_code) >>> 200 all good

# print(response.content)
# print(response) >>> <Response [200]>

# print(response.json())
# This gets the same data as command (response.content)

# print(json.dumps(response.json()["teams"], indent=2))  


def main():
    
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
    
    
    #print("\nNational Hockey League contains following teams: \n")
    
    # teams = response.json()["teams"]
    # print(type(teams)) <class 'list'>
    
    # print(len(response.json()["teams"])) >>> 31
    
    

    x = PrettyTable()
    x.field_names = ["Name", "Conference", "Division"]
    
    for team in response.json()["teams"]:
        
                # val = team.get("shortName"),team["conference"]["name"],team["division"]["name"]
                # print(type(val)) >>> <class 'tuple'>
            
            
                # print(type(team.get("shortName"))) >>> <class 'string'>
                
        x.add_row([team.get("shortName"),team["conference"]["name"],team["division"]["name"]])
                
        x.sortby = "Conference"
                
        x.sortby = "Division"
                
        print(x)
                
    #print()

    
    
main()
