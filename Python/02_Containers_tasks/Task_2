import requests 

ip = requests.get('https://api.ipify.org/?format=json')
ip = ip.text
ip= ip[7:21]
print("your ip is : " + ip + "\n")
location = requests.get(f'https://ipinfo.io/{ip}/geo')
print("your location :  \n"+location.text)
