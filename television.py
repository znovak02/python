class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False  # Setting Television off by default
        self.__muted = False   # Television is not muted by default
        self.__volume = Television.MIN_VOLUME  # Set volume to minimum by default
        self.__channel = Television.MIN_CHANNEL  # Set channel to minimum by default

    def power(self):
        self.__status = self.__status == False  # Setting the power status

    def mute(self):
        if self.__status == True:  # Change mute status when and if TV is on
            self.__muted = self.__muted == False

    def channel_up(self):
        if self.__status == True:  # Only change channel if TV is on
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status == True:  # Only change channel if TV is on
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        self.__muted = False # :FIXME: We are going to try to get rid of mute when we turn up and down the volume
        if self.__status == True:  # Only increase volume if TV is on
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self):
        self.__muted = False# :FIXME: We are going to try to get rid of mute when we turn up and down the volume
        if self.__status == True:  # Only decrease volume if TV is on
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self):
        volume_display = self.__volume if self.__muted == False else 0 # Setting whether or not mute is activated without having to change value of volume variable
        return f"Power = {'True' if self.__status else 'False'}, Channel = {self.__channel}, Volume = {volume_display}"

