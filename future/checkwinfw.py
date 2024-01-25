import ctypes
import subprocess
import sys
import re


def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """Elevate the privileges."""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )


def check_firewall_for_program(programs):
    """Check for firewall rules related to specific programs."""
    try:
        # Fetch all firewall rules
        rules_output = subprocess.check_output(
            "netsh advfirewall firewall show rule name=all", shell=True, text=True
        )

        for program in programs:
            if program in rules_output:
                rule_names = re.findall(r"Rule Name:\s+(.*?)\r?\n", rules_output)
                for rule in rule_names:
                    if program in subprocess.check_output(
                        f'netsh advfirewall firewall show rule name="{rule}"',
                        shell=True,
                        text=True,
                    ):
                        print(f"Found a firewall rule related to {program}: {rule}")
            else:
                print(f"No firewall rule found for {program}.")

    except subprocess.CalledProcessError:
        print("Failed to fetch firewall rules.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_firewall_for_ports(ports):
    """Check for firewall rules related to specific ports."""
    try:
        # Fetch all firewall rules
        rules_output = subprocess.check_output(
            "netsh advfirewall firewall show rule name=all", shell=True, text=True
        )

        for port in ports:
            if str(port) in rules_output:
                rule_names = re.findall(r"Rule Name:\s+(.*?)\r?\n", rules_output)
                for rule in rule_names:
                    if str(port) in subprocess.check_output(
                        f'netsh advfirewall firewall show rule name="{rule}"',
                        shell=True,
                        text=True,
                    ):
                        print(f"Found a firewall rule for port {port}: {rule}")
            else:
                print(f"No firewall rule found for port {port}.")

    except subprocess.CalledProcessError:
        print("Failed to fetch firewall rules.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    programs = ["PalServer.exe", "palserver-win64-test.exe"]
    ports = [8211, 27015]

    if is_admin():
        check_firewall_for_program(programs)
        check_firewall_for_ports(ports)
    else:
        print("Not running as administrator. Trying to elevate privileges...")
        run_as_admin()


if __name__ == "__main__":
    main()
