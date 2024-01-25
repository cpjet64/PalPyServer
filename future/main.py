version = 1.0

# this file will do the following
# use the firstlaunch.py to check for previously installed versions
#
#     if previous version is installed then check registry version against the latest version on github
#         and if out of date then use update.py to update to the latest version on github
#         and if not out of date then ask user if they want to change any settings
#             if not then use servermanagergui.py to open the main server manager window
#             if user wants to change any settings then use the configure function in servermanagergui.py
#
#     if previous version is not installed then check main.py version against the latest version on github
#         and if out of date then use update.py to update to the latest version on github
#         and if not out of date then use installer.py to install the program to $programfiles and set a registry value
#             equal to the version in main.py
