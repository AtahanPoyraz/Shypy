import platform

COLOR = {
    'RESET'     : '\033[0m',
    'BLACK'     : '\033[0;30m',
    'RED'       : '\033[0;31m',
    'BLUE'      : '\033[0;34m',
    'MAGENTA'   : '\033[0;35m',
    'WHITE'     : '\033[0;37m',
    'GREEN'     : '\u001b[32;1m',
    'YELLOW'    : '\u001b[33;1m',
    'CYAN'      : '\u001b[36;1m',
}

OS = platform.system().lower()

LIBS = [
    "pynput", 
    "cv2", 
    "pyautogui", 
    "cryptography", 
    "simplejson", 
    "pyarmor", 
    "mouse", 
    "mouseinfo", 
    "requests", 
    "win32gui"
    ]