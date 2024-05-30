import socket

def dns_lookup(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Hostname not found"

if __name__ == "__main__":
    hostname = input("Enter a hostname to look up: ")
    result = dns_lookup(hostname)
    print("DNS Lookup for {hostname}: {result}")
