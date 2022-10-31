
list_a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letra = input("Informe uma letra do abecedario:")
letra = letra.lower()

if letra in list_a:
    indice = list_a.index(letra)
    print(f"A posição da letra no abecedario é: {indice + 1}")
    
    
