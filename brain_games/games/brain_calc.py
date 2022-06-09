from random import randint, choice
import operator

from brain_games import cli

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def run():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()

    print("What is the result of the expression?")

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        op = choice(list(operations.keys()))

        correct_answer = operations[op](number1, number2)

        expression = f"{number1} {op} {number2}"

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
