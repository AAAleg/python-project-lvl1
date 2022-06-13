from brain_games.cli import welcome_user, get_user_answer


MAX_ATTEMPTS = 3
wrong_answer_message = "'{wrong}' is wrong answer ;(." \
                       " Correct answer was '{correct}'."
finish_message = "Let's try again, {name}!"
right_answer_message = "Correct!"
congrats = "Congratulations, {name}!"


def run(game=None):
    print("Welcome to the Brain Games!")

    if game is not None:
        print(game.DESCRIPTION)

    user_name = welcome_user()

    if game is not None:
        runner(user_name, game.play)


def runner(user_name, play):
    correct_answers = 0
    while correct_answers < MAX_ATTEMPTS:
        question, correct_answer = play()
        print(question)
        is_correct, message = check_answer(get_user_answer(), correct_answer)
        print(message)
        if not is_correct:
            print(finish_message.format(name=user_name))
            return
        correct_answers += 1

    print(congrats.format(name=user_name))


def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True, right_answer_message
    return False, wrong_answer_message.format(wrong=answer,
                                              correct=correct_answer)
