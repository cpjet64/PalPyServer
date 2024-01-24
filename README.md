# PalPyServer
Python based server manager for Palworld

so this program will handle everything basically. the process is as follows:
download the program (fully open source) from my github
run the program
the program will initially ask you if you want to manage a already installed server or setup a new one
if you select manage a server it will ask where the root install directory is for the gameserver and then upon locating the server exe it will change to the overall management screen (explained later) and all of your server settings except for launch parameters will be imported automatically
OR
if you select setup a new one the program will ask where you want the program installed to or ask if you want to use the default location of C:\Gameservers
it will create the directory structure
it will download steamcmd from valve
it will run steamcmd to install and validate the palworld server
it will open a configuration window that is prefilled with default settings allowing people to configure them as needed (change ports or ips etc) (it will also prefill your local IP as well as your public IP)
it will then ask if you want it to automatically apply the firewall rules based on the ports you selected in the previous section
it will then ask you if you want to apply optimal power plan settings such as disabling hard drive shutdown when idle to help avoid server file corruption
it will then open a initial server setup screen where you fill out your server info and configs such as the name and passwords and change the palworldsettings.ini values and can easily change the difficulty presets
it will then prompt if you want to enable backups for your server and if so open a config window for setting how often backups occur, how many backups to keep
it will then prompt if you want to enable auto restarts for your server and if so open a config window for setting how often
it will then take your local computers gateway ip and try to read the webpage login page to determine what manufacturer made it and direct you to the proper port forwarding guide for the brand
it will then change to the overall management screen that shows cpu, ram, hdd usage data and start restart stop buttons, there is also a autorestart toggle, it will also include a toggle box for launching the server as a community server or as a private server
on the overall management screen there is also a RCON console that will connect to the configured server
so far i have all of the individual parts working properly i just need to iron out a few bugs and integrate them all into one program
also almost forgot to add the program will auto elevate to administrator if it wasnt started as admin so it has the ability to do everything listed like firewall and power plan
