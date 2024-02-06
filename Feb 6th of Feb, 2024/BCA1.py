# use two function to check whether a number is odd or not taking from user
def  result(a):
    if((a%2)==0):
        return"even"
    else:
        return"odd"

def main():
     User=int(input("giva a number:"))
     ans=result(User)   
     print("the number is",ans)   

main()