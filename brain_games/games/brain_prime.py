from brain_games.tools import generate_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play():
    number = generate_number()
    question = f'Question: {number}'
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def is_prime(number):
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True
