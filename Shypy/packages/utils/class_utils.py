import os
import sys
import time
import datetime
import importlib
from itertools import cycle

from ..variables.variables import *

class Utils:
    """
    Utility class containing helper methods.
    """
    
    def clear(self) -> None:
        """
        Clears the terminal screen.

        This method detects the operating system and uses appropriate
        commands to clear the terminal screen.

        Returns:
            None
        """
        try:
            if OS.lower() == "windows":
                os.system("cls")
            
            else:
                os.system("clear")
                
        except KeyboardInterrupt:
            self.write(message="Exited from Shypy.", level=2, clear=True)
            sys.exit(1)
            
    def module_exist(self, module : str) -> bool:
        """
            Check if a module exists.

            This inner function checks if a given module exists.

            Args:
                module (str): The name of the module to check.

            Returns:
                bool: True if the module exists, False otherwise.
            """
        try:
            importlib.import_module(module)
            return True
        
        except ImportError:
            return False
    
    def write(self, message : str, level : int, delay : float = 0, clear : bool = False) -> None:
        """
        Prints a message with a specified level.

        This method takes a message and a level as input and prints the
        message with color formatting based on the specified level.
        delay (float, optional): Delay in seconds before printing the message. Defaults to 0.
        clear (bool, optional): Whether to clear the screen before printing the message. Defaults to False.

        Args:
            message (str): The message to be printed.
            level (int): The level of the message.
            
        Returns:
            None
            
        Note:
            The color of the message depends on the specified level:
            - Level 1 : Green
            - Level 2 : Cyan
            - Level 3 : Magenta
            - Level 4 : Yellow
            - Level 5 : Red
        """
        if clear:
            self.clear()
        
        match level:
            case 1:
                print(f"{COLOR["GREEN"]}[+]{COLOR["RESET"]} {message}")
        
            case 2:
                print(f"{COLOR["CYAN"]}[*]{COLOR["RESET"]} {message}")
                
            case 3:
                print(f"{COLOR["MAGENTA"]}[?]{COLOR["RESET"]} {message}")
                
            case 4:
                print(f"{COLOR["YELLOW"]}[!]{COLOR["RESET"]} {message}")
                
            case 5:
                print(f"{COLOR["RED"]}[x]{COLOR["RESET"]} {message}")
                
        time.sleep(delay)
        
    def auto_install(self, libraries : list[str]) -> None:
        """
        Installs missing requirements.

        Args:
            libraries (list[str]): Missing libraries list.
            
        Returns:
            None
        """
        self.write(message="Loading requirements please be patient.", level=1)
        for lib in libraries:
            os.system(f"pip install {lib}")
    
    def check_modules(self) -> None:
        """
        Checks for required modules and installs missing ones if needed.

        This method checks for the presence of required modules listed in the `LIBS` variable.
        If any required module is missing, it prompts the user to install them using `pip`.
        If all required modules are already installed, it notifies the user accordingly.

        Returns:
            None
        """
        def loader() -> None:
            """
            Display loading animation while checking for required modules.

            This inner function displays a loading animation while the check for required
            modules is in progress.

            Returns:
                None
            """
            try:
                self.clear()
                i : int = 0
                for c in cycle(["⢎⡰", "⢎⡡", "⢎⡑", "⢎⠱", "⠎⡱", "⢊⡱", "⢌⡱", "⢆⡱"]):
                    sys.stdout.write(f'\r{COLOR["CYAN"]}{FLAG}{COLOR["RESET"]}| {datetime.datetime.now().strftime("%H:%M:%S")} | Checking Requirements..{COLOR["CYAN"]} {c} {COLOR["RESET"]}\t')
                    sys.stdout.flush()
                    time.sleep(0.07)
                    i += 1

                    if i == len(LIBS) * 5:
                        break
                    
                    else:
                        continue
                    
            except (KeyboardInterrupt):
                self.write(message="Exited from Shypy.", level=2, clear=True)
                sys.exit(1)

        try:
            loader()
            self.clear()
            missing_libs : list[str] = [module for module in list(LIBS.keys()) if not self.module_exist(module)]
            missing_list : list[str] = [LIBS[lib] for lib in missing_libs] 
                
            if missing_libs:
                self.write(message=f"The following libraries are missing: {', '.join(missing_list)}", level=4)
                self.write(message=f"Please run {COLOR['YELLOW']}'pip install -r requirements.txt'{COLOR['RESET']} or {COLOR['YELLOW']}'pip install {', '.join(missing_list)}'{COLOR['RESET']}", level=2)
                try:
                    self.write(message="Auto-install the requirements [y/n]\n", level=3)
                    choice = input(f"{COLOR["CYAN"]}Shypy >> {COLOR["RESET"]}").lower().strip()
                    
                    if choice == "y":
                        self.clear()
                        self.auto_install(libraries=missing_list)
                        
                    else:
                        self.clear()
                        self.write(message="You need to install the required libraries to continue.", level=5)
                        sys.exit(1)
                
                except EOFError:
                    self.write(message="Exited from Shypy.", level=2, clear=True)
                    sys.exit(1)
                
                except KeyboardInterrupt:
                    self.write(message="Exited from Shypy.", level=2, clear=True)
                    sys.exit(1)
                
            else:
                self.write(message="All required requirements are already installed.", level=1)
                time.sleep(1)

        except KeyboardInterrupt:
            self.write(message="Exited from Shypy.", level=2, clear=True)
            sys.exit(1)