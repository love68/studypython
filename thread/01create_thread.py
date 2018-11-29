import threading
import time

def test():
    print("test")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=test)
        t.start()



