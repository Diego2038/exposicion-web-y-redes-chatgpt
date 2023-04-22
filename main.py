from mensaje_entrada import mensaje_entrada

print("Seleccione un número para escoger el módulo, digite -1 para salir del módulo en cuestión")
while(True):
    modulo = input("Digite el módulo que quiere entrar: ")
    if (modulo == "-1"):
        break

    if modulo in ['1','2','3','4','5']:
        mensaje_entrada(modulo)
    else:
        print('Número reconocido, por favor vuelva a intentarlo')
     