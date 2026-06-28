# Q111: Write a program to Create ticket booking system.

total_seats = 10
booked_seats = 0

while True:
    print("\n--- Movie Ticket Booking ---")
    print(f"Available Seats Left: {total_seats - booked_seats} / {total_seats}")
    print("1. Book Ticket")
    print("2. View Booking Summary")
    print("3. Exit")
    
    choice = input("Enter selection: ")
    
    if choice == "1":
        requested_seats = int(input("How many tickets do you want to book? "))
        if requested_seats <= (total_seats - booked_seats):
            booked_seats += requested_seats
            cost = requested_seats * 150  # ₹150 per ticket
            print(f"Booking Success! Total cost for {requested_seats} seat(s): ₹{cost}")
        else:
            print("Sorry, not enough seats are available.")
            
    elif choice == "2":
        print("\n--- Booking Summary ---")
        print(f"Total Seats Occupied : {booked_seats}")
        print(f"Total Seats Remaining: {total_seats - booked_seats}")
        
    elif choice == "3":
        break