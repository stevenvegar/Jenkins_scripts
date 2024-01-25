## enum_access.py
The user access or authentication in Jenkins can be made by many ways, here is a brief:

**Security Realm:**\
This is the authentication mechanism, where Jenkins asks if a user is allowed to log in. Can be one of the following:\
**- Delegate to servlet container**\
Use the servlet container to authenticate users, as per defined by the servlet spec. This is historically what Jenkins has been doing up to 1.163.\
**- Jenkins own userd database**\
This is the default. The user information is saved locally on disk on a folder called "users" and password is encrypted as bcrypt.\
**- LDAP**\
Provide configurations for the LDAP servers that Jenkins should search, minimum one.\
**- Unix user/group database**\
Delegates the authentication to the underlying Unix operating system user database. With this setting, Jenkins account needs to belong to shadow group to read /etc/shadow.\
**- Active Directory**\
With this option, Jenkins authenticates the username and the password through Active Directory. Jenkins recognizes all the groups in Active Directory that the user belongs to, so you can use those to make authorization decisions. "Active Directory" plugin must be installed.

**Authorization:**\
This is where the kind of access is set up for every user. Can be one of the following:\
**- Anyone can do anything**\
No authorization is performed. Everyone gets full control of Jenkins, including anonymous users who haven't signed on.\
**- Legacy mode**\
Behaves exactly the same as Jenkins <1.164. Namely, if you have the "admin" role, you'll be granted full control over the system, and otherwise (including anonymous users) you'll only have the read access.\
**- Logged-in users can do anything**\
Every logged-in user gets full control of Jenkins. The only user who won't have full control is *anonymous* user, who only gets read access.\
**- Matrix-based security**\
In this scheme, you can configure who can do what by using a big table. Each column represents a permission. Each row represents a user or a group. "Matrix Authorization Strategy" plugin must be installed.\
**- Project-based Matrix Authorization Strategy**\
This mode is an extension to "Matrix-based security" that allows additional ACL matrix to be defined for each project separately.\

This is the Jenkins security options when it is installed on different OS:\
![global_security](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_access.py/images/global_security.png)

This is the Matrix-based security mechanism, any account can be configured with granular access:\
![matrix_authorization](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_access.py/images/matrix_authorization.png)

The script performs web requests to this URL list and can determine if the especified user have access to it or not:
1. http://jenkins.local/
2. http://jenkins.local//crumbIssuer/api/json
3. http://jenkins.local/newJob
4. http://jenkins.local/view/all/
5. http://jenkins.local/view/all/builds
6. http://jenkins.local/script
7. http://jenkins.local/jnlpJars/jenkins-cli.jar
8. http://jenkins.local/computer/
9. http://jenkins.local/load-statistics
10. http://jenkins.local/env-vars.html/
11. http://jenkins.local/instance-identity/
12. http://jenkins.local/administrativeMonitor/OldData/
13. http://jenkins.local/manage
14. http://jenkins.local/configfiles/
15. http://jenkins.local/log/
16. http://jenkins.local/pluginManager/installed
17. http://jenkins.local/configureSecurity/
18. http://jenkins.local/configureTools/
19. http://jenkins.local/credentials/
20. http://jenkins.local/credentials/store/system/domain/_/
21. http://jenkins.local/securityRealm/createAccount
22. http://jenkins.local/securityRealm/createAccountByAdmin
23. http://jenkins.local/asynchPeople/
24. http://jenkins.local/securityRealm/
25. http://jenkins.local/ad-health/
26. http://jenkins.local/whoAmI/

Usage:\
python3 ./enum_access.py -w URL
![enum_access_1](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_access.py/images/enum_access_1.png)
![enum_access_2](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_access.py/images/enum_access_2.png)
