# trains = {
#     101: {"name": "Chennai Express", "seats": 50},
#     102: {"name": "Bangalore Mail", "seats": 40}
# }

# print("Available Trains:")
# for t in trains:
#     print(t, trains[t]["name"], "- Seats:", trains[t]["seats"])

# train_no = int(input("Enter train number: "))
# seats = int(input("Enter seats to book: "))

# if train_no in trains and trains[train_no]["seats"] >= seats:
#     trains[train_no]["seats"] -= seats
#     print("Ticket booked successfully!")
# else:
#     print(" Booking failed")
print("Enter your choice")
print("1. Available Trains" )
print("2. Book Ticket")
print("3. Ticket cancellation")
print("4. Exit")

choice = int(input("Choice: "))
if choice == 1:
    print("Available Trains:")
    print("704 - Intercity Express - Seats: 60")

elif choice == 2:
    train_no = int(input("Enter train number: "))
    print("total seats:60")
    seats = int(input("Enter seats to book: "))
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
elif choice == 4:
    print("Exiting the system.") 
else:  
    print("Invalid choice.")
