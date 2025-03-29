valor = int(input())
if valor > 500:
    x = valor - 500
    imposto = x * 0.5
    total = valor + imposto
    print(f"O valor total da compra é: {total}")
else: 
    print(f"O valor total da compra é: {valor}")
    
    
