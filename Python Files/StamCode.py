import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

numbers_to_guess = 4

numbers_generated = random.choices(numbers, k=numbers_to_guess)
numbers_revealed = ["_" for i in range(numbers_to_guess)]

print("Welcome to the number guessing Game!\n")

print(
    "All you need to do is guess the hidden number and the number of correct numbers will appear!\n"
)

play_answer = input("Do you want to play? [Y/N]: ")

attempts_left = 4


def guess_nums() -> list:
    return list(input(f"[{attempts_left} attempts left] Enter 4 numbers: "))


def output_revealed() -> None:
    print(f'\n {" ".join(numbers_revealed)} \n')


def show_revealed_number(index: int) -> None:
    numbers_revealed.pop(index)
    numbers_revealed.insert(index, numbers_generated[index])


def get_remaining_numbers() -> int:
    remaining = 0

    for number in numbers_generated:
        if number not in numbers_revealed:
            remaining += 1

    return remaining


def exit_message() -> None:
    print("\nYou have no more attempts left!")

    print(f'The numbers were: {" ".join(numbers_generated)}')


def success_message() -> None:
    print("You found all the numbers!")

    print(f'The generated numbers were {" ".join(numbers_generated)}')


if play_answer.lower() != "y":
    exit()

while attempts_left > 0:
    output_revealed()

    numbers_guessed = guess_nums()

    attempts_left -= 1

    # Data sanitization

    # Length chk
    if len(numbers_guessed) != 4:
        if attempts_left == 0:
            exit_message()
            exit()

        print("Invalid guess, try again.")
        continue

    # Loop over generated numbers, check if a number is found
    for index, number in enumerate(numbers_generated):
        if number in list(numbers_guessed):
            show_revealed_number(index)

    remaining_numbers = get_remaining_numbers()

    if remaining_numbers == 0:
        success_message()
        exit()

    if attempts_left == 0:
        exit_message()
