total = 0
americano = 4500
latte = 5500
chamomile = 7000

beverages = ["Americano", "Latte", "Chamomile"]
beverages_price = [americano, latte, chamomile]

user_menu = int(input("Americano-0 / Latte-1 / Chamomile-2 :"))
quantity = int(input("How many cups? "))

total += beverages_price[user_menu] * quantity
# total = total + beverages_price[user_menu] * quantity


print(f"Ordered {quantity} cup(s) of {beverages[user_menu]}.")
print(f"Total price: {total}")