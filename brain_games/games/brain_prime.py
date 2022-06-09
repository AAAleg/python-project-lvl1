from random import randint, choice

from brain_games import cli


def run():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:
        number = randint(1, 100)

        expression = f"{number}"

        correct_answer = "yes" if is_prime(number) else "no"

        print(f'Question: {expression}')

        user_answer = cli.get_user_answer()

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            message = "'{wrong}' is wrong answer ;(. " \
                      "Correct answer was '{correct}'."
            print(message.format(wrong=user_answer, correct=correct_answer))
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}')


def is_prime(number):
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True
