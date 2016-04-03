import time

acceptables = ['frostbite', '', 'Frostbite','Frost bite']
while True:
    answer = raw_input("What do you get when you cross a snowman with a vampire?")

    if (answer == "I don't know"):
        print("FROSTBITE!!! LOLOLOLOL!!!!")
        break
    elif answer not in acceptables:
        print("Try again!")
    else:
        print("LOL, " + answer + " , WAS THAT FUNNY? HAHAHAHA!! LOL")
        break

raw_input()

