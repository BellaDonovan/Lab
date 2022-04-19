class Television:
    """
    A class used to turn a TV on/off and change the volume/channel
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create the initial state of the TV
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to turn the tv on/off
        :return: If the TV is on or off
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to increase the TV channel
        :return: Current TV channel
        """

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the TV channel
        :return: Current TV channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel <= Television.MAX_CHANNEL:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the TV volume
        :return: Current TV volume
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = self.__volume

    def volume_down(self) -> None:
        """
        Method to decrease the TV volume
        :return: Current TV volume
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = self.__volume
            elif self.__volume <= Television.MAX_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to print the volume, channel, and status (on/off) of the TV
        :return: Printed status, volume, and channel of the TV
        """
        return (f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}')