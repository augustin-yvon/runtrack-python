def calcule(num1:int, operator:str, num2:int):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    return result
    
print(calcule(547,"+",8))
print(calcule(8,"-",18))
print(calcule(666,"/",3))
print(calcule(5,"*",7))
print(calcule(20,"%",4))

