
def main():
    num=int(input("Input a Number:"))

    for i in range(1,num+1):
        mod=i%2
        if mod==1:
            print (i,"is odd")
        elif mod==0:
            print (i,"is even")
        else:
            print("Invalid Input")

    choice=input("Do you want to input another number? type YES if you want to proceed").lower()
    if choice=="yes":
        main()
    else:
        exit()

main()
   
    

    