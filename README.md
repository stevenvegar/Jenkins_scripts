# Jenkins_scripts
Some scripts to enumerate and attack Jenkins servers

## Enumeration

### [enum_access.py](enum_access.py/)
This script can enumerate 26 different URLs and check if the user can access them.\
If no user is especified, it will try perform authentication as the anonymous user.

### [enum_users.py](enum_users.py/)
This can be used to perform a dictionary attack to obtain possible usernames.\
Either if Jenkins is configured to use local user database or Active Directory.

## CVE-2024-23897

### [win_creds_CVE-2024-23897.py](win_creds_CVE-2024-23897.py/)
This script can download hudson.util.Secret and master.key without Anonymous Overall/Read permissions.\
If access is available, also retrieve credentials from the credentials.xml file and decrypt the passwords.\
Works on Jenkins installed on Windows.

### [init_pass_CVE-2024-23897.py](win_init_pass_CVE-2024-23897.py/)
This script can retrieve the initialAdminPassword which is used when Jenkins is installed.\
The password should work to login, if it is was not changed after installation.\
Anonymous Overall/Read permissions are not necessary.

### [rce_CVE-2024-23897.py](rce_CVE-2024-23897.py/)
This script search for user's credentials and execute a Groovy script with the desired OS command.\
Anonymous Overall/Read permissions are necessary.

### [revshell_CVE-2024-23897.py](revshell_CVE-2024-23897.py)
This script search for user's credentials and create a JOB to execute a reverse shell.\
Anonymous Overall/Read permissions are necessary.

## Reverse shells
These scripts are ported from a Metasploit exploit written in Ruby.\
[Jenkins 2.150.2 - Remote Command Execution (Metasploit)](https://www.exploit-db.com/exploits/46352)

### [win_revshell_cmd.py](win_revshell_cmd.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Powershell base64** encoded payload.\
This script use the **"Execute Windows batch command"** job type.

### [win_revshell_nodejs.py](win_revshell_nodejs.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **NodeJS script** payload.\
This script use the **"Execute NodeJS script"** job type.

### [win_revshell_groovy.py](win_revshell_groovy.py/)
Get a Powershell reverse shell from Windows-based Jenkins server using a **Groovy script** payload.\
This script use a **"Pipeline script"** job type.

### [linux_revshell_cmd.py](linux_revshell_cmd.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **Bash base64** encoded payload.\
This script use the **"Execute shell"** job type.

### [linux_revshell_nodejs.py](linux_revshell_nodejs.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **NodeJS script** payload.\
This script use the **"Execute NodeJS script"** job type.

### [linux_revshell_groovy.py](linux_revshell_groovy.py/)
Get a Bash reverse shell from Linux-based Jenkins server using a **Groovy script** payload.\
This script use a **"Pipeline script"** job type.


## External resources
[HackTricks - Boitatech](https://hacktricks.boitatech.com.br/pentesting/pentesting-web/jenkins)\
[Github - Carlos Polop](https://github.com/carlospolop/hacktricks-cloud/tree/master/pentesting-ci-cd/jenkins-security)\
[Github - Jenkins Attack Framework](https://github.com/Accenture/jenkins-attack-framework)\
[Github - Pwn-Jenkins](https://github.com/gquere/pwn_jenkins)
