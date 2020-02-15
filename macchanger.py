import subprocess
import optparse
import re


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface")
    parse_object.add_option("-m", "--mac", dest="mac_adress")
    ##(user_inputs,arguments)=parse_object.parse_args()
    return parse_object.parse_args()


def change_mac_adress(interface, mac_adress):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_adress])
    subprocess.call(["ifconfig", interface, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("MAC CHANGER FROM 4NY")
try:
    (user_inputs, arguments) = get_user_input()

    change_mac_adress(user_inputs.interface, user_inputs.mac_adress)

    final_mac = control_new_mac(user_inputs.interface)

    if final_mac == user_inputs.mac_adress:
        print("Mac Changed!")
    else:
        print("Error!")
except:
    print("TRY AGAIN\nAll Comands:\n    -i , --interface , -m ,--mac "
          "\nFor Example: \n    sudo python3 macchanger.py -i (eth0,wlan0) -m (ff:ff:ff:ff:ff:ff)")

##interface=user_inputs".interface bu iki islemi fonksiyon sayesinde yaptik
##mac_adress=user_inputs.mac_adress
##24:0a:64:b1:f3:95
##d8:50:e6:1c:f1:f8
##interface=input("interface:")
##mac_adress=input("Mac Adress:")
