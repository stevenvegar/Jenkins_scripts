# Jenkins_scripts
Some scripts to enumerate and attack Jenkins servers

### [win_revshell_cmd.py](win_revshell_cmd.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Powershell base64** encoded payload.\
This script uses the **"Execute Windows batch command"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [win_revshell_nodejs.py](win_revshell_nodejs.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **NodeJS script** payload.\
This script uses the **"Execute NodeJS script"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [win_revshell_groovy.py](win_revshell_groovy.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Groovy script** payload.\
This script uses a **"Pipeline script"** job type.\
Tested on Jenkins 2.150.2 installed on Windows 10 Pro 22H2 b.19045

### [linux_revshell_groovy.py](linux_revshell_groovy.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **Groovy script** payload.\
This script uses a **"Pipeline script"** job type.\
Tested on Jenkins 2.150.2 installed on Ubuntu Server 22.04.3 LTS
