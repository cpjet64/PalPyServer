import subprocess
import re
import tkinter as tk
from tkinter import messagebox

def run_command(command):
    """Run a command in the Windows command line."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    return result.stdout.strip()

def get_current_power_plan():
    """Get the name and GUID of the currently active power plan."""
    active_plan = run_command("powercfg /GETACTIVESCHEME")
    match = re.search(r'Power Scheme GUID: ([\w-]+)  \((.*)\)', active_plan)
    if match:
        return match.group(1), match.group(2)
    else:
        raise Exception("Active power plan not found")

def create_power_plan(base_plan_guid, new_plan_name):
    """Create a new power plan based on an existing plan."""
    output = run_command(f"powercfg /DUPLICATE SCHEME {base_plan_guid}")
    new_plan_guid = re.search(r'Power Scheme GUID: ([\w-]+)  \(.*\)', output).group(1)
    run_command(f"powercfg /CHANGE {new_plan_guid} /name \"{new_plan_name}\"")
    return new_plan_guid

def set_active_power_plan(plan_guid):
    """Set a power plan as active."""
    run_command(f"powercfg /SETACTIVE {plan_guid}")

def prompt_user_and_set_plan(new_plan_guid, new_plan_name):
    """Prompt the user and set the power plan based on their choice."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    if messagebox.askyesno("Change Power Plan", "The recommended power plan is not currently active. Do you want to apply the 'Server Hosting' plan?"):
        set_active_power_plan(new_plan_guid)
        messagebox.showinfo("Power Plan Changed", f"'{new_plan_name}' is now the active power plan.")
    root.destroy()

def main():
    recommended_guids = ["8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c", "e9a42b02-d5df-448d-aa00-03f14749eb61"]
    new_plan_name = "Server Hosting"
    base_plan_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"

    try:
        current_plan_guid, current_plan_name = get_current_power_plan()

        if current_plan_guid not in recommended_guids:
            new_plan_guid = create_power_plan(base_plan_guid, new_plan_name)
            prompt_user_and_set_plan(new_plan_guid, new_plan_name)
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Power Plan Status", f"The currently active power plan is '{current_plan_name}'.")
            root.destroy()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
