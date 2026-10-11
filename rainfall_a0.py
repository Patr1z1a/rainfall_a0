
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

#Variante 2: If-Else | kein Break
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

#Variante 3: Lamda
exc2 = lambda xy: (s := [x for x in xy[: xy.index(-999)] if x >= 0], (sum(s) / len(s) if s else 0.0))[1]


#Testläufe

x = [2, -5, 2,2, -999, 10, -5]
y = [-999, 5, 2, 3,]

print ("Test x:")
exc(x)

print("Test y:")
exc(y)

print("Test Variante 2")
el(x)
el(y)
