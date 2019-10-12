import os 
import sys
from sys import platform
from time import sleep

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

def logo():
    if len(sys.argv) < 2:
        os.system("clear || cls")
        sys.stdout.write(RED + """
        888       888 8888888888    8888888           .d888         8888888888 d8b               888                  
        888   o   888 888             888            d88P"          888        Y8P               888                  
        888  d8b  888 888             888            888            888                          888                  
        888 d888b 888 8888888         888   88888b.  888888 .d88b.  8888888    888 88888b.   .d88888  .d88b.  888d888 
        888d88888b888 888             888   888 "88b 888   d88""88b 888        888 888 "88b d88" 888 d8P  Y8b 888P"   
        88888P Y88888 888      888888 888   888  888 888   888  888 888        888 888  888 888  888 88888888 888     
        8888P   Y8888 888             888   888  888 888   Y88..88P 888        888 888  888 Y88b 888 Y8b.     888     
        888P     Y888 888           8888888 888  888 888    "Y88P"  888        888 888  888  "Y88888  "Y8888  888                                                                                                       
        """  + END+LightBlue+'WF-InfoFinder'.format(RED, END).center(93) +
        '\n' + '\tMade ^_^ by: {}Mighty Ghost Hack'.format(YELLOW, RED, YELLOW, LightBlue).center(114) +
        '\n' + '\tVersion: {}1.0{}\n'.format(YELLOW, END).center(118) + '\n')
    else:
        sys.exit('Usage: python WF-InfoFinder.py')
        os.system("clear || cls")

def main():
    platform_output = check_system()
    os.system('cmd: cols=125 lines=30')
    logo()
    check_os_animation()
    print(LightCyan+"[√] "+YELLOW+"You are running on "+platform_output+" Machine, Everything is Perfect!!!"+END)
    sleep(5)
    os.system('cmd: cols=125 lines=30')
    while True:       
        logo()
        output = menu()
        opt = None
        if(str(type(output)) == "<class 'list'>"):
            opt = output[1]
            output = int(output[0])
        if(output == 1):
            list_of_available_SSIDs(opt=opt)
        elif (output == 2):
            list_of_profile(opt=opt)
        elif (output == 3):
            list_of_blocked_APs(opt=opt)
        elif (output == 4):
            current_interface(opt=opt)
        elif (output == 5):
            gen_full_report(opt=opt)
        elif (output == 6):
            shoW_clear_password(opt=opt)
        elif (output == 7):
            print(""+END,end="")
            sys.exit(0)
        else:
            print(LightCyan+"\n[x] "+RED+"Enter wrong field :( ")
            input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)


def check_system():
    os.system('color')
    if platform == "linux" or platform == "linux2":
        result = YELLOW+"[!] "+RED+"You are running on Linux Machine. \n"+YELLOW+"[!]"+RED+" Please run the application on Windows machine."+END
    elif platform == "darwin":
        result = YELLOW+"[!] "+RED+"You are running on MAC Machine. \n"+YELLOW+"[!]"+RED+" Please run the application on Windows machine."+END
    elif platform == "win32":
        return "Windows"
    print(result)
    sys.exit()

def check_os_animation():
    print(LightCyan+"[+] "+YELLOW+"Wait for few moments its looking for ur system"+END)
    print(LightCyan+"[+] "+YELLOW+"Checking ==> ",end="")
    words = RED+"█████████████"
    for char in words:
        print(char, end='', flush=True)
        sleep(0.5)
    print(END)

def menu():
    print(LightCyan+"[?] "+YELLOW+"What do you want to perform ?\n"+END)
    print(LightCyan+"[1] "+YELLOW+"List of Available SSID"+END)
    print(LightCyan+"[2] "+YELLOW+"List Wireless Profiles"+END)
    print(LightCyan+"[3] "+YELLOW+"List of Blocked Wireless Access Points"+END)
    print(LightCyan+"[4] "+YELLOW+"Current Wireless Interface (Including SNR)"+END)
    print(LightCyan+"[5] "+YELLOW+"Generate Full Report"+END)
    print(LightCyan+"[6] "+YELLOW+"Show Cleartext Passwords"+END)
    print(LightCyan+"[7] "+YELLOW+"Exit\n"+END)
    output = input(LightCyan+"[+] "+YELLOW+"Select your options : ").lower()
    if('--save' in output):
        return output.split()
    return int(output.strip())

def list_of_profile(opt=None):
    if(opt!=None):
        os.popen('netsh wlan show profiles >> profile.txt')
        print(LightCyan+"[√] "+YELLOW+"Profile text file has been generated"+END)
    else:
        p = os.popen('netsh wlan show profiles')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

def current_interface(opt=None):
    if(opt!=None):
        os.popen('netsh wlan show interfaces >> Interface_info.txt')
        print(LightCyan+"[√] "+YELLOW+"Interface info text file has been generated"+END)
    else:
        p = os.popen('netsh wlan show interfaces')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

def list_of_available_SSIDs(opt=None):
    if(opt!=None):
        os.popen('netsh wlan show networks >> networks.txt')
        print(LightCyan+"[√] "+YELLOW+"Networks text file has been generated"+END)
    else:
        p = os.popen('netsh wlan show networks')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

def list_of_blocked_APs(opt=None):
    if(opt!=None):
        os.popen('netsh wlan show filters >> blocked.txt')
        print(LightCyan+"[√] "+YELLOW+"Blocked text file has been generated"+END)
    else:
        p = os.popen('netsh wlan show filters')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

def gen_full_report(opt=None):
    if(opt!=None):
        os.popen('netsh wlan show all >> Full_Report.txt')
        print(LightCyan+"[√] "+YELLOW+"Full report text file has been generated"+END)
    else:
        p = os.popen('netsh wlan show all')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

def shoW_clear_password(opt=None):
    p = os.popen('netsh wlan show profiles')
    print(p.read()+"\n")
    access_point = input(LightCyan+"[+] "+YELLOW+"Enter wifi profile name from above list : ").strip()
    if(opt!=None):
        os.popen('netsh wlan show profiles '+access_point+' key=clear >> clear_password.txt')
        print(LightCyan+"[√] "+YELLOW+"Clear password text file has been generated"+END)
    else:
        p =  os.popen('netsh wlan show profiles '+access_point+' key=clear')
        print(p.read())
    input(LightCyan+"[+] "+YELLOW+"Press enter key to continue :) "+END)

if __name__ == "__main__":
    main()
    

