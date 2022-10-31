while True: 
    try: 
        status = input()
        if status == "esquerda":
            print("ingles")
        if status == "direita":
            print("frances")
        if status == "nenhuma":
            print("portugues")
        if status == "ambas":
            print("caiu")
    except EOFError: 
        break