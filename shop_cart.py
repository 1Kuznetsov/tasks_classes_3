class Product:
    def __init__(self, barcode):
        self.__barcode = barcode
        self.__country = None
        self.__name = None
        self.__price = None

    def set_country(self, country):
        self.__country = country

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def get_barcode(self):
        return self.__barcode

    def get_country(self):
        return self.__country

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class Basket:
    def __init__(self):
        self.__products = []
        self.__total_price = 0

    def add_product(self, product):
        self.__products.append(product)
        self.__total_price += product.get_price()

    def remove_product(self, barcode):
        for product in self.__products:
            if product.get_barcode() == barcode:
                self.__products.remove(product)
                self.__total_price -= product.get_price()

    def get_total_price(self):
        return self.__total_price

    def load_data(self, file_name):
        with open(file_name, 'r', encoding='utf8') as f_in:
            for ptr in f_in:
                ptr = ptr.split()
                product = Product(ptr[0])
                product.set_country(ptr[1])
                product.set_name(ptr[2])
                product.set_price(int(ptr[3]))
                self.add_product(product)

    def save_data(self, file_name):
        data = []
        for product in self.__products:
            data.append(f'{product.get_barcode()} {product.get_country()} {product.get_name()} {product.get_price()}')

        with open(file_name, 'w') as f_out:
            print(data, file=f_out)
