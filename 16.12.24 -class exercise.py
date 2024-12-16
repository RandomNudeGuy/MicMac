
def buy_item(product, amount):
    if product in shop:
        if amount <= shop[product]:
            if product not in cart:
                shop[product] -= amount
                cart[product] = amount
                print(f"{amount} {product}s bought!")
            else:
                shop[product] -= amount
                cart[product] += amount
                print(f"{amount} {product}s bought!")
        else:
            exeption_amount = Exception(f"Not enough {product}s in the shop!")
            raise exeption_amount

    else:
        exeption_product = Exception(f"We don't sell {product}s in the shop!")
        raise exeption_product


if __name__ == '__main__':
    shop = {"banana": 5,
            "apple": 3,
            "kiwi": 10,
            "potatoe": 7,
            "strawberry": 1
            }

    cart = {}
    try:
        buy_item("apple", 1)
        buy_item("apple", 1)
    except Exception as e:
        print("No can do!")
        print(e)

    print(f"Cart: {cart}")
