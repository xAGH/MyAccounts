from src.config import APP
from datetime import datetime

# Function to get the current time
def time():
    return datetime.now().strftime(APP.TIME_FORMAT)

# Function to validate the data according to the class schema
def validate_input(sender, content):
    errors = sender.validator.validate(content)
    if errors:
        return (
            [
                {
                    "response": errors
                },
                400
            ],
            False
        )
    
    return content, True
