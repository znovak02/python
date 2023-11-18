import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    
def test_power():
    tv = Television()
    tv.power()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert tv.__str__() != "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    tv.power()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"
    tv.mute()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"


def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"
    for _ in range(3):
        tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    for _ in range(1):
        tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    

def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    for _ in range(1):
        tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"


def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    for _ in range(2):
        tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"

