from millionaire_game_pkg.game_board import set_home_page
from millionaire_game_pkg.question_processor import setup_question

current_question = 0

while (True):
    answerd_correctly = set_home_page(current_question, setup_question(current_question) )
    # print("-------------------------------------------------logger")
    # print("did the user ansewr correctly ?:", answerd_correctly )

    if (answerd_correctly):
        current_question += 1
    else:
        print("\n\n\nAnswer Not Correct ....GoodBye !!")
        break
