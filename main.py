import news
from time import sleep

TICK = 60

def main_update():
    while True:
        news.updae()
        sleep(TICK)

if __name__ == '__main__':
    main_update()