import requests 

response=requests.get(url="https://scmeal.ml/%EC%88%9C%EC%8B%AC%EA%B3%A0")
response.raise_for_status()


data=response.json()

breakfast= data["breakfast"]
lunch= data["lunch"]
dinner= data["dinner"]

listbreakfast=[breakfast]

listlunch=[lunch]

listdinner=[dinner]

print("아침 메뉴")
for i in range(len(listbreakfast)):
    print(listbreakfast[i])
        
print("점심 메뉴")
for i in range(len(listlunch)):
    print(listlunch[i])
           
print("저녁 메뉴")
for i in range(len(listdinner)):
    print(listdinner[i])


