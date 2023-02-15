def shopping_cart(*data):
    products = {'Soup': [], 'Pizza': [], 'Dessert': []}
    products_limits = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    added_products = False

    for current_data in data:
        if current_data == 'Stop':
            break

        meal, product = current_data

        if meal in products and product not in products[meal]:
            if len(products[meal]) < products_limits[meal]:
                products[meal].append(product)
                added_products = True

    if added_products:
        result = ''
        sorted_data = sorted(products, key=lambda s: (-len(products[s]), s))
        for key in sorted_data:
            result += f'{key}:\n'
            for value in sorted(products[key]):
                result += f' - {value}\n'

        return result

    return "No products in the cart!"


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
