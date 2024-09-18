def outer(func):
    def inner():
        print("start")
        func()
        print("end")
    return inner


@outer
def sleep():
    import random
    import time
    print("sleeping")
    time.sleep(random.randint(1,5))

sleep()
# fn=outer(sleep)
# fn()
