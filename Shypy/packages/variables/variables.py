import os
import platform

FLAG : str = "Shypy >> "

PARENT_FOLDER = os.path.abspath("")

OS : str = platform.system().lower()

V = 1.0

MODULES = [
    {"NAME" : "Keylogger Generator",        "OS" : ["Windows", "Linux", "MacOS"]},
    {"NAME" : "Ransomware Generator",       "OS" : ["Windows", "Linux", "MacOS"]},
    {"NAME" : "Camera Recorder Generator",  "OS" : ["Windows", "Linux", "MacOS"]},
    {"NAME" : "Screen Recorder Generator",  "OS" : ["Windows", "Linux", "MacOS"]},
    {"NAME" : "BackDoor Generator",         "OS" : ["Windows", "Linux", "MacOS"]},
]

LIBS = {
    "pynput"       :  "pynput", 
    "cv2"          :  "opencv-python", 
    "pyautogui"    :  "pyautogui", 
    "cryptography" :  "cryptography", 
    "simplejson"   :  "simplejson", 
    "pyarmor"      :  "pyarmor", 
    "mouse"        :  "mouse", 
    "mouseinfo"    :  "mouseinfo", 
    "requests"     :  "requests", 
    "pywin"        :  "pywin32",
    "PyInstaller"  :  "pyinstaller"
}

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

BANNER = f"""{COLOR["CYAN"]}
            ████████████████████████████████████████████████████████████████████████████╗
            ╚══██╔══════════════════════════════════════════════════════════════════════╝
               ██║  ██╗  ██╗  ███████╗     ██████╗  ██╗  ██╗  ██╗  ██╗  ██████═╗ ██╗  ██╗ 
               ██║  ██╚══██║  ██╔════╝    ██╔════╝  ██╚══██║  ██╚══██║  ██╔══██║ ██╚══██║
               ██║  ███████║  ███████╗    ╚██████═╗ ███████║  ╚██████║  ██████╔╝ ╚██████║
               ██║  ██╔══██║  ██╔════╝     ╚════██║ ██╔══██║   ╚═══██║  ██╔═══╝   ╚══╗██║
               ██║  ██║  ██║  ███████╗    ███████╔╝ ██║  ██║  ██████╔╝  ██║          ║██║
               ╚═╝  ╚═╝  ╚═╝  ╚══════╝    ╚══════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═╝         ╔███║
               ████████████████████████████████████████████████████████████████████████╔╝
               ╚═══════════════════════════════════════════════════════════════════════╝\n
{COLOR["RESET"]}"""