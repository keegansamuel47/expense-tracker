expense = input("what did you spend money on? ")
price = float(input("how much? "))
expense_2 = input("what else did you spend on? ")
second_price = float(input("how much for the second expense? "))

print(f"Recorded: {expense} - ${price:.2f}")
print(f"Recorded: {expense_2} - ${second_price:.2f}")
print(f"Total spent: ${price + second_price:.2f}.")
