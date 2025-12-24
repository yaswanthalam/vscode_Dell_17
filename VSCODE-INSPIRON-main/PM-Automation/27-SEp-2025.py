from netmiko import ConnectHandler
import getpass

host =input("Enter Device IP adress: ")
username=input("Enter the user name")
password=getpass.getpass("Please enter your password ")


router={
    "device_type":"cisco_ios",
    "ip":host,
    "username":username,
    "password":password
}

connect=ConnectHandler(**router)

output=connect.send_command("show running-config")
output=connect.send_command("show ip interface brief")
output=connect.send_command("show startup-config")
print(output)

connect.disconnect()

