dias = int(input())
km = int(input())
if km > 100:
    km2 = km - 100
    total = dias*90 + km2*12
    print(f"O valor total é: {total}")
else:
    pagar = dias*90 
    print(f"O valor total é: {pagar}")
    
