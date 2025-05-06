from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'your_password',
}

# Establish SSH connection
net_connect = ConnectHandler(**device)

# Send command
output = net_connect.send_command('show ip int brief')
print(output)

# Send configuration
config_commands = [
    'interface loopback0',
    'ip address 10.10.10.1 255.255.255.0',
]
net_connect.send_config_set(config_commands)

net_connect.disconnect()
