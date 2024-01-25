import socket
import requests
import netifaces as ni

def get_default_gateway():
    """Get the default gateway IP address (usually the router's IP)."""
    gws = ni.gateways()
    return gws['default'][ni.AF_INET][0]

def get_router_info(ip):
    """Attempt to get information from the router's web interface."""
    try:
        response = requests.get(f"http://{ip}", timeout=5)
        return response.text
    except requests.RequestException as e:
        return str(e)

def main():
    router_ip = get_default_gateway()
    print(f"Router IP Address: {router_ip}")

    router_info = get_router_info(router_ip)
    print(f"Router Information: {router_info[:500]}")  # Print the first 500 characters

if __name__ == "__main__":
    main()
