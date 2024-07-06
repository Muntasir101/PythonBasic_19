expected_purchase_amount = 1000

customer_purchase_amount = int(input("Enter Amount: "))

if customer_purchase_amount > expected_purchase_amount:
    print("Free bag")
else:
    print("Thanks")