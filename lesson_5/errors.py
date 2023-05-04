class RequiredFieldsMissingError(Exception):
    def __str__(self):
        return "Invalid message received"

