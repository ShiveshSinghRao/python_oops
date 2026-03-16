from abc import ABC , abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to : str, message: str):
        pass


class EmailService(NotificationService):
    def send(self,to : str, message: str):
        print(f"sending Email to {to} with subject {message['subject'] } from message {message['body']}")

class SmsService(NotificationService):
    def send(self, to: str, message : str):
        print(f"sending sms to {to} from message {message}")


def notify(service: NotificationService, to : str, message:str):
    service.send(to, message)


email_message = {"subject": "hello world!", "body": "this is prank test"}

notify(EmailService(), "test@gamil.com",email_message)
notify(SmsService(),"123456", "hello world")