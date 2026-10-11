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
        ergebnis = summe/count
        print(f"Das Ergebnis ist {ergebnis}")
        return ergebnis 

    except ZeroDivisionError: 
        print("Es befinden sich keine positiven Zahlen vor -999.")
        return None

    finally:
        print("Durchlauf Variante 1 beendet")

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
        ergebnis = summe/count 
        print(f"Das Ergebnis ist {ergebnis}")
        return ergebnis
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

print(exc2(xy))

#Testläufe




print ("Test x:")
exc(x)

print("Test y:")
exc(y)

print("Test Variante 2")
el(x)
el(y)
