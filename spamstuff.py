import time
from pynput.keyboard import Key, Controller
import random

def getWord(wordlist):
    return random.choice(wordlist)
delay = 5  # Delay in seconds
#outlog=open("timelog.txt", 'a')
print("This will send 400 messages\nBeginning a 5 second daley. click into the field you want to enter text in")
time.sleep(delay)

keyboard=Controller()
i=0
messagenum=0
timerun=0
spamdelayletter=.00001
messagesToSend=400
pauseexec=31
wordlist=["amondrOp", "amondrUnk","amondrIq", "amondrOH", "amondrEady", "amondrUgs", "amondrIve", "amondrEst", "amondrIzz","amondrWut", "amondrEason","amondrInk","amondrEam","<3"]
while messagenum<messagesToSend:
    word = getWord(wordlist)
    for letter in word:
        keyboard.tap(letter)
        time.sleep(spamdelayletter)
        timerun+=spamdelayletter
    keyboard.tap(Key.enter)
    time.sleep(.000000001)
    timerun+=.000000001
    if i==99:
        i=0
        timerun+=pauseexec
        print(f"99 messages sent. Sleeping for {pauseexec} seconds to evade spam detection")
        time.sleep(pauseexec)
    messagenum+=1
    i+=1
#outlog.write(f"Time elapsed: {timerun} seconds\n")