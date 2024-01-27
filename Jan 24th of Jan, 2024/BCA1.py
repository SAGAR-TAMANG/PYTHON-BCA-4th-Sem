# Write a program where if a person's age > 18 & Indian then will
# get 15% discount, & if he is greater than 18 & other country
# then will get 5%

age = int(input("AGE: "))
country = (input("Country: "))

if age >= 18:
  if country.lower() == "india":
    print("15 discount")
  else:
    print("5 discount")
else:
  print("No discount")