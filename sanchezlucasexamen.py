from os import system
system("cls")
import random


trabajadores=[f"juan perez", "maria garcia", "carlos lopez", "ana martinez", "pedro rodriguez", "laura hernandez", "miguel sanchez", "isabel gomez", "francisco diaz", "elena fernandez"] 
sueldos=[]
sueldo_completo=[]
total=0
sueldo_alto0=0
sueldo_bajo=0










def asignar_aleatorio():
     while True:
         op1=str(input("precione enter para generar el sueldo de juan perez "))
         op1=random.randint(300000, 2500000)
         sueldos.append(op1)
         print("guardado")
         
         
         
         op2=str(input("precione enter para generar el sueldo de maria garcia "))
         op2=random.randint(300000, 2500000)
         sueldos.append(op2)
         print("guardado")
         

         op3=str(input("precione enter para generar el sueldo de carlos lopez "))
         op3=random.randint(300000, 2500000)
         sueldos.append(op3)
         print("guardado")
         


         op4=str(input("precione enter para lgenerar el sueldo de ana martinez "))
         op4=random.randint(300000, 2500000)
         sueldos.append(op4)
         print("guardado")
         


         op4=str(input("precione enter para generar el sueldo de pedro rodriguez "))
         op4=random.randint(300000, 2500000)
         sueldos.append(op4)
         print("guardado")
         


         op5=str(input("precione enter para generar el sueldo de laura hernandez "))
         op5=random.randint(300000, 2500000)
         sueldos.append(op5)
         print("guardado")
         


         op6=str(input("precione enter para generar el sueldo de miguel sanchez "))
         op6=random.randint(300000, 2500000)

         sueldos.append(op6)
         print("guardado")


         op7=str(input("precione enter para generar el sueldo de isabel gomez "))
         op7=random.randint(300000, 2500000)
         sueldos.append(op7)
         print("guardado")

         op8=str(input("precione enter para generar el sueldo de francisco dias "))
         op8=random.randint(300000, 2500000)
         sueldos.append(op8)
         print("guardado")
        
         
         op9=str(input("precione enter para generar el sueldo de elena fernandez "))
         op9=random.randint(300000, 2500000)
         sueldos.append(op9)
         print("guardado")
         print(sueldos)
         sueldo_completo.append(sueldos)

         return
     
         
    
     
    


def mostrar_sueldos():
    while True:
        for sueldos in sueldo_completo:
            print(f"""
                  sueldos menores a $800000 total:{total}
            nombre empleado: sueldo:
              juan perez           {sueldos[0]}    
              maria garcia         {sueldos[1]}
            sueldos entre 800.000 y 2.000.000:

             carlos lopez         {sueldos[2]}
             Ana Martinez          {sueldos[3]}
             sueldos superiores a 2.000.000:
             total:
              Pedro Rodriguez      {sueldos[4]}
              laura Hernandez       {sueldos[5]}
              sueldos entre 2.000.000 y 2.500.000
              total:
              miguel Sanchez        {sueldos[6]}
              isabel Gomez          {sueldos[7]}
              Francisco Diaz         {sueldos[8]}
              elena fernandez         {sueldos[9]}    

               total Sueldos: {sueldos[0]+sueldos[1]+sueldos[2]+sueldos[3]+sueldos[4]+sueldos[5]+sueldos[6]+sueldos[7]+sueldos[8]+sueldos[9]}
                  """)
            break
                
        return













def imprimir():
    archivo=open("examen_final", "w")
    archivo.write(sueldos)










def reporte():
    while True:
        for sueldos in sueldo_completo:
            print(f""""
     nombres:         sueldo base:          descuento de salud:            descuento AFP:                        sueldo liquido:
    juan perez     {sueldos[0]}        {sueldos[0]*0.07}          {sueldos[0]*0.12}                             {sueldos[0]*0.07*0.12}
    maria garcia   {sueldos[1]}        {sueldos[1]*0.07}          {sueldos[1]*0.12}                          {sueldos[1]*0.07*0.12}
    carlos lopez   {sueldos[2]}        {sueldos[2]*0.07}          {sueldos[2]*0.12}                          {sueldos[2]*0.07*0.12}
    ana martinez   {sueldos[3]}        {sueldos[3]*0.07}          {sueldos[3]*0.12}                          {sueldos[3]*0.07*0.12}
    pedro rodriguez   {sueldos[4]}     {sueldos[4]*0.07}          {sueldos[4]*0.12}                          {sueldos[4]*0.07*0.12}
    laura hernandez   {sueldos[5]}      {sueldos[5]*0.07}         {sueldos[5]*0.12}                          {sueldos[5]*0.07*0.12}
    miguel sanchez   {sueldos[6]}       {sueldos[6]*0.07}         {sueldos[6]*0.12}                          {sueldos[6]*0.07*0.12}
    isabel gomez   {sueldos[7]}        {sueldos[7]*0.07}          {sueldos[7]*0.12}                          {sueldos[7]*0.07*0.12}
    francisco diaz   {sueldos[8]}     {sueldos[8]*0.07}           {sueldos[8]*0.12}                         {sueldos[8]*0.07*0.12}
    elena fernandez  {sueldos[9]}     {sueldos[9]*0.07}           {sueldos[9]*0.12}                        {sueldos[9]*0.07*0.12}



""")
            break
        return
    










def menu_aplicacion():
    while True:
        print('''
          1.generar sueldos aleatorios
          2.clasificar sueldos
          3.ver estadisticas
          4.reporte de sueldos
          5.SALIR
          
          
          ''')
        op=str(input(":"))
        match op:
            case "1":
                asignar_aleatorio()
            case "2":
                mostrar_sueldos()
            case "3":
                 break
            case "4":
                reporte()
            case "5":
                break
                
           
                
            






print("Bienvenido")
menu_aplicacion()