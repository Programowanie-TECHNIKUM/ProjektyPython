def pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def slabagoldbacha(doilu):
  for i in range(9,doilu,2):
    for p in range(2,i):
      if pierwsza(p):
        for a in range(2,i):
           if pierwsza(a):
             for u in range(2,i):
               if pierwsza(u):
                 if(i-u-a-p==0):
                   print(f"{i} = {u} i {a} i {p}")

slabagoldbacha(199)