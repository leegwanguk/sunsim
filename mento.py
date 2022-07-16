import requests 

response=requests.get(url="https://scmeal.ml/%EC%A4%91%EC%95%99%EA%B3%A0")
response.raise_for_status()


data=response.json()

listbreakfast= data["breakfast"]
listlunch= data["lunch"]
listdinner= data["dinner"]

    
def menu(a,b):
    print(b)
    for i in range(len(a)):
        print(a[i])

menu(listbreakfast,"아침메뉴")
menu(listlunch,"점심메뉴")
menu(listdinner,"저녁메뉴")    