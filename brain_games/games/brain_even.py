from random import randint

from brain_games import cli


def run():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()

    rounds = 3
    correct_answers = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    print()

    while correct_answers < rounds:
        number = randint(1, 100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'

        print(f'Question: {number}')
        user_answer = cli.get_user_answer()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            message = "'{wrong}' is wrong answer ;(. " \
                      "Correct answer was '{correct}'."
            print(message.format(wrong=user_answer, correct=correct_answer))
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}')
