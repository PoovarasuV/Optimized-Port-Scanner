import socket
import threading
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # timeout for faster scanning
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            with lock:
                print(Fore.GREEN + f"[OPEN] {ip}:{port}")
        
        sock.close()
    except:
        pass

def scan_target(ip, start_port, end_port):
    print(Fore.CYAN + f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def main():
    parser = argparse.ArgumentParser(description="Optimized Python Port Scanner")
    parser.add_argument("targets", help="Target IP(s), comma separated")
    parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000)", default="1-1000")
    
    args = parser.parse_args()

    targets = args.targets.split(",")
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    for target in targets:
        scan_target(target.strip(), start_port, end_port)

if __name__ == "__main__":
    main()

