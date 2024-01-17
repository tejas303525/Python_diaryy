import requests

with open("/home/profbubs/python/small.txt","r") as file:
    f = [line.strip() for line in file.readlines()]

def loop():
    for words in f:
        print(words)
        data=requests.get(url=f"http://172.217.167.142/{words}")
        if data.status_code==404:
            print("Status 404 - Resource not found:", data)
        else:
            print(data.text)
loop()



    
