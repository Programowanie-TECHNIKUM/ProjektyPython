def pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    if n <= 2 or n % 2 != 0:
        return "Nie ma"
    for i in range(2, n):
        if pierwsza(i) and pierwsza(n-i):
            return str(i) + "," + str(n-i)
    return "Nie ma"


for i in range(1, 101):
    if(goldbach(i) != "Nie ma"):
        print(f"{i} >> {goldbach(i)}")