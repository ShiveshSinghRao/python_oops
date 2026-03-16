"""
Why use abstraction?

- To hide the implementation details
- To provide a simple interface to the client
- To make the code more maintainable
- To make the code more readable
- To make the code more testable
- To make the code more maintainable
- To make the code more readable
- To make the code more testable
"""


class EmailService:
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} with subject {subject} and body {body}")


class SMSService:
    def send_sms(self, to: str, message: str):
        print(f"Sending SMS to {to} with message {message}")


# this is a code we have to write and maintain without abstraction
# if we want to add a new feature, we have to modify the code


# diffrent method names and hard to scale and no rule


