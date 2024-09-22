size = int(input("Enter the size of the pattern:") )# size = 4 

x = 1
while x <= size : 

    for num in range(1,size+1) :
        print("*",end="")
    
    print()
    x+=1

