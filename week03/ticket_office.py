tickets_sold  = 0
total_revenue = 0
free_tickets  = 0

while True:
    customer_name = input("Customer name(or q to quit):")
    if customer_name.lower() == 'q':
        break

    try:
        age = int(input("Age:"))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day(weekday/weekend):").lower()
    if day not in ['weekday', 'weekend']:
        print("Invalid day.")
        continue

    is_student = input("Are you a student? (y/n):").lower()
    if is_student not in ['y', 'n']:
        print("Please enter 'y' for yes or 'n' for no.")
        continue

    is_student = is_student == 'y'

    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

        if age < 6:
            category = "Free"
            final_price = 0.0

        elif age >= 65:
            category = "Senior"
            final_price = base_price * 0.5
        elif 6 <= age <= 12:
            category = "Child"
            final_price = base_price * 0.6
        elif is_student and age <= 25:
            category = "Student"
            final_price = base_price * 0.7
        else:
            category = "standard" 
            final_price = base_price

        print(f"{customer_name}: {final_price:.2f} TRY ({category})")

        tickets_sold += 1
        total_revenue += final_price
        if final_price == 0.0:
            free_tickets += 1

            if tickets_sold == 0:
                print("No tickets were sold.")
            else:
                avg_price = total_revenue / tickets_sold
                print(f"Tickets sold: {tickets_sold} Total revenue: {total_revenue:.2f} TRY Average price: {avg_price:.2f} TRY Free tickets: {free_tickets}")
