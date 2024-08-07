def itemlist():
    import random
    print(" ")
    print(" "*10," >>> ITEMS PAGE <<< ")
    print(" "*10," ================== ")
    fp=open("items.txt")
    c=fp.read()
    cp=fp.readlines()
    print(c)
    fp.close()
    total=0
    l=[]
    l1=[]
    l2=[]
    fp=open("items.txt",'r')
    cp=fp.readlines()
    while True:
        flag=0
        dn=input("\nChoose dish number: ")
        for i in cp:
            k=i.rstrip().split(",")
            if k[0]==dn:
                q=int(input("Enter Quantity : "))
                l1.append(q)
                total = total + (q *int(k[2]))
                l.append(dn)
                flag=1
        if flag==0:
            print("Dish number not present")
        ch5=input("Press 'y' to choose another dish: ").lower()
        if ch5=='y':
            continue
        else:
            on=random.randint(1,500) + random.randint(500,1000)
            print("\n","*"*26,"!! YOUR ORDER LIST !!","*"*28)
            print(f"\n Order number : {on}")
            l2.append(f"{on},")
            for i in cp:
                p=i.rstrip().split(",")
                for j in range(len(l)):
                    if p[0]==l[j]:
                        print(f"{p[1]},{l1[j]}")
                        l2.append(f"{p[1]},{l1[j]},")
            l2.append("\n")
            print(l2)
            print(f"\n ================********* TOTAL AMOUNT IS : RS {total} **********================")
            break
    ch2=input("ARE YOU CONFIRM: (YES/NO): ")
    if ch2=='YES':
        print("\n"," "*11," ..........>>>>>>THANKS FOR CONFIRMING <<<<<<............ ","\n")
        print("\n"," "*9," ......>>>>>>CONGRATS !! YOUR ORDER IS RECEIEVED<<<<<<........ ","\n")
        ol=open("orderlist.txt",'a')
        ol.writelines(l2)
        ol.close()
    else:
        print("\n ========>>> THANK YOU !! RELOGIN FOR NEW ORDER <<<======== ")
        
                          
    
