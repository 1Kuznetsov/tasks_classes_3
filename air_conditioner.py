class AirConditioning:
    """
    Class representing air conditioner condition
    """

    def __init__(self):
        """
        Sets all the necessary attributes for the class AirConditioning
        """

        self.__status = False
        self.__temperature = None

    @property
    def status(self):
        """
        status getter
        :return: status
        """

        return self.__status

    @property
    def temperature(self):
        """
        temperature getter
        :return: temperature
        """

        return self.__temperature

    @status.setter
    def status(self, value):
        self.__status = self.__status

    @temperature.setter
    def temperature(self, value):
        self.__temperature = self.__temperature

    def switch_on(self):
        """
        Method turning status of conditioner on
        :return:
        """

        if self.__status is False:
            self.__status = True
            self.__temperature = 18

    def switch_off(self):
        """
        Method turning status of conditioner off
        :return:
        """

        if self.__status is True:
            self.__status = False
            self.__temperature = None

    def reset(self):
        """
        Method restarting turned conditioner
        :return:
        """

        if self.__status:
            self.switch_off()
            self.switch_on()

    def get_temperature(self):
        """
        Method of getting temperature
        :return: temperature
        """

        return self.__temperature

    def raise_temperature(self):
        """
        Method of incrementing temperature
        :return:
        """

        if self.__temperature is not None and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        """
        Method of decrementing temperature
        :return:
        """

        if self.__temperature is not None and self.__temperature > 0:
            self.__temperature -= 1

    def __repr__(self):
        """
        Method of representing data of class
        :return:
        """

        if self.__status is True:
            return f'Conditioner is on. Temperature mode: {self.__temperature} degrees'
        else:
            return 'Conditioner is off'
