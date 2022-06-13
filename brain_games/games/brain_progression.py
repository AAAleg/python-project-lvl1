from random import choice

from brain_games.tools import generate_number


DESCRIPTION = "What number is missing in the progression?"
MAX_LENGTH = 10


def make_progression():
    initial_number = generate_number()
    delta = generate_number()
    maximum_number = (delta * MAX_LENGTH) + initial_number
    return range(initial_number, maximum_number, delta)


def play():
    prog = make_progression()
    correct_answer = choice(prog)
    progression = ' '.join([
        '..' if num == correct_answer else str(num) for num in prog
    ])
    question = f"Question: {progression}"
    return question, str(correct_answer)
