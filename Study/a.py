def myfunc():
  a = 0  
  yield a
  a = 2
  yield a

gen = myfunc()

for i in gen:
  print(i)