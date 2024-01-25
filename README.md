# Python-Based Server Manager for Palworld

<!-- Brief introduction -->
This document outlines the functionality and usage of a Python-based server manager designed for the Palworld game. The server manager is a comprehensive tool aimed at simplifying server setup, management, and maintenance for Palworld.

## Key Features:

<!-- List of major features -->
1. **Open Source and Easy to Download:** The program is fully open source and can be downloaded from the GitHub repository.

2. **Initial Setup Choices:**
   <!-- Options for initial setup -->
   - **Manage Existing Server:** If you have a server already installed, the program will ask for the root installation directory. Upon locating the server executable, it switches to the management interface (detailed below), importing all server settings except for launch parameters.
   - **Set Up New Server:** For new installations, the program offers a default installation location (C:\Gameservers) or allows you to choose a custom directory. The setup process includes:
     - Creating the directory structure.
     - Downloading and running SteamCMD from Valve to install and validate the Palworld server.
     - Opening a configuration window with default settings, including pre-filled local and public IP addresses, enabling customization of settings like ports and IPs.
     - Options to automatically apply firewall rules based on selected ports.
     - Suggesting optimal power plan settings to prevent server file corruption, such as disabling hard drive shutdown when idle.
     - A setup screen for initial server configurations (server name, passwords, difficulty settings, editing `palworldsettings.ini`).

3. **Additional Configuration Options:**
   <!-- Additional configuration details -->
   - **Backups:** Option to enable server backups, with settings for frequency and retention.
   - **Auto Restarts:** Ability to set up automatic server restarts and configure their frequency.
   - **Network Setup Assistance:** The program can identify your router’s manufacturer and guide you through port forwarding based on the brand.

4. **Overall Management Screen:**
   <!-- Description of the management screen -->
   - Displays CPU, RAM, and HDD usage.
   - Features start, restart, and stop buttons for server management.
   - Includes toggles for auto-restart, and options to launch the server as either a community or a private server.
   - Contains an RCON console for direct server interaction.

5. **Program Execution and Administration:**
   <!-- Information on program execution -->
   - The program will automatically request administrative rights if not started with them, ensuring full functionality for tasks like firewall and power plan adjustments.

## Current Status:

<!-- Update on the current development status -->
- The program is currently under heavy development. As such, it is in a preliminary phase, and users should expect that not all features may work correctly at this time.
- All individual components of the program are operational, but integration and bug fixing are ongoing.

---

<!-- Conclusion and future outlook -->
This server manager aims to streamline the process of running a Palworld server, making it accessible and manageable for users with varying levels of technical expertise. Users are encouraged to keep this in mind and stay updated with future developments and improvements.
