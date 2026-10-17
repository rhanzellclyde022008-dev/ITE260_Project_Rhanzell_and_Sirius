def show_numbers():
    print("Counting from 1 to 5")

    for i in range(1, 6):
        print("Number:", i)


def countdown():
    number = 5

    while number > 0:
        print("Countdown:", number)
        number = number - 1

    print("Countdown finished!")


show_numbers()
countdown()
