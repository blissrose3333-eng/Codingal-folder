def calculate_due():
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid by the customer: "))

    if amount_paid < total_bill:
        due_amount = total_bill - amount_paid
        print(f"The customer still owes: ${due_amount:.2f}")
    elif amount_paid > total_bill:
        change = amount_paid - total_bill
        print(f"Payment successful. Return change: ${change:.2f}")
    else:
        print("Bill paid in full. No balance due.")
calculate_due()