import os
from time import sleep
#Login
contas = {}
itens = {}
os.system("clear")
with open ("accounts.txt", "w", encoding="utf8") as file:
    file.close()
if not os.path.exists("./users/"):
    os.mkdir("users")
with open ("accounts.txt", "r", encoding="utf8") as file:
    txt = [linha[0:-1] for linha in file.readlines()] # -1 no primeiro linha remove o \n
    for i,_ in enumerate(txt):
        x = txt[i].split("//")
        contas[x[0]] = x[1:]
    login = False
    print(contas)
    user = input("Digite o nome de usuário -> ")
    while True:
        if login:
            file.close()
            break
        elif user in contas:
            while True:
                opc = input("Você deseja logar nessa conta de usuário? (s/n) -> ").lower()
                if opc == "s":
                    while True:
                        senha = input("Digite sua senha -> ")
                        if senha in contas[user]:
                            print("Seja bem vindo!")
                            login = True
                            break
                        else:
                            print("Senha incorreta. Tente novamente!")
                            continue
                    break
                elif opc == "n":
                    while True:
                        user = input("Digite o nome de usuário -> ")
                        if user in contas:
                            print("Este usuário já existe!")
                            continue
                        break
                    break
        elif not login:
            print(f"Você deseja criar uma conta com o nome: {user}?")
            while True:
                opc = input("(s/n) -> ").lower()
                if opc == "s" or opc == "n":
                    break
                else:
                    continue
            if opc == "s":
                senha = input("Digite a sua senha -> ")
                with open("accounts.txt","a",encoding="utf8") as arquivo:
                    arquivo.write(f"{user}//{senha}\n")
                    arquivo.close()
                    os.mkdir(f"users/{user}")
                login = True
                continue        
            elif opc == "n":
                print("Obrigado por usar o Backpack Creator!")
                exit()

#Dentro do sistema
criar = False
while True:
    sleep(1.5)
    os.system("clear")
    print("O que você deseja fazer?\nc - Criar personagem | l - Carregar personagem | q - Sair do Backpack Creator")
    opc = input("-> ").lower()
    if opc == "c":
        while True:
            char = input("Escreva o nome do seu personagem -> ")
            if os.path.isfile(f"users/{user}/{char}.txt"):
                print(f"{char} já existe.")
                while True:
                    ask = input("Você deseja sobrescrever o personagem? (s/n) -> ").lower()
                    if ask == "s":
                        criar = True
                        break
                    elif ask == "n":
                        break
                if criar:
                    break
            else:
                criar = True
                break
        if criar:
            break
        else:
            continue
    elif opc == "l":
        if not os.listdir(f"users/{user}/"):
            print("Você não possui nenhum personagem para carregar")
            continue
        else:
            print("Você possui os seguintes personagens criados: ")
            for e in os.listdir(f"users/{user}/"):
                print(e[0:-4])
            char = input("Escreva o nome do personagem que deseja carregar -> ")
            if os.path.isfile(f"users/{user}/{char}.txt"):
                break
            else:
                print("Esse personagem não existe")
    elif opc == "q":
        print("Obrigado por usar o Backpack Creator!")
        exit()
    else:
        continue

if criar:
    with open (f"users/{user}/{char}.txt","w",encoding="utf8") as file:
        file.write("")
        file.close()



#Dentro da mochila
while True:
    os.system("clear")
    opc = input("Escolha uma das opções disponíveis\nd - apagar | a - adicionar | e - editar | v - visualizar | s - pesquisar | q - sair\n-> ").lower()
    if opc == "d":
        break
    elif opc == "a":
        with open (f"users/{user}/{char}.txt","a",encoding="utf8") as file:
            infos = []
            info = input("Digite o nome do item -> ")
            infos.append(info)
            info = input("Escolha o tipo do item (w - arma | a - armadura | h - cura | e - equipamentos | o - outros -> ").lower()
            if info == "w":
                info = "Arma"
            elif info == "a":
                info = "Armadura"
            elif info == "h":
                info = "Cura"
            elif info == "e":
                info = "Equipamentos"
            elif info == "o":
                info = "Outros"
            else:
                info = "Outros"
            infos.append(info)
            info = input("Digite a classe do item -> ")
            infos.append(info)
            info = input("Digite o valor do item -> ")
            infos.append(info)
            info = input("Digite a quantidade de itens -> ")
            infos.append(info)
            infos = "//".join(infos)
            file.write(f"{infos}\n")
            file.close()
            print("\nItem adicionado!")
            sleep(1)
            continue
    elif opc == "e":
        with open (f"users/{user}/{char}.txt", "r",encoding="utf8") as file:
            editN = input("Escreva o nome do item -> ")
            editC = input("Escolha o tipo do item que será editado (w - arma | a - armadura | h - cura | e - equipamentos | o - outros -> ").lower()
            if editC == "w":
                tp = "Arma"
            elif editC == "a":
                tp = "Armadura"
            elif editC == "h":
                tp = "Cura"
            elif editC == "e":
                tp = "Equipamento"
            elif editC == "o":
                tp = "Outro"
            else:
                tp = "Outro"
            backpack = {}
            txt = [item[0:-1] for item in file.readlines()]
            for i,_ in enumerate(txt):
                itm = txt[i].split("//")
                backpack[itm[0]] = itm[1:]
                if editN in backpack and backpack[editN][0] == editC:
                    print(f"Tipo atual do item:{backpack[editN][0]}\nClasse atual do item:{backpack[editN][1]}\nValor atual do item:{backpack[editN][2]}\nQuantidade atual do item:{backpack[editN][3]}")
                    novo = []
                    novo.append(input("Digite a nova classe do item -> "))
                    novo.append(input("Digite o novo valor do item -> "))
                    novo.append(input("Digite a nova quantidade do item -> "))
                    backpack[editN] = novo[0:]
                    with open(f"users/{user}/{char}.txt","w",encoding="utf8") as arquivo:
                        for k,v in backpack.items():
                            arquivo.write(f"{k}//{backpack[k][0]}//{backpack[k][1]}//{backpack[k][2]}//{backpack[k][3]}\n")
                            print("\nItem editado!")
                            continue
            print("\nO item não existe!")
            continue
    elif opc == "v":
        print('=-'*30)
        with open (f"users/{user}/{char}.txt","r",encoding="utf8") as file:
            backpack = {}
            txt = [item[0:-1] for item in file.readlines()]
            for i,_ in enumerate(txt):
                itm = txt[i].split("//")
                backpack[itm[0]] = itm[1:]

        print("\nArmas\n")
        for k,v in backpack.items():
            if v[0] == "Arma":
                print(f"{k}\nClasse:{v[1]}\nValor:{v[2]}\nQuantidade:{v[3]}")

        print("\nArmaduras\n")
        for k,v in backpack.items():
            if v[0] == "Armadura":
                print(f"{k}\nClasse:{v[1]}\nValor:{v[2]}\nQuantidade:{v[3]}")

        print("\nCura\n")
        for k,v in backpack.items():
            if v[0] == "Cura":
                print(f"{k}\nClasse:{v[1]}\nValor:{v[2]}\nQuantidade:{v[3]}")

        print("\nEquipamentos\n")
        for k,v in backpack.items():
            if v[0] == "Equipamentos":
                print(f"{k}\nClasse:{v[1]}\nValor:{v[2]}\nQuantidade:{v[3]}")

        print("\nOutros\n")
        for k,v in backpack.items():
            if v[0] == "Outros":
                print(f"{k}\nClasse:{v[1]}\nValor:{v[2]}\nQuantidade:{v[3]}")

        input("\nAperte enter para voltar")
        continue
    elif opc == "s":
        break
    elif opc == "q":
        print("Obrigado por usar o Backpack Creator!")
        break
    else:
        continue