import json
from proxmoxer import *
from termcolor import colored
import proxmoxer.backends
import urllib3
import os
import time

with open("config.json", "r") as config_file:
    config = json.load(config_file)


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to Proxmox API
proxmox = ProxmoxAPI(config["proxmox-address"], user=config["user"], password=config["password"], verify_ssl=config["ssl"])

# Get the list of all the nodes available from the connected node
nodes = proxmox.nodes.get()

# Define colors for the workload bar
WORKLOAD_COLORS = {
    0: 'green',
    50: 'yellow',
    75: 'red'
}

while True:
    # Clear the console before printing new information
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal_width = os.get_terminal_size().columns
    # Iterate through each node and print the containers and their status
    for node in nodes:

        # Get the node's current CPU and RAM usage
        node_stats = proxmox.nodes(node['node']).status.get()
        cpu_usage = node_stats['cpu'] * 100
        ram_usage = node_stats['memory']['used'] / node_stats['memory']['total'] * 100

        # Define the color for the CPU workload bar based on the CPU usage
        if cpu_usage < 50:
            cpu_workload_color = WORKLOAD_COLORS[0]
        elif cpu_usage < 75:
            cpu_workload_color = WORKLOAD_COLORS[50]
        else:
            cpu_workload_color = WORKLOAD_COLORS[75]

        # Define the color for the RAM workload bar based on the RAM usage
        if ram_usage < 50:
            ram_workload_color = WORKLOAD_COLORS[0]
        elif ram_usage < 75:
            ram_workload_color = WORKLOAD_COLORS[50]
        else:
            ram_workload_color = WORKLOAD_COLORS[75]

        # Print the node name as the title on the top center of the console
        title = f"{node['node']} - Containers and Workload"
        title_padding = " " * ((terminal_width - len(title)) // 2)
        print("\n" + title_padding + colored(title, "white", "on_blue"))

        print()

        # Print the CPU and RAM workload bars
        print(colored('{0: <5}'.format('CPU:'), 'white', 'on_blue'), end='')
        print(colored('[{0: <35}]'.format('|' * int(cpu_usage / 2.8)), cpu_workload_color), end='')
        print(colored(' {0:>4.1f}%'.format(cpu_usage), cpu_workload_color))

        print(colored('{0: <5}'.format('RAM:'), 'white', 'on_blue'), end='')
        print(colored('[{0: <35}]'.format('|' * int(ram_usage / 2.8)), ram_workload_color), end='')
        print(colored(' {0:>4.1f}%'.format(ram_usage), ram_workload_color))

        print()

        print(colored('{0: <10}'.format('ID'), 'white', 'on_grey'), end='')
        print(colored('{0: <20}'.format('Name'), 'white', 'on_grey'), end='')
        print(colored('{0: <15}'.format('Status'), 'white', 'on_grey'), end='')
        print(colored('{0: <18}'.format('Memory'), 'white', 'on_grey'), end='')
        print(colored('{0: <10}'.format('CPU'), 'white', 'on_grey'))
        print()
        containers = proxmox.nodes(node["node"]).lxc.get()
        sorted_containers = sorted(containers, key=lambda c: c["vmid"])
        for container in sorted_containers:
            vm_id = container['vmid']
            name = container['name']
            status = container['status']
            name_color = 'yellow' if name.startswith(('vm', 'CT')) else 'white'
            mem_used = container['maxmem'] - container['mem']
            mem_usage = f"{container['mem'] / 1024**3:.1f}/{container['maxmem'] / 1024**3:.1f} GB"
            cpu_usage = container['cpu'] * 100
            print(colored('{0: <10}'.format(vm_id), 'white', 'on_grey'), end='')
            print(colored('{0: <20}'.format(name), name_color), end='')
            print(colored('{0: <15}'.format(status), 'green' if status == 'running' else 'red', 'on_grey'), end='')
            print(colored('{0: <18}'.format(mem_usage), 'white', 'on_grey'), end='')
            print(colored('{0: <10}'.format(f"{cpu_usage:.1f}%"), 'white', 'on_grey'))

        print()
    time.sleep(2)