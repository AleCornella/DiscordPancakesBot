import keyboard
import time
import random
import threading


def highlow(stop_event):
    while not stop_event.is_set():
        List = ["high","low"]
        keyboard.write("p!highlow")
        time.sleep(0.1)
        keyboard.send("enter")
        time.sleep(1)
        keyboard.write(random.choice(List))
        time.sleep(0.1)
        keyboard.send("enter")
        time.sleep(0.2)
        keyboard.write("p!deposit all")
        time.sleep(0.1)
        keyboard.send("enter")
        stop_event.wait(30) #30

def work(stop_event):
    while not stop_event.is_set():
        keyboard.write("p!work")
        time.sleep(0.1)
        keyboard.send("enter")
        time.sleep(1)
        keyboard.write("p!deposit all")
        time.sleep(0.1)
        keyboard.send("enter")
        stop_event.wait(300) #300 12


def start():
    kill = threading.Event()
    w = threading.Thread(target=work, args=(kill,))
    hl = threading.Thread(target=highlow, args=(kill,))
    w.start()
    time.sleep(5)
    hl.start()
    return kill, w, hl

def stop(kill, w, hl):
    kill.set()
    w.join()
    hl.join()

if __name__ == '__main__':
    time.sleep(5)
    f, g, z = start()
    keyboard.wait('esc')
    stop(f, g, z)
    
