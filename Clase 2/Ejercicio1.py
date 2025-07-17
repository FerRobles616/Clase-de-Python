n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if ((n1 % 2 == 0) and (n2 % 2 == 0)):
    print("Ambos son pares")
elif ((n1 % 2 == 0)) and ((n2 % 2 != 0)):
    print("uno es par y el otro es impar")
elif ((n1 % 2 != 0) and (n2 % 2 == 0)):
    print("uno es impar y el otro es par")
elif ((n1 % 2 != 0) and (n2 % 2 != 0)):
    print("Ambos son impares")