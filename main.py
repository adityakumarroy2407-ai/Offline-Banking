import json
print("1. SEND MONEY")
print("2. cash out")
print("3. Mobile recharge")
print("4. Download Bkash app")
print("5. My bkash")
print("6. Exit")
accountBalance = 140

n = int(input("Enter your choice: "))
if(n>6):
    print("Enter a number between 1 to 6")

elif(n==1):
    reciever=(input("Enter reciever bkash account number:"))
    amount=int (input("Enter amount: "))
    if(amount>accountBalance):
        print("You donot have sufficiant balance")
    else:
        print("Succesfully send",amount,"tk")
        accountBalance=accountBalance-amount
        print ("New balance:",accountBalance)
elif n==2:
    print("1. From agent")
    print("2. From ATM")
    m=int(input("Enter your choice:"))
    if m==1:
        agent=input("Enter agent number:")
        amount=int(input("Enter amount:"))
        if(amount>accountBalance):
            print("You donot have sufficiant balance")
        else:
            print("Succesefully cashout",amount,"tk")
            accountBalance=accountBalance-(amount*0.0139+amount)
            print("Your new balance is",accountBalance)
    else:
        pin=int(input("Enter your pin"))
        amount=int(input("Enter amount"))
        if(amount>accountBalance):
            print("You donot have sufficiant balance")
        else:
            print("Succesefully cashout",amount)
            accountBalance=accountBalance-(amount*0.01+amount)
            print("Your new balance is",accountBalance)

elif n==3:
    MobileNo=input("Enter mobile number:")
    amount=int(input("Enter amount:"))
    if amount>accountBalance:
         print("You donot have sufficiant balance")
    else:
        accountBalance=accountBalance-amount
        print("you have successfully recharged with amount",amount,"BDT")
        print("Your new balance is",accountBalance)



    

