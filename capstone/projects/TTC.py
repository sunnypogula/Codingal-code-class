# 1. Store travel booking details (Data Types)
destination = "Paris"  # String (text)
num_tickets = 3  # Integer
ticket_price = 150.50  # Float (decimal)
is_vip = True  # Boolean

print(f"Booking Destination: {destination}")

# 2. Calculate total ticket cost (Operators)
total_cost = num_tickets * ticket_price
print(f"Total Ticket Cost for {num_tickets} tickets: ${total_cost:.2f}")

# 3. Compare values (Comparison Operators)
is_budget_friendly = total_cost < 500
print(f"Is total cost under $500? {is_budget_friendly}")

# 4. Swap two ticket prices to understand updating variables
bus_ticket = 45.0
train_ticket = 85.0

print(f"\nBefore Swap -> Bus: ${bus_ticket}, Train: ${train_ticket}")

# Swapping values in Python
bus_ticket, train_ticket = train_ticket, bus_ticket

print(f"After Swap  -> Bus: ${bus_ticket}, Train: ${train_ticket}")