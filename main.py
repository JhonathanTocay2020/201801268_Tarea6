import re

def main():
    #Cargar
    archivo = open("ejemplo.aon")
    file = archivo.read()
    env = file.lower().replace(' ','').replace('\n','')
    AFD(env)

def AFD(cadena):
    estado = 0
    con = ''
    num = ''
    bol = ''

    for i in range(len(cadena)):
        if(estado==0):
            if cadena[i] == '(':
                print(str(cadena[i]) + " -- tk_A_parentesis")
                estado = 1
            else:
                print("cadena invalida")
                return
        elif(estado == 1):
            if cadena[i] == '<':
                print(str(cadena[i])+" -- tk_menorQ")
                estado =2
            else:
                print("cadena invalida")
                return
        elif(estado == 2):
            if cadena[i] == '[':
                print(str(cadena[i]) + " -- tk_A_corchete")
                estado =3
            else:
                print("cadena invalida")
                return
        elif (estado == 3):
            if cadena[i].isalpha() or cadena[i]=='_':
                con = con + cadena[i]
                estado = 3
            elif cadena[i] == ']':
                print(str(con) + " -- tk_P_reservada")
                con=''
                print(str(cadena[i])+ " -- tk_C_corchete")
                estado = 4
            else:
                print("cadena invalida")
                return
        elif(estado == 4):
            if cadena[i] == '=':
                print(str(cadena[i]) + " -- tk_igual")
                estado = 5
            else:
                print("cadena invalida")
                return
        elif(estado == 5):
            if cadena[i] == '"':
                print(str(cadena[i]) + " --tk_Comillas")
                estado = 6
            elif cadena[i].isdigit() or cadena[i]=="." or cadena[i]== "-":
                num = num + str(cadena[i])
                estado = 5
            elif cadena[i].isalpha():
                bol= bol + cadena[i]
                if(bol=='true' or bol=='false'):
                    print(bol + "--tk booleano")
                    bol = ''
                    estado = 7
                else:
                    estado = 5
            elif cadena[i]== ',':
                print(num + " -- numero")
                num = ''
                print(cadena[i] + " -- tk_coma")
                estado=2
            else:
                print("cadena invalida")
                return
        elif(estado == 6):
            if cadena[i].isalpha() or cadena[i]=='_' or cadena[i] == ',':
                con = con + cadena[i]
                estado = 6
            elif cadena[i]== '"':
                print(con + " -- tk_cadena")
                print(cadena[i] + " -- tk_Comillas")
                con=''
                estado = 9
            else:
                print("cadena invalida")
                return
        elif(estado == 7):
            if cadena[i] == ">":
                print(cadena[i] + " --tk_mayorQ")
                estado = 8
            else:
                print("cadena invalida")
                return
        elif(estado==8):
            if cadena[i] == ',':
                print(str(cadena[i]) + " --tk_coma")
                estado = 1
            elif cadena[i] ==')':
                print(str(cadena[i])+ " --tk_C_parentesis")
                print("cadena valida")
                return
            else:
                print("cadena invalida")
                return
        elif(estado ==9):
            if cadena[i] == ",":
                print(cadena[i] + " --tk_coma")
                estado = 2
            else:
                print("cadena invalida")
                return

if __name__ == '__main__':
    main()
