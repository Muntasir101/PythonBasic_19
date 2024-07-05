amount_before_purchase = 1000

phone_price = 200
food_price = 300
transport_cost = 100

# addition
total_cost = phone_price + food_price + transport_cost
print(total_cost)

# 10% discount apply
discount = 20

discount_amount = (total_cost * discount) / 100
print(discount_amount)

final_amount = total_cost - discount_amount
print(final_amount)

# subtract
remaining_amount = amount_before_purchase - total_cost
print(remaining_amount)
