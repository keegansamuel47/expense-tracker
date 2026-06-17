expense = input("what did you spend money on? ")
price = float(input("how much? "))
expense_2 = input("what else did you spend on? ")
second_price = float(input("how much for the second expense? "))

total = 0
if price > 0:
    print(f"Recorded: {expense} - ${price:.2f}")
    total += price
else:
    print("That's not a valid amount.")

if second_price > 0:
    print(f"Recorded: {expense_2} - ${second_price:.2f}")
    total += second_price
else:
    print("That's not a valid amount.")

print(f"Total spent: ${total:.2f}.")


