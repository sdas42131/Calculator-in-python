# Defining functions

def sum(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def div(num1, num2):
    return float(num1 / num2)

def mult(num1, num2):
    return num1 * num2

# Press "=" anywhere to know the answer.
print("\nPress '=' anywhere to know the answer.")
num1 = int(input("Enter number: "))
while True:
    op = (input("Enter operator: "))
    
    if op == "=":
        break
        
    num2 = int(input("Enter number: "))
    if op == "+":
        num1 = sum(num1, num2)
    if op == "-":
        num1 = difference(num1, num2)
    if op == "*":
        num1 = mult(num1, num2)
    if op == "/":
        num1 = div(num1, num2)
        
print(f"\nAns is: {num1}")



    