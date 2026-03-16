from abc import ABC , abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to : str, message: str):
        pass


class PushNotification(NotificationService):
    pass

obj = PushNotification()
obj.send("1" , "2")


# this will raise an error because PushNotification is not implemented
# type error : cant instantiate abstract class PushNotification with abstract method send


obj = NotificationService()
obj.send("1" , "2")

# this will raise an error because NotificationService is an abstract