"""Loose coupling means minimizing dependencies between components of a program.
This makes it easier to change or replace components without affecting the rest
of the system. Loose coupling is often achieved through the use of interfaces or
abstraction layers. In this example we'll see how to apply loose coupling using
dependency injection.

Dependency injection allows a component to receive it's dependencies from an
external source rather than creating them. This makes it easier do change
these dependencies and mock them."""

# First, lets define a Message service that can't deliver the messages in
# different ways depending on the sender.


class MessageService:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message: str) -> None:
        self.sender.send(message)


# Now we can define a couple of classes that implement the send method.
class ChatSender:
    def send(self, message: str) -> None:
        print(f"Sending on chat: {message}")


class MailSender:
    def send(self, message: str) -> None:
        print(f"Sending on mail: {message}")


# In this example MessageService is loosely coupled with both Sender classes
# through dependency injection. This allows us to easily switch between
# different sending mechanisms without having to change the MessageService
# class.
if __name__ == "__main__":
    chat_service = MessageService(ChatSender())
    chat_service.send_message("Hello chat!")

    mail_service = MessageService(MailSender())
    mail_service.send_message("Hello, this is a letter!")
