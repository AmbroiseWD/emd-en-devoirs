#Exercice 1
print("")
print("Exercice1")
print("")
a=10
while a > -11 :
    if a%2 == 0 :
        print(a)
        a=a-1
    else:a=a-1

#Exercice 2
print("")
print("Exercice2")
print("")
def safe_Index (item,aray):
    if item in aray:
        a = aray.index(item)
        print("L'index existe et correspond à : " , a)
        a=a+1
        print("ce qui correspond à la ", a , "ème position")
    else :
        print("l'index n'existe pas désolé vous etes bien u ")
patate = ['patate2','rhum','pastis','tabac']
safe_Index(item='rhum',aray=patate)

#exercice3
print("")
print("Exercice3")
print("")
a = patate.index('rhum')
patate.pop(a)
print(patate)

#exercice4
print("")
print("Exercice4")
print("")
def delet_item (item,aray):
    a = aray.index(item)
    aray.pop(a)
    return aray
deuxièmetableau = delet_item('pastis',patate)
print(deuxièmetableau)

#exercice5
print("")
print("Exercice5")
print("")
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
i=0
while i < len(list(d1.keys())) :
    if list(d1.keys())[i] in d2:
        d1[list(d1.keys())[i]]+=d2[list(d1.keys())[i]]
        print(d1)
    i = i+1
m = d2.copy()
m.update(d1)
print(m)
