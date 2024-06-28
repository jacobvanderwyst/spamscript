import time
from pynput.keyboard import Key, Controller
delay = 5  # Delay in seconds
#outlog=open("timelog.txt", 'a')
print("Beginning a 5 second daley. click into the field you want to enter text in")
time.sleep(delay)

keyboard=Controller()
i=0
messagenum=0
timerun=0
spamdelayletter=.00001
messagesToSend=400
pauseexec=31
while messagenum<messagesToSend:
    word = f"amondrUnk {messagenum}"
    for letter in word:
        keyboard.tap(letter)
        time.sleep(spamdelayletter)
        timerun+=spamdelayletter
    keyboard.tap(Key.enter)
    time.sleep(.000001)
    timerun+=.0000001
    if i==99:
        i=0
        timerun+=pauseexec
        print(f"Sleeping for {pauseexec} seconds to evade spam detection")
        time.sleep(pauseexec)
    messagenum+=1
    i+=1
#outlog.write(f"Time elapsed: {timerun} seconds\n")