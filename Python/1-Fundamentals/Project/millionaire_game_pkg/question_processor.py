from millionaire_game_pkg.question_bank import questions_dict

consumed_questions =[]

# returns next question to ask
def setup_question(current_question_number):
    next_question = ()
    # #  100 level question
    if current_question_number <= 5 :
        next_question = questions_dict[1]
        key = 1
    # # 200 level question
    elif current_question_number <= 10:
        next_question = questions_dict[2]
        key = 2
    # # 300 level question
    else:
        next_question = questions_dict[3]
        key = 3
    consumed_questions.append(key)
    print("logger consumer question: ", consumed_questions)
    return next_question


def evalute_user_answer(answer):
    question_key = consumed_questions[-1]
    correct_answer = questions_dict[question_key][2]
    if (correct_answer == answer):
        return True
    else:
        return False
