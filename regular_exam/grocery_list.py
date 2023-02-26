def shop_from_grocery_list(budget, grocery_list, *data):
    products = {}
    purchased_item = []

    for item in data:
        if item[0] in products:
            continue

        product, price = item

        if product not in grocery_list:
            continue
        if product not in products:
            products[product] = price
            if price <= budget:
                purchased_item.append(product)
                budget -= price
            else:
                break

    new_list = list(set(grocery_list).difference(purchased_item))

    purchased_item.sort()
    grocery_list.sort()

    if purchased_item == grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(new_list)}."



# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


