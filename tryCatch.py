a = 10
b = 0
try:
  a/b
except ZeroDivisionError:
  print('division by 0')
finally:
  print('this always executes')