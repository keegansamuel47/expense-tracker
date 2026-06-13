
expense = input("what did you spend money on? ")
price = float(input("how much? "))
expense_2 = input("what else did you spend on? ")
second_price = float(input("how much for the second expense? "))


if price > 0:
    print(f"Recorded: {expense} - ${price:.2f}")
else:
    print("That's not a valid amount.")

if second_price > 0:
    print(f"Recorded: {expense_2} - ${second_price:.2f}")
else:
    print("That's not a valid amount.")


print(f"Total spent: ${price + second_price:.2f}.")

