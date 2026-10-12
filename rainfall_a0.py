xy = [2, -5, 2,2, -999, 10, -5]
x =  [5, 60, 30, 4, -900, -999]
y = [-999, 5, 2, 3,]

# Variante 1: Mit Exception Handling
def exc (xy):
    summe = 0
    count = 0

    for i in xy:
        if i == -999:
            break
        if i >= 0: 
            summe += i
            count += 1

    try:
        t = summe / count 
        return t

    except ZeroDivisionError: 
        print(f"Keine positiven Zahlen in d. Liste {xy}")
        return None

#Variante 2: If-Else 
def el (a):
    summe = 0
    count = 0

    for i in a:
        if i == -999:
            break
        if i >= 0: 
            summe += i
            count += 1

    if count == 0: 
       print("only Chuck Norris can divide by 0") 
       return None

    else:
        p = summe / count
        return p
    
#Variante 3: List comprehension
def lis (c):
    f = c.index(-999)
    s = c[:f]
    s = [i for i in s if i >= 0]
    if len(s) == 0:
        return None
    erg = sum(s) / len(s)
    return erg

#Variante 4: Lamda
exc2 = lambda xy: (
    s := [i for i in xy[: xy.index(-999)] if i >= 0], 
    sum(s) / len(s) if s else None
)[1]

#Testbereich
print ("Test Var1:")

print("Liste x:",exc(x))
print("Liste y:", exc(y))


print("Test Var2")
print("Liste x:", el(x))
print("Liste y:", el(y))

print("Test Var3")
print("Liste x:",lis(x))
print("Liste y:",lis(y))

print("Test Var4")
print("Liste x:",exc2(x))
print("Liste y:",exc2(y))
print("Liste xy:",exc2(xy))
