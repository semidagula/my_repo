from abc import ABC, abstractmethod


class CarModel(ABC):
    @abstractmethod
    def volan(self):
        raise NotImplemented

    @abstractmethod
    def roti(self):
        raise NotImplemented

    @abstractmethod
    def scaune(self):
        raise NotImplemented

    def sistem_audio(self):
        print('Avem sistem audio')