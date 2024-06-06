import requests, datetime
import time

last_api_call_made_on = 0

# returns next question to ask
def setup_question(current_question_number):
    global last_api_call_made_on

    #  code to stay within api call interval of every 5 seconds.
    if (current_question_number == 0):
        last_api_call_made_on = datetime.datetime.now()
    if( datetime.datetime.now() < last_api_call_made_on + datetime.timedelta(seconds=5)):
        time.sleep(3)

    # #  100 level question
    if current_question_number <= 5 :
        response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple', 'category':'18', 'difficulty':'easy'}).json()["results"][0]
        # print("-------------------------------------------------logger")
        # print("response: ", response)

    # # 200 level question
    elif current_question_number <= 10:
        response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple', 'category':'18', 'difficulty':'medium'}).json()["results"][0]
        # print("-------------------------------------------------logger")
        # print("response: ", response)

    # # 300 level question
    else:
        response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple', 'category':'18', 'difficulty':'hard'}).json()["results"][0]
        # print("-------------------------------------------------logger")
        # print("response: ", response)

    # return a tuple,
    # setup as:
    # (100, "in python, what is refered to as a Snake Case",
    #                         "correct answer",
    #                                       "wrong ans",
    #                                       "wrong ans",
    #                                       "wrong ans"),
    last_api_call_made_on = datetime.datetime.now()
    # print("-------------------------------------------------logger")
    # print("last api call set to: ", last_api_call_made_on)
    # print("last api call set to + 5: ", last_api_call_made_on + datetime.timedelta(seconds=5))

    next_question = (100, response['question'],
                    response['correct_answer'],
                                response['incorrect_answers'][0],
                                response['incorrect_answers'][1],
                                response['incorrect_answers'][2],)
    # print("-------------------------------------------------logger")
    # print("difficulty level: ", response['difficulty'])
    return next_question
