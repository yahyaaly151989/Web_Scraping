# ================================= requests Module ==================================

import requests

# r = requests.get("https://sllearnengine.blob.core.windows.net/material-images/d7aa9e6be90c47c3968f99d1a30792e1-Python%20For%20Beginners.png")

# print(r)
# print(r.status_code)
# print(r.ok)

# print(dir(r))
# print(help(r))

# print(r.text)
# print(r.content)

# with open("python.png", "wb") as f:
#     f.write(r.content)

# print(r.headers['Date'])


# r =  requests.get("http://httpbin.org/get?country=Syria&capital=Damascus")

# payload = {"country": "Syria", "capital": "Damascus"}
# r =  requests.get(url="http://httpbin.org/get", params=payload)


# print(r.status_code)
# print(r.url)


# payload = {"fname": "Yehya", "lname": "Ali"}
# r =  requests.post(url="http://httpbin.org/post", data=payload)


# print(r.status_code)
# print(r.url)
# print(r.text)
# print(r.json())

# payload = {"fname": "Yehya", "lname": "Ali"}
# r =  requests.put(url="http://httpbin.org/put", data=payload)

# print(r.status_code)
# print(r.url)
# print(r.text)
# print(r.json())




# r =  requests.get("http://httpbin.org/basic-auth/yehya/123", auth=("yehya1", 123))

# print(r.status_code)
# # print(r.url)
# # print(r.json())



# try:
#     # r =  requests.get("http://httpbin.org/delay/3", timeout=4)
#     r =  requests.get("http://httpbin.org/delay/3", timeout=2)
#     print(r.status_code)
# except requests.exceptions.ReadTimeout:
#     print("Timeout")

# print("Hi")

import login_info

login_url = "https://the-internet.herokuapp.com/authenticate"

target_url = "https://the-internet.herokuapp.com/secure"

payload = {
    "username": login_info.username,
    "password": login_info.password
}


with requests.session() as s:
    r = s.post(url=login_url, data=payload)
    r2 = s.get(target_url)
    print(r2.text)