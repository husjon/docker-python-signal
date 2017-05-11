import signal
import time

i = 0
running = True


def sigterm(x, y):
    global running
    print '[python] SIGTERM received, time to leave.'
    running = False
    # exit()

# Register the signal to the handler
signal.signal(signal.SIGTERM, sigterm)  # Used by this script


# A simple loop
def loop():
    global i
    print "[python] Hello, %s" % i
    i += 1
    time.sleep(1)

if __name__ == '__main__':
    print '[python] Started, waiting for SIGTERM'
    while True:
        if running:
            loop()
        else:
            break

    print '[python] Bye...'
