def fib(x):
  if x == 0: 
    return print(0)
  elif x == 1: 
    return print(1)
  else: 
    fn0 = 0
    fn1 = 1 
    count = 2
    while True:
      fn2 = fn1 + fn0
      if count == x: 
        return print(fn2)
        break
      else:
        fn0 = fn1
        fn1 = fn2
        count = count + 1
        continue
  pass 

fib(6)