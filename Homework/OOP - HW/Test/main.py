from item import Item
from order import Order
from customer import Customer
from regular_order import RegularOrder
from vip_order import VIPOrder
from datetime import date
from gift import Gift

if __name__ == '__main__':
    item1 = Item(1, "Laptop", 3000)
    item2 = Item(2, "Mouse", 100)
    item3 = Item(3, "Keyboard", 200)
    gift = Gift("Free Speaker!")



    regular_customer = Customer(101, "Jonathan", "Tzur", "jonathant@email.com", "Massad", "REGULAR")
    vip_customer = Customer(102, "Ben", "Meir", "benm@email.com", "Tel Aviv", "VIP", 20)

    regular_order = RegularOrder(201, "Jonathan Order", "Massad", [item1, item2], regular_customer, "CREDIT CARD", date.today())
    print(f"Regular order total: {regular_order.total_price}")

    vip_order = VIPOrder(202, "Bob Order", "456 VIP Ave", [item1, item3], vip_customer, "CASH", date.today())
    print(f"VIP order total (with discount): {vip_order.total_price}")

    print(len(regular_customer.favorite_items))
    regular_customer.remove_fav(item1)
    print(len(regular_customer.favorite_items))
    regular_customer.add_fav(item1)
    print(len(regular_customer.favorite_items))

    print(regular_customer.open_gift())
    regular_customer.give_gift(gift)
    print(regular_customer.open_gift())

