
print("Welcome to Train Ticket Booking System")
total=60
seats=total
while True:

    print("1. Available Trains" )
    print("2. Book Ticket")
    print("3. Ticket cancellation")
    print("4. Exit")
    print("Enter your choice: ")
    choice = int(input("Choice: "))
    if(choice == 1):
        print("----------------------")
        print("Available Trains:")
        print("704 - Intercity Express - From Goa to Mumbai")
        print("Departure Time: 10:00 AM")
        print("Arrival Time: 04:00 PM")
        seat=60-seats
        print("Total Seats: ", seats)
        print("----------------------")

    elif choice == 2:
        print("----------------------")
        print("Book Ticket")
        train_no = int(input("Enter train number: "))
        if train_no == 704 and seats >0:
            print("Available seats: ",seats)
            n=int(input("Number of passenger to book a ticket: "))
            if n<=seats and n>0:
                names=[]
                for i in range(n):
                    while True:
                        name=input(f"Enter name {i+1}: ")
                        if name.isalpha():
                                names.append(name)
                                break
                        else:
                                print("INVALID NAME !, Use only letters")  
            seats-=n
            print("Collected names  ",names)     
            print("Total seats booked: ",n)
            print("Ticket booked successfully!")
            print("Remaining seats:", seats) 
            print("----------------------")
        else:
            print("Invalid train number")
            print("----------------------")
    elif choice == 3:
        print("----------------------")
        print("Ticket Cancellation")
        train_no = int(input("Enter train number: "))
        seats = int(input("Enter seats to cancel: "))
        if train_no == 704:
            print("Ticket cancelled successfully!")
            rem=60 -seats
            print("Remaining seats:", rem) 
        else:
            print("Cancellation failed")
        print("----------------------")    
    else:
        print("Exiting the system. Thank you!")
        print("----------------------")
        break
                  