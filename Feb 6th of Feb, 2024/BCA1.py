# use two function to check whether a number is odd or not taking from user
def  result(a):
    if((a%2)==0):
        return"even"
    else:
        return"odd"

def main():
     User=[1, 2, 3, 4, 5, 6, 7, 8, 9]
     
     for i in User:
        ans=result(i)   
        print("the number is",ans)   

main()