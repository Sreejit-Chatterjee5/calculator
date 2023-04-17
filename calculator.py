#Calculator
#Addition
def add(n1, n2):
  return (n1 + n2)
#Subtraction
def sub(n1, n2):
  return (n1 - n2)
#Multiplication
def mul(n1, n2):
  return (n1 * n2)
#Division
def div(n1, n2):
  return (n1/n2)

calculator = {
  '+': add, 
  '-': sub, 
  '*': mul, 
  '/': div
}
num1 = int(input("What is the first number?: "))
for key in calculator.keys():
    print(key)
end = False
while end is False:
  symbol = input("Pick an operation from the list above: ")
  num2 = int(input("What is the next number?: "))
  for key in calculator.keys():
    if key == symbol:
      i = key
  if i == "/" and num2 == 0:
    print("Math Error! number cannot be divided by zero")
  else:
    answer = calculator[i](num1, num2)
    print(f"{num1} {i} {num2} = {answer}")
    come = input("Do you want to continue?(yes/no): ").lower()
    if come == 'yes':
      num1 = answer
      continue
    else:
      end = True
