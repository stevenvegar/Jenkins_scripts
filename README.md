# Jenkins_scripts
Some scripts to enumerate and attack Jenkins servers

## Reverse shells
These scripts are ported from a Metasploit exploit written in Ruby.\
[Jenkins 2.150.2 - Remote Command Execution (Metasploit)](https://www.exploit-db.com/exploits/46352)

### [win_revshell_cmd.py](win_revshell_cmd.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Powershell base64** encoded payload.\
This script use the **"Execute Windows batch command"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [win_revshell_nodejs.py](win_revshell_nodejs.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **NodeJS script** payload.\
This script use the **"Execute NodeJS script"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [win_revshell_groovy.py](win_revshell_groovy.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Groovy script** payload.\
This script use a **"Pipeline script"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [linux_revshell_cmd.py](linux_revshell_cmd.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **Bash base64** encoded payload.\
This script use the **"Execute shell"** job type.\
Tested on Jenkins 2.150.2 installed on Ubuntu Server 22.04.3 LTS

### [linux_revshell_nodejs.py](linux_revshell_nodejs.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **NodeJS script** payload.\
This script use the **"Execute NodeJS script"** job type.\
Tested on Jenkins 2.150.2 installed on Ubuntu Server 22.04.3 LTS

### [linux_revshell_groovy.py](linux_revshell_groovy.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **Groovy script** payload.\
This script use a **"Pipeline script"** job type.\
Tested on Jenkins 2.150.2 installed on Ubuntu Server 22.04.3 LTS
