import requests 

response=requests.get(url="https://scmeal.ml/순심고")
response.raise_for_status()


data=response.json()

listbreakfast= data["breakfast"]
listlunch= data["lunch"]
listdinner= data["dinner"]

    
def menu(menu, printStr):
    print(printStr)
    if menu == None:
        print('없음\n')
        return
    for i in range(len(menu)):
        print(menu[i])
    print('\n')

menu(listbreakfast,"아침메뉴")
menu(listlunch,"점심메뉴")
menu(listdinner,"저녁메뉴")