# CHAPTER 1: WHAT IS RECURSION?


def count_down_and_up(number):
    print(number, "counting down")
    # BASE CASE
    if number == 0:
        print("Reached the base case.")
        return

    # RECURSIVE CASE
    count_down_and_up(number - 1)
    print(number, "counting up")
    return


count_down_and_up(3)
