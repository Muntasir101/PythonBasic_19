user_type = input("Enter User Type: ")
item_type = input("Enter Item Type: ")
discount_code = input("Discount Code: ")
purchase_amount = int(input("Purchase Amount: "))

# 10% discount
discount = 10

if user_type == "regular" or user_type == "premium":
    if item_type == "e" or item_type == "c" or item_type == "b":
        if discount_code == "BD19":
            discount_amount = (purchase_amount * discount) / 100
            final_amount = purchase_amount - discount_amount
            print("Coupon Applied.Discounted amount You have to pay: :", final_amount)
        else:
            print("User type and Item Type Valid but Coupon Code Invalid.No Discount !!You have to pay: ", purchase_amount)
    else:
        print("User type valid but Item Type Invalid. No Discount !!You have to pay: ", purchase_amount)
else:
    print("User Type Invalid. No Discount !! You have to pay: ", purchase_amount)
