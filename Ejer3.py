def Saludar():
    print("Hola mundo")
def CalcularDoble(num):
    res = num*2
    return res
def Triplicar(num):
    res = num*3
    return res
print("Lammar a la funcion saludar:")
Saludar()
num =int(input("Ingrese un valor numérico para num:"))
print("Llamar a la funcion CalcularDoble")
CalcularDoble(num)
print("El doble de ",num,"es",CalcularDoble(num))
print("Llamada a la funcion triplicar")
Triplicar(num)
print("El triple de ",num,"es:",Triplicar(num))