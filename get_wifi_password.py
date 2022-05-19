import subprocess
def get_wifi_profile():
    wifi_data = subprocess.check_output(['netsh','wlan','show','profiles'])
    new_data= wifi_data.decode('utf8')
    new_data = new_data.split("\n")
    wifi_names=[]
    for wifi_name in new_data:
        if 'All User Profile     :' in wifi_name:
            ip_name = wifi_name.split(":")[1]
            wifi_names.append(ip_name[1:-1])
    return wifi_names
for wifi_name in get_wifi_profile():
    wifi_data = subprocess.check_output(['netsh','wlan','show','profile',wifi_name,'key=clear'])
    new_data= wifi_data.decode('utf8')
    new_data = new_data.split("\n")
    wifi_passwords=[]
    for wifi_password in new_data:
        if 'Key Content ' in wifi_password:
            ip_password = wifi_password.split(":")[1]
            wifi_passwords.append(ip_password[1:-1])
    print(wifi_passwords)
