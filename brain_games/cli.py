import prompt


def welcome_user():
    name = get_user_name()
    print(f"Hello, {name}!")
    return name


def get_user_name():
    return prompt.string("May I have your name? ")


def get_user_answer():
    return prompt.string('Your answer: ')
