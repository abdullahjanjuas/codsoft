#Contact Book in Python
contact = {}

#Function for displaying contacts
def displaycontact():
    print("Name\t\t\tContact Number,Email Address,Address")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
    

while True:
      
    #User Menu
    choice = int(input("1.Add new contact. \n2.Search contact. \n3.Display Contact. \n4.Edit Contact. \n5.Delete Contact. \n6.Exit. \nEnter your choice:"))
   
   #Allows user to add a new contact   
    if choice == 1:
        name = input("Enter the name:")
        phone = input("Enter the mobile number:")
        email = input("Enter email address:")
        address = input("Enter address:")
        contact[name] = [phone,email,address]
   
    #Allows the user to search for a contact
    elif choice == 2:
          search_name = input("Enter the contact name:")
          if search_name in contact:
              print(search_name,"\'s contact details are:",contact[search_name] )
          else:
              print("Name is not found in contact list")
    
    #Allows user to display contacts in contact list
    elif choice ==3:
        if not contact:
            print("Contact book is empty")
        else:
            displaycontact()
   
    #Allows user to edit contact from contact book
    elif choice ==4:
        edit_contact = input("Enter the contact name you want to edit:")
        if edit_contact in contact:
            phone = input("Enter the new mobile number:")
            email = input("Enter the new email address:")
            address = input("Enter the new address:")
            contact[edit_contact] = [phone,email,address]
            print("Contact details have been updated.")
            displaycontact()
        else:
             print("The entered name does not exist in your contact list.")
    
    #Allows user to delete a contact
    elif choice == 5:
        del_contact = input("Enter the contact name you want to delete:")
        if del_contact in contact:
            confirm = input("Are you sure you want to delete this contact:y/n",del_contact)
            if confirm == 'y':
                contact.pop(del_contact)
                print("Contact Deleted.")
                displaycontact()
            else:
                 print("The entered name does not exist in your contact list.")
                 
        #Ask the user for exit
        elif choice == 6:
            print("Bye!")
            break
    
    
        