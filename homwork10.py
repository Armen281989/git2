
import random
user_score = 0
computer_score = 0
choices = ("qar", "tuxt", "mkrat")
print("qar haxtum e mkratin. mkrat haxtum e txtin. tuxt haxtum e qarin.")
user = input("@ntreq qar, tuxt, mkrat kam durs gal? ")
while user != "durs gal":                 
    user = user.lower()             
    computer = random.choice(choices)   
    print("cer @ntrutyun " +user+ ", comp @ntrel e " +computer+ ".")
    if user == computer:
        print("havasar")
    elif user == "qar":
        if computer == "mkrat":
            print("duq haxteciq!")
            user_score = user_score + 1
        else:
            print("haxtec comp!")
            computer_score = computer_score + 1
        print ("hashiv: duq uneq ", user_score, "comp hashiv ", computer_score)
    elif user == "tuxt":
        if computer == "qar":
            print("duq haxteciq!")
            user_score = user_score + 1
        else:
            print("haxtec comp!")
            computer_score = computer_score + 1
        print ("hashiv: duq uneq ", user_score, "comp hashiv ", computer_score)
    elif user == "mkrat":
        if computer == "tuxt":
            print("duq haxtel eq!")
            user_score = user_score + 1
        else:
            print("haxtec comp!")
            computer_score = computer_score + 1
        print ("hashiv: duq uneq ", user_score, "comp hashiv ", computer_score)
    else:
        print("error...")
    print()                             
    user = input("qar,tuxt, mkrat, kam durs gal ? ")	