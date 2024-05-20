import psutil
from os import kill
from time import sleep
from colorama import Fore
from signal import SIGTERM
from webbrowser import open

GAME_URL = "steam://rungameid/4000"
GAME_NAME = "hl2.exe"

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

WAIT_TIME = 5  #modify this for your pc

def main():
    times_open = 0
    for _ in range(1000):
        times_open += 1
        open_gmod(times_open)
        wait(WAIT_TIME)
        close_gmod(get_pid())

    print(GREEN + "COMPLETED")

def open_gmod(t: int):
    print(f"{GREEN} GAME OPEND {t}/1000{RESET}")
    open(GAME_URL)

def close_gmod(pid:int):
    print(RED + "GAME CLOSED" + RESET)
    kill(pid, SIGTERM)

def get_pid() -> int:
    for proc in psutil.process_iter():
        if GAME_NAME in proc.name():
            return proc.pid
        
def wait(time:int):
    print(YELLOW + "Waiting..." + RESET)
    sleep(time)

if __name__ == "__main__":
    main()