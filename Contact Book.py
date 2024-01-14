print("\t\t\t\t\t\tContact Book")
contact_list = []
c = 0

while True:
    print("Press 1 if you want to add Contact")
    print("Press 2 if you want to View all Contacts")
    print("Press 3 if you want to Search any Contact")
    print("Press 4 if you want to update any existing Contact")
    print("Press 5 if you want to delete any Contact")
    print("Press 0 to exit\n")

    u1 = int(input(""))

    if u1 == 0:
        print("Have a nice day :)")
        break  

    if u1 == 1:
        ch = "0"
        while ch == "0":
            try:
                contact_book = {
                    "Name": str(input("Name:\n")),
                    "Phone Number": int(input("Phone Number:\n")),
                    "Email": str(input("Email:\n")),
                    "Address": input("Address:\n"),
                }
                contact_list.append(contact_book)
                c += 1
                ch = str(input("Enter 0 if you want to include more names else press any key to exit:\n"))
            except ValueError as v:
                print(v)
            except:
                print("An error occurred\n")
            else:
                for i in contact_list:
                    print(i)
                print(f'Total contacts in list = {c}\n')

    elif u1 == 2:
        if not contact_list:
            print("No contacts found\n")
        else:
            print("\t\t\tAll Contacts List")
            for contact in contact_list:
                print("Name:", contact["Name"])
                print("Phone Number:", contact["Phone Number"])
                print("Email:", contact["Email"])
                print("Address:", contact["Address"])
                print("\n")

    elif u1 == 3:
        print("\nPress 1 for searching by name\nPress 2 for searching by number\n")
        u01 = int(input())

        found_contacts = []

        try:
            if u01 == 1:
                u02 = input("Enter Name:\n").lower()
                for contact in contact_list:
                    if u02 in contact["Name"].lower():
                        found_contacts.append(contact)

            elif u01 == 2:
                u03 = int(input("Enter Number:\n"))
                for contact in contact_list:
                    if u03 == contact["Phone Number"]:
                        found_contacts.append(contact)

        except Exception as e:
            print("An error occurred:", e)
        else:
            if found_contacts:
                for contact in found_contacts:
                    print("\nName:", contact["Name"])
                    print("Phone Number:", contact["Phone Number"])
                    print("Email:", contact["Email"])
                    print("Address:", contact["Address"])
                    print("\n")
            else:
                print("No contacts found\n")

            
    elif u1 == 4:
        u001 = input("Enter name of contact:\n").lower()
        found = False

        for contact in contact_list:
            if u001 == contact["Name"].lower():
                try:
                    contact_book = {
                        "Name": str(input("New Name:\n")),
                        "Phone Number": int(input("New Phone Number:\n")),
                        "Email": str(input("New Email:\n")),
                        "Address": input("New Address:\n"),
                    }
                    contact_list.remove(contact)
                    contact_list.append(contact_book)
                    found = True
                    print("Contact Updated Successfully\n")
                except ValueError as v:
                    print("Value Error Occurred\n", v)
                except:
                    print("An Error Occured\n")
                
        if not found:
            print("No Contact found")
                            
    elif u1 == 5:
        u002 = input("Enter Name of contact:\n").lower()
        found = False

        for contact in contact_list:
            try:
                if u002 == contact["Name"].lower():
                    contact_list.remove(contact)
                    found = True
                    print("Contact Deleted Successfully\n")
                    break                                  
            except Exception as e:
                print("An error occurred:", e)
        if not found:
            print("No Contact found")