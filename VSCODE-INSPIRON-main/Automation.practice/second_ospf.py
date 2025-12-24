from netmiko import ConnectHandler

# Define device information
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.54.132",
        "username": "admin",
        "password": "admin"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.54.133",
        "username": "cisco",
        "password": "cisco"
    }
]

# OSPF configuration commands
ospf_commands = [
    "router ospf 1",
    "network 192.168.54.0 0.0.0.255 area 0"
]

# Configure OSPF on each device
for index, device in enumerate(devices, start=1):
    name = f"R{index}"
    print(f"\nConnecting to {name} ({device['ip']}) ...")
    connection = ConnectHandler(**device)

    print(f"Entering configuration mode on {name}")
    output = connection.send_config_set(ospf_commands)
    print(output)

    # Save configuration to make it persistent
    print(f"Saving configuration on {name} ...")
    connection.save_config()

    # Verify OSPF neighbors
    print(f"Verifying OSPF on {name} ...")
    verify_output = connection.send_command("show ip ospf neighbor")
    print(verify_output)

    connection.disconnect()
    print(f"Configuration completed for {name}")

    

