import pyautogui as pg
import time

# Constants
WAIT_TIME = 3

pg.hotkey('win', 'r')
pg.write('chrome')
pg.press('enter')


COORDINATES = [ 
    (1078 , 397),   
    (321, 84)      
]


def search(url, query):
    for x, y in COORDINATES:
        pg.moveTo(x, y)
        pg.click()
        time.sleep(1)
    
    pg.write(url)
    pg.press('enter')
    time.sleep(WAIT_TIME)

    pg.moveTo(654, 150)
    pg.click()
    pg.write(query, interval=0.1)
    pg.press('enter')

def play_video():
    time.sleep(WAIT_TIME)
    pg.moveTo(671, 813)
    pg.doubleClick()


time.sleep(WAIT_TIME) 
search("youtube.com", "best part")
play_video()
