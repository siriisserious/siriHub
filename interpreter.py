expression = input("Expression: ")
x, sign, y = expression.split(" ")
x = float(x)
y = float(y)

if sign == "+":
  print(x + y)
elif sign == "-":
  print(x - y)
elif sign == "*":
  print(x * y)
elif sign == "/":
  print(x / y)
