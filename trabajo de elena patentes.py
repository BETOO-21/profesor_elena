patentes=["ABC123","AAA123","AEI111"]
velocidades=[60, 120, 45]
meses=[1, 2, 3]
años=[2015, 2026, 2002]




def menu():
    print("1) nueva patente y velocidad")
    print("2) Ver todo")
    print("3) Ver listado de infractores")
    print("4) Buscar por patente")
    print("5) Salir")
   
      
    
        
def Agregar():
    Patente=input("ingrese nueva patente: ")
    Velocidad=int(input("Ingrese nueva velocidad: "))
    Mes=int(input("Ingrese el nuevo mes: "))
    Año=int(input("Ingrese el nuevo Año: "))
    meses.append(Mes)
    años.append(Año)
    patentes.append(Patente)
    velocidades.append(Velocidad)
    
    
    
    
def Ver_todo():
    for i in range(len(patentes)):
        print(patentes[i], velocidades[i], meses[i], años[i])
        
        
        
        
        
        
def Infractores():
    for i in range(len(velocidades)):
        if velocidades[i]>60:
            print("Ptanete infractora: ", patentes[i], "  ",  "velocidad: ", velocidades[i], "  ", meses[i], "  ", años[i])
            
            
                
                        
def Buscar():
    cont=0
    patente_buscar=input("Ingrese patente a buscar :")
    for i in range(len(patentes)):
        if patente_buscar==patentes[i]:
            if velocidades[i]>60:
                cont+=1
            print("infracciones:", cont, "patente:",patentes[i], "  velocidad:",velocidades[i], "  mes:",meses[i], "   Año: ", años[i])
            
            
            
                        
def main():
    op=0
    while(op!=5):
        menu()
        op=int(input("Ingrese una opcion: "))
        if op==1:
            Agregar()
        if op==2:
            Ver_todo()
        if op==3:
            Infractores()
        if op==4:
            Buscar()
    print("Saliendo del programa...")
main()