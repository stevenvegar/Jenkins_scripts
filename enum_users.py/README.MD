### [enum_users.py](enum_users.py)
This can be used to perform a dictionary attack to obtain possible usernames.\
Either if Jenkins is configured to use local user database or Active Directory.\
*Internet required* to use an online Seclist dictionary or it can use a local wordlist to do bruteforcing offline.\
The bruteforcing attempts are done with the anonymous user, which must be enabled as read-only.

Usage:
python3 ./enum_users.py -w URL
![enum_users_1.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_1.png)

First, the script check if the anonymous user can display local user list and/or known Jenkins user which logged in at least once.\
http://jenkins.local/asynchPeople/
http://jenkins.local/SecurityRealm/
![enum_users_6.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_6.png)
![enum_users_7.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_7.png)

You can especify a local wordlist to perform the bruteforcing attack. Every valid user found, it will display the URL where you can validate and obtain more information if available.
![enum_users_2.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_2.png)
![enum_users_3.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_3.png)

But, if no wordlist is especified, it will download a Seclist Username list from internet as a dictionary and perform the bruteforcing with it.
![enum_users_4.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_4.png)
![enum_users_5.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_5.png)


