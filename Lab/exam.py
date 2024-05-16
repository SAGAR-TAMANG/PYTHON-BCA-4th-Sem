print("Welcome to the Code")

membership = input("Premium/Regular:")
def borrow(membership:str) -> int:
  if membership == "Premium":
    return 10
  else:
    return 5
  
print("You can brrow ", borrow(membership), " books")

# Late Fees Calculator

def late_return_calculator(days, membership) -> int:
  if membership == "Premium":
    return days * 2
  else:
    return days * 10

days = int(input("Number of  days late:"))
print("the late fees is ", late_return_calculator(days, membership))

books = {
  'Titanic': "Not_reserved",
  'The Stranger': "Not_reserved",
  'Fifty Shades of Gray': "Not_reserved",
  'Attention is all you need': "Reserved",
}

def get_book(book):
  status = books[book]

  print("Status:", status)

  if status == "Reserved":
    return False
  else:
    return True
  
book = input("Book Name: ")

status = get_book(book)

if status:
  print("Book reserved for you")
else:
  print("Book Not Reserved as it is already Taken")

