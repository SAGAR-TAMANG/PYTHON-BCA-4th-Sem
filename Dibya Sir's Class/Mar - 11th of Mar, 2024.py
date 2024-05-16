quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} rupees."

print(myorder.format(quantity, itemno, price))
print(myorder.format(2, 0, 1))
print(f"I want {quantity} pieces of item {itemno} for {price} rupees.")



uni = "Kaziranga University"
name = "Upa"
age = 19

text = "I am {}, & I am an {} year old {} student."

print(f"I am {name}, & I am an {age} year old {uni} student.")
print(text.format(name, age, uni))


























