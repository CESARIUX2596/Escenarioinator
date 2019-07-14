LENGTH = 1.25
def calculateinator(l_size1, l_size2):
    amount_1 = int(l_size1/LENGTH)
    amount_2 = int(l_size2/LENGTH)
    final_size1 = amount_1 * LENGTH
    final_size2 = amount_2 * LENGTH

    return amount_1, amount_2, final_size1, final_size2

def flicker(bool_value):
    flick = not bool_value
    return flick

def baseinator(amount):
    if amount == 1:
        return 1
    elif amount == 2:
        return 2
    else:
        status = False
        counter = 0
        for i in range(1, amount+1):
            status = flicker(status)
            if status == True:
                counter += 1
            elif ((i == amount) and (status == False)):
                counter += 1
    return counter

def plotinator(amount_a, amount_b):
    status_a = False
    if ((amount_a == 1) and (amount_b == 1)):
        print("X")
        return 0
    else:  
        for a in range(1, amount_a + 1):
            status_a = flicker(status_a)
            if ((status_a == True) or ((status_a == False) and (a == amount_a))):
                status_b = False
                line = ""
                for b in range(1 , amount_b + 1):                   
                    status_b = flicker(status_b)
                    
                    if ((status_b == True) or ((status_b == False) and (b == amount_b))):
                        line += "X  "
                    elif( status_b == True):
                        line =+ "X  "  
                    else:
                        line += "█  "
                print(line)
                print(" ")
            else:
                line = ""
                for i in range(1, amount_b + 1):
                    line += "█  "
                print(line)
                print(" ")

side_a = float(input("Medida en metros para lado a: "))
side_b = float(input("Medida en metros para lado b: "))
if side_a < 1.25:
    side_a = 1.25
if side_b < 1.25:
    side_b = 1.25
amount_side_a, amount_side_b, final_size_a, final_size_b = calculateinator(side_a, side_b)
print(f"Medida Final = {final_size_a} metros por {final_size_b} metros")
print(f"El escenario final es de {amount_side_a} tablas por {amount_side_b} tablas")
total1 = baseinator(amount_side_b)
total2 = baseinator(amount_side_a)
half_a = 0
half_b = 0
if amount_side_a % 2 == 0:
    half_a = 2 * total1 
    print (total1)
if amount_side_b % 2 == 0:
    half_b = 2 * total2 
    print (total2)
plotinator(amount_side_a, amount_side_b)
total_bases = total1*total2
if (half_a > 0 and half_b > 0):
    total_crowns = total_bases*4 - (half_a + half_b) + 1
elif (half_a > 0 or half_b > 0):
    total_crowns = total_bases*4 - (half_a + half_b)
else:
    total_crowns = total_bases * 4

print(f"Se requiere un total de {amount_side_a*amount_side_b} tablas, {total_bases} crucetas y {total_crowns} coronitas")
