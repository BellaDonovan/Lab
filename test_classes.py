
from classes import *

class Test:
    def setup_method(self):
        self.T1 = Television()

    def test___init__(self):
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.T1.power()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.T1.power()
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.T1.channel_up()
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.T1.power()
        self.T1.channel_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.T1.channel_up()
        self.T1.channel_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.T1.channel_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.T1.channel_down()
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.T1.power()
        self.T1.channel_down()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.T1.channel_down()
        self.T1.channel_down()
        self.T1.channel_down()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.T1.volume_up()
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.T1.power()
        self.T1.volume_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.T1.volume_up()
        self.T1.volume_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.T1.volume_down()
        assert self.T1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.T1.power()
        self.T1.volume_up()
        self.T1.volume_up()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.T1.volume_down()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.T1.volume_down()
        self.T1.volume_down()
        assert self.T1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'


