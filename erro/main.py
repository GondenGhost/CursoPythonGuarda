
tipo_do_calculo=input("escolha tipo do calculo(+,-,x,%):")
num1=int(input("digite um numeros:"))
num2=int(input("digite um outro numero"))
if tipo_do_calculo == "+":
    total = (num1+num2)
    print("tomi o total,:",total)
elif  tipo_do_calculo == "-":
    total = int(num1-num2)
    print("tomi o total,:",total)
elif tipo_do_calculo == "/":
    total =  (num1/num2)
    print("tomi o total,:",total)
elif tipo_do_calculo  == "*":
    total = int(num1*num2)
    print("tomi o total,:",total)
else:
  print("tipo do calculo invalido")





































