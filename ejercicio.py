lista=[1,9,5,0,20,-4,12,7,16]
obj=12
for i in range(len(lista)):
  for j in range (i+1):
    a=lista[i]
    b=lista[j]
    result=a+b
    if (result==12):
      print(a,b)

