def fib(x):
  if x < 0:
   print("Incorrect input")
  elif x == 0:
   return 0
  elif x == 1 or x == 2:
   return 1
  else:
   return fib(x-1) + fib(x-2)
  pass 

print(fib(6))