import importlib
from ..variables.variables import *
from ..utils.module_utils import *

class BackDoorGenerator(ModuleUtils):
    """
    The Generator class is responsible for managing the backdoor generation process.
    It provides a command-line interface for setting up the necessary parameters and
    generating the backdoor.
    """
    def __init__(self) -> None:
        """
        Constructor method for the Generator class.
        Initializes the ip, port and payload attributes.
        """
        super().__init__()
        self.module  = "backdoor"
        self.ip      = ""
        self.port    = ""
        self.payload = ""
    
    def run(self) -> None:
        """
        Runs the main command-line interface for setting up and generating the backdoor.
        Provides options for setting ip, port and payload, as well as
        displaying available payloads and generating the backdoor.
        """
        self.clear()
        
        print(f"""{COLOR['CYAN']}
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║*                          - BackDoor Generator -                        *║
            ╠═════════════════════════════════════╦════════════════════════════════════╣ 
            ║              Commands               ║            Function                ║    
            ╠═════════════════════════════════════╬════════════════════════════════════╣   
            ║ "set lhost <ip adress>"             : Set IP Adress.                     ║ 
            ║ "set lport <port>"                  : Set Port                           ║
            ║ "set payload" <payload name>        : Set Payload.                       ║ 
            ║ "show payloads"                     : Showing all Payloads.              ║ 
            ║ "generate"                          : Generate a Back Door.              ║
            ║ "back"                              : Back To Shypy.                     ║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*              LHOST                 : {COLOR['RESET']}{self.ip}{COLOR['CYAN']}{' ' *  (35 - len(self.ip))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*              LPORT                 : {COLOR['RESET']}{str(self.port)}{COLOR['CYAN']}{' ' *  (35 - len(str(self.port)))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             Payload                : {COLOR['RESET']}{self.payload}{COLOR['CYAN']}{' ' * (35 - len(self.payload))}║                                             
            ╠═════════════════════════════════════╩════════════════════════════════════╣            
            ║*                               - The Shypy -                            *║ 
            ╚══════════════════════════════════════════════════════════════════════════╝
            \n\n""")
        
        answer = input(f"{COLOR['CYAN']}Shypy >>{COLOR['RESET']} ").lower().strip()
        
        if answer.startswith("set lhost"):
            try:
                self.ip = answer.split(" ")[2]
                self.run() 
            
            except IndexError:
                self.write(message="set lhost <ip>", level=4, delay=1, clear=False)
                self.run()

        elif answer.startswith("set lport"):
            try:
                self.port = int(answer.split(" ")[2])
                self.run()
                    
            except IndexError:
                self.write(message="set lport <port>", level=4, delay=1, clear=False)
                self.run()
                
            except ValueError:
                self.write(message="Please enter integer type", level=4, delay=1, clear=False)
                self.run()
        
        elif answer.startswith("set payload"):
            try:
                self.payload = answer.split(" ")[2]
                self.run()
            
            except IndexError:
                self.write(message="set payload <payload name>", level=4, delay=1, clear=False)
                self.run()
        
        elif answer == "show payloads":
            self.list_payloads(self.module)

        elif answer == "generate":
            if self.ip == "" or self.port == "" or self.payload == "":
                self.write(message="Please fill in the required fields.", level=4, delay=1, clear=False)
                self.run()
            
            else:
                backdoor_name = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Name Of backdoor: ") + ".py"
                backdoor_icon = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Icon Of backdoor (Optional): ")
                
                self.pipeline(
                    module=self.module, payload=self.payload, ip=self.ip,
                    port=int(self.port), name=backdoor_name, icon_path=backdoor_icon)
                
                sys.exit(1)
            
        elif answer == "back":
            importlib.import_module("main").Shypy().menu()

        else:
            self.write(message="Invalid Option", level=4, delay=1, clear=False)
            self.run()