def login():
    pd="owner@123"
    pwd=input("Enter Password: ")
    if pwd==pd:
        print(" ------->>!! LOGGED IN SUCCESSFULLY !!<<-------")
        while True:
            print("\n======>>>>> What do you want to do ? <<<<<========\n")
            print(" 1--> View Items list")
            print(" 2--> Update items in list")
            print(" 3--> Dispatch order")
            print(" 4-->Close")
            ch=input("\nEnter choice\n")
            if ch=='1':
                print("*"*5," !! ITEMS PAGE !!","*"*5)
                fp=open("items.txt")
                c=fp.read()
                print(c)   
            elif ch=='2':
                l=[]
                fp=open("items.txt",'r')
                cp=fp.readlines()
                for i in cp:
                    k=i.rstrip().split(",")
                    l.append(k[0])
                print(" 1--> Add new item ")
                print(" 2--> Delete an item ")
                print(" 3--> Update the price of an item ")
                ch1= input("\nEnter choice : ")
                if ch1 == '1':
                    item_no=input('\nEnter item no : ')
                    if item_no in l:
                        print(" .........SORRY !! Item no is already present !!........... ")
                        print(" .........Try Using Item no which is not present ...........")
                    else:
                        item_name=input("\nEnter item name: ")
                        item_price=input("Enter price of item : ")
                        fp=open("items.txt","a")
                        fp.writelines(item_no + "," + item_name + "," + item_price + "\n")
                        print("\n ------>>>> ITEM ADDED SUCCESSFULLY <<<<<-------")
                elif ch1=='2':
                    fp=open("items.txt","r+")
                    c=fp.readlines()
                    fp.seek(0)
                    ch5=input("\n Enter item no to delete from list : ")
                    if ch5 in l:
                        for i in c:
                            k=i.rstrip().split(",")
                            if k[0]!=ch5:
                                fp.write(i)
                        fp.truncate()
                        print("\n ------>>>> ITEM DELETED SUCCESSFULLY <<<<<------ ")
                    else:
                        print("  .......   SORRY !! Item no not present !!........... ")
                        print(" ........ Try Using Item no which is present ..........")
                        
                elif ch1=='3':
                    fp=open("items.txt",'r')
                    cp=fp.readlines()
                    itemno=input("\nEnter item no : ")
                    if itemno in l:
                        name=input("Enter item name: ")
                        price=input("Enter the price to be updated : ")
                        if price.isdigit():
                            for i in range(len(cp)):
                                if name in cp[i]:
                                    cp[i]= itemno + "," + name + "," + price + "\n"
                                    print("\n")
                                    print(cp[i])
                                    print("\n ----->>>> UPDATED SUCCESSFULLY <<<<-----")
                                    flag=1
                                    break
                            if flag==0:
                                print("....... ITEM NOT FOUND !!.........")
                        else:
                            print(" ........PRICE SHOULD BE NUMERIC !!.......... ")
                        fp=open("items.txt",'w')
                        cp=fp.writelines(cp)
                    else:
                        print("\n ....... Item number not present......... ")
                else:
                    print(" .......... INVALID CHOICE !! ...........")
                    break
                    
            elif ch=='3':
                fp=open("orderlist.txt","r")
                c=fp.readlines()
                print(" \n","*"*10," !! ORDERS LIST !! ","*"*10,"\n")
                for i in c:
                    print(" "*2,i)
                fp1=open("orderlist.txt","r+")
                cp=fp1.readlines()
                fp1.seek(0)
                l1=[]
                for i in cp:
                    k1=i.rstrip().split(",")
                    l1.append(k1[0])
                choice=input("\nChoose Order number to dispatch: ")
                if choice in l1:
                    for i in cp:
                        k1=i.rstrip().split(",")
                        if k1[0]!=choice:
                            fp1.write(i)
                    fp1.truncate()
                    print(f"\n>>>>> ORDER NO.{choice} DISPATCHED SUCCESSFULLY <<<<<")
                else:
                    print("\n ..........Order not Present !! .......... ")
            elif ch=='4':
                print(" "*20,"******** !! THANK YOU !! ********")
                break
    else:
        print(" INVALID PASSWORD !!")
        print("\n  ---------------************--------------")
        login()
