### [enum_users.py](enum_users.py)
This can be used to perform a dictionary attack to obtain possible usernames.\
Whether Jenkins is configured to use local user database or Active Directory.\
*Internet is required* to use an online Seclist dictionary or it can use a local wordlist to do bruteforcing offline.\
The brute force attempts are made with the anonymous user account, which must be enabled as read-only.

Usage:
python3 ./enum_users.py -w URL
![enum_users_1.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_1.png)

First, the script check if the anonymous user can display the list of local users and/or the known Jenkins users whom logged in at least once.\
http://jenkins.local/asynchPeople/\
http://jenkins.local/SecurityRealm/
![enum_users_6.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_6.png)
![enum_users_7.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_7.png)

You can specify a local wordlist to perform the bruteforce attack. Each valid user found will display the URL where you can validate and obtain more information if available.
![enum_users_2.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_2.png)
![enum_users_3.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_3.png)

But, if no wordlist is specified, it will download a list of Seclist Usernames from the internet to use as a dictionary and perform the bruteforce with it.
![enum_users_4.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_4.png)
![enum_users_5.png](https://github.com/stevenvegar/Jenkins_scripts/blob/main/enum_users.py/images/enum_users_5.png)


