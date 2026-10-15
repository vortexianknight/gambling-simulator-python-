import random
import os

tokens = 125
while True:
    gambleq = input("gamble for 1 token?(Y/N/B/R)")

    if gambleq == "y":
        if tokens == 0:
            print ("you are a broke ass nigga now,go get a job!")
        else:
            tokens = tokens - 1
            aftermath = random.randint(1,100)
            if aftermath == 5:
                print ("you winned the gambling! now you have 100 free tokens as a price!")
                tokens = tokens + 100
            else:
                print ("youve lost...")
    else:
          if gambleq == "b":
            if tokens >= 1:
              print (f"your balance is {tokens}.remember,once you loose it all there is no way back!")
            else:
                print("youre broke dude,go get a job")
    
    if gambleq == "r":
        if tokens >= 1:
            print("dude,youre quite rich! why would you reset? reset is only avaible at 0 tokens!")

        else:
            os.system("cls")
                    
