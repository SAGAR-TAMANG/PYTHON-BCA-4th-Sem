def test(f):
  def wrapper():
    print("Before the function executes")

    a = f()
    
    a = a.upper()
    
    print("After the function executes")
    return a

  print("Wrapper")
  return wrapper

@test
def myfunc():
  return "My name is Sagar"

myfunc()