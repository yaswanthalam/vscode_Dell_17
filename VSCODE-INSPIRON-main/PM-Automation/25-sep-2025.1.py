from netmiko import ConnectHandler
import getpass

host = input("Enter Device IP address: ")
username = input("Enter the user name: ")
password = getpass.getpass("Please enter your password: ")

router = {
    "device_type": "cisco_ios",
    "ip": host,
    "username": username,
    "password": password
}

connect = ConnectHandler(**router)

output1 = connect.send_command("show running-config")
output2 = connect.send_command("show ip interface brief")
output3 = connect.send_command("show startup-config")

print("=== Running Config ===")
print(output1)
print("\n=== IP Interface Brief ===")
print(output2)
print("\n=== Startup Config ===")
print(output3)

connect.disconnect()
