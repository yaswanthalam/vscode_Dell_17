from netmiko import ConnectHandler
import getpass

hostname =input("Enter Device IP adress: ")
username=input("Enter the user name")
password=getpass.getpass("Please enter your password ")


router={
    "device_type":"cisco_ios",
    "ip":hostname,
    "username":username,
    "password":password
}

connect=ConnectHandler(**router)

commands=[
    "interface loopback 0",
    "ip address 1.1.1.1 255.255.255.255",
    ##"no shutdown"
    "do show ip interface brief"
]

output=connect.send_config_set(commands)
print(output)
connect.disconnect()