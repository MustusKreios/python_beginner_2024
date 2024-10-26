import pyautogui as pg
import time

# Constants
WAIT_TIME = 3
URL = "youtube.com"
SEARCH_QUERY = "ninong ry"

# Coordinates
COORDINATES = {
    "chrome_icon": (365, 74),
    "search_bar": (654, 186),
    "video_play_button": (671, 813)
}

# Helper Functions
def open_chrome():
    """Opens Chrome via Run command."""
    pg.hotkey('win', 'r')
    pg.write('chrome')
    pg.press('enter')
    time.sleep(WAIT_TIME)

def navigate_to_url(url):
    """Navigates to the specified URL."""
    pg.moveTo(*COORDINATES["chrome_icon"])
    pg.click()
    time.sleep(1)
    pg.write(url)
    pg.press('enter')
    time.sleep(WAIT_TIME)

def search_query(query):
    """Searches for the query in the search bar."""
    pg.moveTo(*COORDINATES["search_bar"])
    pg.click()
    pg.write(query, interval=0.1)
    pg.press('enter')

def play_video():
    """Starts playing the video."""
    time.sleep(WAIT_TIME)
    pg.moveTo(*COORDINATES["video_play_button"])
    pg.doubleClick()

# Main Workflow
def main():
    open_chrome()
    navigate_to_url(URL)
    search_query(SEARCH_QUERY)
    play_video()

if __name__ == "__main__":
    main()
