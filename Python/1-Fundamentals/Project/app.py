from millionaire_game_pkg.game_board import set_home_page
from millionaire_game_pkg.question_processor import setup_question, evalute_user_answer

current_question = 1

while (True):
    answer = set_home_page(current_question, setup_question(current_question) )
    if (evalute_user_answer(answer)):
        current_question += 1
    else:
        print("Answer Not Correct ....")
        break
