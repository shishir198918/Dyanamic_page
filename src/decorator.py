import time

def delay(intro):
    def delay1():
        time.sleep(5)
        intro()
    return delay1    

@delay
def intro():

    print("hi my name is khan ")

intro()  