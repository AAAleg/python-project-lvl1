from random import randint

from brain_games import cli


def run():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()

    print("What is the result of the expression?")

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        correct_answer = gcd(number1, number2)

        expression = f"{number1} {number2}"

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
