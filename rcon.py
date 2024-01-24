import valve.rcon

# Server details
SERVER_ADDRESS = ("your_server_ip", your_server_port)  # Replace with your server's IP and port
RCON_PASSWORD = "your_rcon_password"  # Replace with your RCON password
COMMAND = "status"  # Replace with the command you want to send

def send_rcon_command(server_address, password, command):
    try:
        with valve.rcon.RCON(server_address, password) as rcon:
            response = rcon(command)
            print(f"Sent command: {command}")
            print(f"Received response: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_rcon_command(SERVER_ADDRESS, RCON_PASSWORD, COMMAND)
