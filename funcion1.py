import math
valor1=int(input("Ingrese el primer termino del binomio (el coeficiente de la x > 1)"))
valor2=int(input("Ingrese el segundo termino del binomio (el segundo)"))
res1=pow(valor1,2) #se calcula la potencia el primer valor del binomio
res2=(2*valor2) #se calcula el segundo valor del binomio
res3=pow(valor2,2) #se calcula la potencia el segundo valor del binomio
print ("La soluciopn del binomio es: ",res1,"x^2 +",res2,"x +",res3) #se muesta la solucion
resultadox1= -((res2)+(math.sqrt((pow(res2,2))-(4)*(res1)*(res3))))/2*(res1)
print("El resltado de x1 = ",resultadox1)
resultadox1= -((res2)-(math.sqrt((pow(res2,2))-(4)*(res1)*(res3))))/2*(res1)
print("El resltado de x2 = ",resultadox1)