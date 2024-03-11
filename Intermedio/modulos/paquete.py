import Intermedio.paquetes.paquete.multiplicar
import Intermedio.paquetes.paquete.sumar
print("Esta función te ayuda a multiplicar 2 números")
num1 = int(input("Ingresa el número 1: "))
num2 = int(input("Ingresa el número 2: "))
print(f"El resultado de la multiplicación es: {Intermedio.paquetes.paquete.multiplicar.mult(num1, num2)}")

print(f"El resultado de la suma es: {Intermedio.paquetes.paquete.sumar.suma(num1, num2)}")