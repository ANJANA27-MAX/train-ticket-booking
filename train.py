trains = {
    101: {"name": "Chennai Express", "seats": 50},
    102: {"name": "Bangalore Mail", "seats": 40}
}

print("Available Trains:")
for t in trains:
    print(t, trains[t]["name"], "- Seats:", trains[t]["seats"])

train_no = int(input("Enter train number: "))
seats = int(input("Enter seats to book: "))

if train_no in trains and trains[train_no]["seats"] >= seats:
    trains[train_no]["seats"] -= seats
    print("Ticket booked successfully!")
else:
    print(" Booking failed")
