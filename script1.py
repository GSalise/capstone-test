from netmiko import ConnectHandler

device = {
    	'device_type': 'cisco_ios',
    	'host': '192.168.10.1',
	'username': 'admin',
	'password': 'cisco',
	'secret': 'cisco',
}

# Establish SSH connection
net_connect = ConnectHandler(**device)

net_connect.enable()

numofSUB = int(input("How many subints do you want to make?: "))


for x in range(1, numofSUB):
	sub_int = x * 10
	output = net_connect.send_config_set(
		[
		f"int f0/0.{sub_int}",
		f"encapsulation dot1Q {sub_int}",
		f"ip add 192.168.{sub_int}.1 255.255.255.0",
		"exit",
		]
	)
	print(output)

net_connect.disconnect()
