n1 = int(input("Informe um número:"))
n2 = int(input("Informe outro número:"))
n3 = int(input("Informe outro número:"))
if n1 > n2 and n1 > n3:
    print(f"O maior número é: {n1}")
if n2 > n1 and n2 > n3:
    print(f"O maior número é: {n2}")
if n3 > n1 and n3 > n2:
    print(f"O maior número é: {n3}")
if n1 < n2 and n1 < n3:
    print(f"O menor número é: {n1}")
if n2 < n1 and n2 < n3:
    print(f"O menor número é: {n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor número é: {n3}")
