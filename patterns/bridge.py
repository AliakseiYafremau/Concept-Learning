from abc import abstractmethod, ABC


class Device(ABC):
    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, volume) -> None:
        pass


class Remote(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def increment_volume(self) -> None:
        pass

    @abstractmethod
    def decrease_volume(self) -> None:
        pass


class SamsungTV(Device):
    def __init__(self):
        self.volume = 0

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, volume) -> None:
        if not (0 <= volume <= 100):
            raise ValueError
        self.volume = volume


class SamsungRemote(Remote):
    def increment_volume(self):
        self.device.set_volume(self.device.get_volume() + 5)

    def decrease_volume(self):
        self.device.set_volume(self.device.get_volume() - 5)


class AndroidRemote(Remote):
    def increment_volume(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def decrease_volume(self):
        self.device.set_volume(self.device.get_volume() - 10)


device = SamsungTV()
samsung_remote = SamsungRemote(device=device)
android_remote = AndroidRemote(device=device)


samsung_remote.increment_volume()
samsung_remote.increment_volume()
samsung_remote.increment_volume()
samsung_remote.increment_volume()
print(device.get_volume())
android_remote.decrease_volume()
android_remote.decrease_volume()
print(device.get_volume())
