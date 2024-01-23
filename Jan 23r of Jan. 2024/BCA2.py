# age=int(input("enter your age"))
# if age > 18:
#     if age < 100:
#         print("You can vote.")
#     else:
#         print("This persion is dead.")
# else:
#     print("You cannot vote.")

    
age=int(input("enter your age"))
if age > 18 and age < 100:
    print("You can vote.")
elif age > 18 and age > 100:
    print("This person is dead")
else:
    print("You cannot vote.")

