import threading
import time
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread=threading.Thread(target=sing,args=("python",))
    dance_thread=threading.Thread(target=dance,kwargs={"msg":"java"})
    sing_thread.start()
    dance_thread.start()

