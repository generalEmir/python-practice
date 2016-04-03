import time

NUM_PLAYS = 5
MAX_FOOS = 10
MIN_FOOS = 1

print("Hello, welcome to the all new FOO restaurant! Foo is a special type of noodles.")
time.sleep(2)
responses = range(MIN_FOOS, MAX_FOOS)
numPlays = NUM_PLAYS
i = 0
while i < numPlays:
    i = i + 1
    answer = raw_input("SO Dude, how many orders of FOOs do ya want?")
    if int(answer) not in responses:
        print("CMON BRO!")
    else:
        print("OK DUDE, " + answer + " ,COMING RIGHT UP!!!!")
        foo = 0; 
        while (foo < int(answer)):
            print("foo now equals " + str(foo))
            foo = foo + 1                                
raw_input()


