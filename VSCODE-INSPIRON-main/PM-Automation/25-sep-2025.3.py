from netmiko import ConnectHandler
import getpass

Router1 = "192.168.213.139"
Router2 = "192.168.213.140"
#Router3 = "192.168.236.133"

Routers = [Router1, Router2]

username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

for router in Routers:

    device_details = {
        'device_type':'cisco_ios',
        'ip':router,
        'username':username,
        'password':password
    }

    ssh = ConnectHandler(**device_details)

    show_route = ssh.send_command("show ip route")
    print(f"\n=== Routing Table for {router} ===\n{show_route}\n")

    ssh.disconnect()