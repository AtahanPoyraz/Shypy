import platform

COLOR = {
    'BLACK': '\033[0;30m',
    'RED': '\033[0;31m',
    'GREEN': '\u001b[32;1m',
    'YELLOW': '\u001b[33;1m',
    'BLUE': '\033[0;34m',
    'MAGENTA': '\033[0;35m',
    'CYAN': '\u001b[36;1m',
    'WHITE': '\033[0;37m',
    'RESET': '\033[0m'
}

OS = platform.system().lower()

LIBS = ["pynput", "cv2", "pyautogui", "cryptography", "simplejson", "pyarmor", "mouse", "mouseinfo", "requests", "win32gui"]