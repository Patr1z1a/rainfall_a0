
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

#Testläufe

x = [2, -5, 2,2, -999, 10, -5]
y = [-999, 5, 2, 3,]

print ("Test x:")
exc(x)

print("Test y:")
exc(y)