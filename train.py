
print("Welcome to Train Ticket Booking System")
while True:

    print("1. Available Trains" );
    print("2. Book Ticket");
    print("3. Ticket cancellation");
    print("4. Exit");
    print("Enter your choice: ");
    choice = int(input("Choice: "));
    if(choice == 1):
        print("Available Trains:");
        print("704 - Intercity Express - Seats: 60");

    elif choice == 2:
        train_no = int(input("Enter train number: "))
        print("total seats:60")
        seats = int(input("Enter number of seats to book: "))
        if train_no == 704 and seats <= 60:
            print("Ticket booked successfully!")
        else:
            print("Booking failed")
        rem=60 - seats
        print("Remaining seats:", rem) 
    elif choice == 3:
        train_no = int(input("Enter train number: "))
        seats = int(input("Enter seats to cancel: "))
        if train_no == 704:
            print("Ticket cancelled successfully!")
            rem=60 + seats
            print("Remaining seats:", rem) 
        else:
            print("Cancellation failed")
    else:
        print("Exiting the system. Thank you!")
        break
                  