#!/usr/bin/env python3
""" Python Learning | Author: kushkota2015@gmail.com """

import requests
import random
import time
import pyfiglet 


r = requests.get("https://official-joke-api.appspot.com/random_joke")
setUp = r.json().get("setup")
punchline = r.json().get("punchline")


def createRandomAPIRequest():


    var = requests.get("https://official-joke-api.appspot.com/random_joke")
    setUp = var.json().get("setup")
    punchline = var.json().get("punchline")
    print()
    print("Alligator asks: \t" + setUp)
    time.sleep(3)

    print("\n\tCrocodile is waiting for the punchline ...")
    time.sleep(3)

    # punchline = r.json().get("punchline")
    print("\n\n")
    print("Alligator replies: \t" + punchline)
    time.sleep(2)
    print("\n\tCrocodile is rolling in the floor laughing ...\n")
    time.sleep(1)
    print("Do you want to hear again? (Y /n)")
    #print(pyfiglet.figlet_format("",font"digital",justify="center"))
    playAgain = input()
    if playAgain == "Y" or playAgain == "y":
      
        createRandomAPIRequest()
        
    


        # print('''\nSee you later Alligator!
        #         After a while Crocodile!''')

# print(r.status_code) > 200
# print(type(r)) < class 'requests.models.Response' >

def showIntro():
    print()
    result = pyfiglet.figlet_format("Alligator and Crocodile", font="digital", justify= "center")

    print(result)

  

    print('''

    \t\t\tWecome to Florida SaltWater!

    Today, Alligator and Crocodile are having a little fun telling a joke.

    Are you ready to hear their interesting conversation? (Y / n) 
    ''')

showIntro()



user = input()

# def playerOption():
   

while user == "Y" or user == "y":
        print()
        
        # print(type(r.json)) < class 'method' >
        
        # setUp = r.json().get("setup")

        # print(type(setUp)) < class 'str' >

     
        print("Alligator asks: \t" + setUp)
        time.sleep(3)

        print("\n\tCrocodile is waiting for the punchline ...")
        time.sleep(3) 
    

        # punchline = r.json().get("punchline")
        print("\n\n")
        print("Alligator replies: \t"  + punchline)
        time.sleep(2)
        print("\n\tCrocodile is rolling in the floor laughing ...\n")
        time.sleep(2)
        

        print("\nDo you want to play again? (Y /n)")
       
        playAgain = input()

        # if playAgain == "y" or playAgain == "Y":
        if playAgain == "Y" or playAgain == "y":
            createRandomAPIRequest()
            break
        
            
       
               
        #    playerOption() 
        
            

print('''\n\n\nSee you later Alligator!
                After a while Crocodile!\n''')
        












