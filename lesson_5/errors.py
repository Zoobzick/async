class RequiredFieldsMissingError(Exception):
    def __str__(self):
        return "Invalid message received"


class IncorrectDataRecievedError(Exception):
    def __str__(self):
        return "Incorrect data recieved"
