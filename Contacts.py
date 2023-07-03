#Menu driven Contact Application that is used to store user input data(number, name, email) in a csv file and can update, delete, display the data
#function that return line number of particular phone number if it is present in csv file if not found returns -1
def findnumber(n):
    with open("Contact.csv","r") as c:
        line,cnt=c.readlines(),0
        while cnt<len(line):
            if line[cnt][:10]==n:
                return cnt
            cnt+=1
    return -1

#function used to insert data into csv file
def create(number,name,email):
    with open("Contact.csv","a") as c:
        c.write(number+","+name+","+email+"\n")

#Function used to delete particular data from csv file based on line number        
def delete(idx):
    with open("Contact.csv","r") as c:
        l=c.readlines()
        del l[idx]
    with open("Contact.csv","w") as c:
        print(*l,file=c)
        
#main program a menu driven coode
while 1:
    #display of menu and input of choice
    print("\n1. Create Contact\n2. Update Contact\n3. Delete Contact\n4. Display All Contacts\n5. Display Single Contact\n6. Exit")
    choice=int(input("Enter a choice : "))
    #creat contact condition checks if number is already present or else insert data using create function
    if choice==1:
        number=input("Enter Mobile Number: ")
        if(findnumber(number)!=-1):
            print(f"{number} contact already Exists")
        else:
            name,email=input("Enter Name:"),input("Enter Email:")
            create(number,name,email)
    #update contact condition checks if number is present or not and then updates the required information of particular number        
    elif choice==2:
        number=input("Enter Mobile Number: ")
        idx=findnumber(number)
        if(idx==-1):
            print(f"{number} Contact Doesnt Exists to Update")
        else:
            with open("Contact.csv","r") as c:
                l=c.readlines()
            number,name,email=l[idx].split(",")
            delete(idx)
            while 1:
                print("\n\t1. Name\n\t2. Email\n\t3. Mobile Number\n\t4. Exit")
                upch=int(input("Enter a choice:"))
                if upch==1:
                    name=input(f"Old name: {name}\nEnter New Name: ")
                    print(f"{name} is updated to a contact")
                elif upch==2:
                    email=input(f"Old Email: {email[:-2]}\nEnter New Mail: ")
                elif upch==3:
                    number=input(f"Old Number: {number}\nEnter New Number: ")
                elif upch==4:
                    break
                else:
                    print("Invalid choice!")
            create(number,name,email)
            print(f"Updated Successfully for {number}")
    #delete contact condition checks if number is present or not and then delete the contact
    elif choice==3:
        number=input("Enter Mobile Number: ")
        idx=findnumber(number)
        if(idx==-1):
            print(f"{number} Contact Doesnt Exist to Delete")
        else:
            delete(idx)
            print("Contact is Deleted Successfully")
    #Displays all the contacts in the csv file
    elif choice==4:
        with open("Contact.csv","r") as c:
            l=c.readlines()
            if len(l)==0:
                print("Contact List is Empty")
            else:
                print(*l)
    #displays particlar contact in the csv file
    elif choice==5:
        number=input("Enter Mobile Number: ")
        idx=findnumber(number)
        if(idx==-1):
            print(f"{number} Contact Doesnt Exist")
        else:
            with open("Contact.csv","r") as c:
                l=c.readlines()
                l2=l[idx].split(",")
                print(f"Contact Name: {l2[1]}\nEmail: {l2[2][:-1]}\nMobile: {l2[0]}")
    #termination condition
    elif choice==6:
        break
    else:
        print("Invalid choice!")
print("Thanks for Using Contact File")

#Created by Pavan Vitesh Kuncham
