class Product:
    """
    Class representing the product in shop
    """

    def __init__(self, barcode):
        """
        Sets all the necessary attributes for the class Product
        :param barcode: stroke of the product
        """

        self.__barcode = barcode
        self.__country = None
        self.__name = None
        self.__price = None

    def set_country(self, country):
        """
        Method of setting country
        :param country:
        :return:
        """

        self.__country = country

    def set_name(self, name):
        """
        Method of setting name
        :param name:
        :return:
        """

        self.__name = name

    def set_price(self, price):
        """
        Method of setting price
        :param price:
        :return:
        """

        self.__price = price

    def get_barcode(self):
        """
        Method of getting barcode
        :return: barcode
        """

        return self.__barcode

    def get_country(self):
        """
        Method of getting country
        :return: country
        """

        return self.__country

    def get_name(self):
        """
        Method of getting name
        :return: name
        """

        return self.__name

    def get_price(self):
        """
        Method of getting price
        :return: price
        """

        return self.__price


class Basket:
    """
    Class representing basket in the shop
    """

    def __init__(self):
        """
        Sets all the necessary attributes for the class Basket
        """

        self.__products = []
        self.__total_price = 0

    def add_product(self, product):
        """
        Method of adding new product in the basket
        :param product:
        :return:
        """

        self.__products.append(product)
        self.__total_price += product.get_price()

    def remove_product(self, barcode):
        """
        Method of removing the product from the basket
        :param barcode:
        :return:
        """

        for product in self.__products:
            if product.get_barcode() == barcode:
                self.__products.remove(product)
                self.__total_price -= product.get_price()

    def get_total_price(self):
        """
        Method of returning total price of the basket
        :return: total price of the basket
        """

        return self.__total_price

    def load_data(self, file_name):
        """
        Method of loading data from file
        :param file_name:
        :return:
        """

        with open(file_name, 'r', encoding='utf8') as f_in:
            for ptr in f_in:
                ptr = ptr.split()
                product = Product(ptr[0])
                product.set_country(ptr[1])
                product.set_name(ptr[2])
                product.set_price(float(ptr[3]))
                self.add_product(product)

    def save_data(self, file_name):
        """
        Method of saving data in file
        :param file_name:
        :return:
        """

        data = []
        for product in self.__products:
            data.append(f'{product.get_barcode()} {product.get_country()} {product.get_name()} {product.get_price()}')

        with open(file_name, 'w') as f_out:
            print(data, file=f_out)
