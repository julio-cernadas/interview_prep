def count_down_and_up(number):
    print(number, "counting down")
    # base case
    if number == 0:
        print("Reached the base case.")
        return

    # recursive case
    count_down_and_up(number - 1)
    print(number, "counting up")
    return


count_down_and_up(3)
