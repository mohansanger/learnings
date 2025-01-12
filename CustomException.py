class invalidAgeException(Exception):
    "Raised when the age is less than 18"
    pass

number=18

try:
    input_number=int(input("Enter +ive Intiger :"))
    if input_number < number:
        raise invalidAgeException
    else:
        print("You are eligable for vote")
except invalidAgeException:
    print("Exception Error: Invalid Age")


