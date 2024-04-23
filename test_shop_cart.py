from shop_cart import Basket
from shop_cart import Product

basket = Basket()
basket.load_data('products.txt')

while True:
    print('1. Add product to basket')
    print('2. Remove product from basket')
    print('3. View total price')
    print('4. Save data to file')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        barcode = input('Enter product barcode: ')
        country = input('Enter country: ')
        name = input('Enter product name: ')
        price = float(input('Enter product price: '))

        product = Product(barcode)
        product.set_country(country)
        product.set_name(name)
        product.set_price(price)

        basket.add_product(product)

    elif choice == '2':
        barcode = input('Enter product barcode to remove: ')
        basket.remove_product(barcode)

    elif choice == '3':
        print('Total price: $', basket.get_total_price())

    elif choice == '4':
        basket.save_data('basket.txt')

    elif choice == '5':
        break
