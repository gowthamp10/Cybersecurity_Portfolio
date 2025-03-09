"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

customer_basket_cost = 101
customer_basket_weight = 44

# Write if statement here to calculate the total cost
if customer_basket_cost > 100:
    print("Customer spent over $100, hence they get free shipping")
    print(f"Customer spent:        ${customer_basket_cost}")
    print(f"Shipping charge:       $0")
    print(f"Customer total charge: ${customer_basket_cost}")
else: 
    shipping_charge = customer_basket_weight * 1.20
    print(f"Customer spent:         ${customer_basket_cost}")
    print(f"Shipping charge:        ${shipping_charge}")
    total_charge = customer_basket_cost + shipping_charge
    print(f"Customer total charge:  ${total_charge} ")

"""
Solution provided and modified:
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

    ===> You've redeemed a hint. Replace the X's with code to complete this exercise.


shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost = customer_basket_cost + shipping_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))

"""





