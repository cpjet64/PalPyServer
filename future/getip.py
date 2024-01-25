import socket
import netifaces as ni
import requests


def get_local_ip():
    """Get the local IP address of the computer."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def get_gateway():
    """Get the default gateway IP address."""
    gws = ni.gateways()
    default_gateway = gws['default'][ni.AF_INET][0]
    return default_gateway


def get_public_ip():
    """Get the public IP address."""
    try:
        response = requests.get('https://api.ipify.org')
        public_ip = response.text
        return public_ip
    except requests.RequestException:
        return "Error: Unable to get public IP"


def main():
    local_ip = get_local_ip()
    gateway = get_gateway()
    public_ip = get_public_ip()

    print(f"Local IP Address: {local_ip}")
    print(f"Gateway IP Address: {gateway}")
    print(f"Public IP Address: {public_ip}")


if __name__ == "__main__":
    main()
