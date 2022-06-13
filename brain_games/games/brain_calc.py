from random import choice
import operator

from brain_games.tools import generate_number


DESCRIPTION = "What is the result of the expression?"

operations = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def play():
    number1 = generate_number()
    number2 = generate_number()
    symbol, operation = choice(operations)
    correct_answer = operation(number1, number2)
    question = f"Question: {number1} {symbol} {number2}"
    return question, str(correct_answer)
