class AirConditioning:
    """

    """

    def __init__(self):
        self.__status = False
        self.__temperature = None

    @property
    def status(self):
        return self.__status

    @property
    def temperature(self):
        return self.__temperature

    @status.setter
    def status(self, value):
        self.__status = self.__status

    @temperature.setter
    def temperature(self, value):
        self.__temperature = self.__temperature

    def switch_on(self):
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        self.__status = False
        self.__temperature = None

    def reset(self):
        if self.__status:
            self.switch_off()
            self.switch_on()

    def get_temperature(self):
        return self.__temperature

    def raise_temperature(self):
        if self.__temperature is not None and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        if self.__temperature is not None and self.__temperature > 0:
            self.__temperature -= 1

    def __repr__(self):
        if self.__status == True:
            return f'Conditioner is on. Temperature is {self.__temperature}'
        else:
            return 'Conditioner is off'
