from random import randint, choice

from brain_games import cli


def run():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()

    print("What number is missing in the progression?")

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:
        initial_number = randint(1, 100)
        delta = randint(1, 25)
        length = 10
        maximum_number = (delta * length) + initial_number
        prog = range(initial_number, maximum_number, delta)

        correct_answer = choice(prog)
        progression = ' '.join([
            '..' if num == correct_answer else str(num) for num in prog
        ])

        expression = f"{progression}"

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


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)
