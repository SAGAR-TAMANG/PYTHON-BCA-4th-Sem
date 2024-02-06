def sagar(cat):
    if((cat%2)==1):
        return("odd")
    else:
         ("even")
def main():
    user = int(input("give a number:"))
    ans=sagar(user)
    print("the number is", ans)
if __name__=="__main__":
  main()