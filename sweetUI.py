import time

def typing_print(text, end="\n",speed=1):
    for i in text:
        print(i,end="")
        time.sleep(0.1/speed)
        if i in "!.?":
            time.sleep(0.5/speed)
        if i in ",;":
            time.sleep(0.2/speed)
    print(end)