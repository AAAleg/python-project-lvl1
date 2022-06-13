from brain_games.tools import generate_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    number = generate_number()
    question = f'Question: {number}'
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
