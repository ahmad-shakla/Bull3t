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
=======>>   2.Create a php payload
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
        
        
install()
banner()
