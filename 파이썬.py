a=input("더할 수들을 띄워서 입력하십시오.").split()
sum=0
for i in range(len(a)):
    sum+=int(a[i])
print(sum)
