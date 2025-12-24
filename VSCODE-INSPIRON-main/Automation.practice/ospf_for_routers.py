from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
import time

# Device information
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.54.132",
        "username": "admin",
        "password": "admin",
        "name": "R1"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.54.133",
        "username": "admin",
        "password": "admin",
        "name": "R2"
    }
]

# OSPF configuration commands
ospf_commands = [
    "router ospf 1",
    "network 192.168.54.0 0.0.0.255 area 0"
]

print("\n===== OSPF AUTOMATION SCRIPT STARTED =====\n")

# Loop through each device
for device in devices:
    print(f"🔹 Checking SSH access to {device['name']} ({device['ip']}) ...")

    try:
        # Attempt to connect to device
        connection = ConnectHandler(**device)
        print(f"✅ SSH connection established with {device['name']}")

        # (Optional) Get hostname to confirm device identity
        hostname = connection.find_prompt()
        print(f"Connected as: {hostname}")

        # Send OSPF configuration
        print(f"\n🚀 Configuring OSPF on {device['name']} ...")
        output = connection.send_config_set(ospf_commands)
        print(output)

        # Verify OSPF neighbor
        print(f"\n🔍 Verifying OSPF neighbors on {device['name']} ...")
        verify_output = connection.send_command("show ip ospf neighbor")
        print(verify_output)

        connection.disconnect()
        print(f"✅ Completed configuration for {device['name']}\n")
        time.sleep(2)

    except NetMikoTimeoutException:
        print(f"❌ Timeout: Unable to connect to {device['ip']} (SSH not reachable)")
    except NetMikoAuthenticationException:
        print(f"❌ Authentication failed for {device['ip']} (check username/password)")
    except Exception as e:
        print(f"⚠️ Unexpected error connecting to {device['ip']}: {str(e)}")

print("===== OSPF AUTOMATION SCRIPT COMPLETED =====\n")

