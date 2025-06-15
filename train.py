# Train ticket booking
print ("Available seats are 30")
print("If you want to Quit the services enter 101")
x=30
#x= no of seats available in total
#y= no of seats the user wants to book
#c= no of seats remaining after booking

while True:
 
  y= int(input("Enter the number of seats you want to book: "))

  if(y==101):
       break
  if(y<x):
    c=x-y
    print("Dear user you have booked the seats successfully")
    print("THANK YOU , COME AGAIN")
    print ("The remaining seats after booking is: ",c)
  else:
    print("You exceeds the available seats, sorry") 



