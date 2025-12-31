
print("Welcome to Train Ticket Booking System")
seats=0
while True:

    print("1. Available Trains" )
    print("2. Book Ticket")
    print("3. Ticket cancellation")
    print("4. Exit")
    print("Enter your choice: ")
    choice = int(input("Choice: "))
    if(choice == 1):
        seat = 60
        print("----------------------")
        print("Available Trains:")
        print("704 - Intercity Express - From City goa to City mumbai")
        print("Departure Time: 10:00 AM")
        print("Arrival Time: 04:00 PM")
        seat=60-seats
        print("Total Seats: ", seat)
        print("----------------------")

    elif choice == 2:
        print("----------------------")
        print("Book Ticket")
        train_no = int(input("Enter train number: "))
        print("total seats:60")
        seats = int(input("Enter number of seats to book: "))
        if train_no == 704 and seats <= 60:
            print("Ticket booked successfully!")
        else:
            print("Booking failed")
        rem=60 - seats
        print("Remaining seats:", rem) 
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
                  