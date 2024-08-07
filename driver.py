import user
import owner
print("*"*80)
print("-"*20,">"," !! WELCOME TO OUR RESTAURANT !! ","<","-"*20)
print("*"*80)
print(" "*27," >>> RESTAURANT PAGE <<< ")
print(" "*27," ======================= ")
print(" 1-->>Customer LOGIN")
print(" 2-->>Restaurant owner LOGIN")
ch=input("\nEnter choice: ")
if ch=='1':
    user.login()
elif ch=='2':
    owner.login()
else:
    print("Invalid")
