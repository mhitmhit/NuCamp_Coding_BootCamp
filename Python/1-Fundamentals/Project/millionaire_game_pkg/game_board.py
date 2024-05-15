import random

# draw main game board
def set_home_page(current_question_number, next_question):
     answers_list = [next_question[2],next_question[3],next_question[4],next_question[5]]
     random.shuffle(answers_list)
     current_question_list = set_current_question_list(current_question_number)
     print("============= Who Wants to be a Millionaire ================")
     print("                                    15      $ 1,000,000",current_question_list[15])
     print("                                    14      $ 500,000",current_question_list[14])
     print("                                    13      $ 250,000",current_question_list[13])
     print("                                    12      $ 125,000",current_question_list[12])
     print("                                    11      $ 64,000",current_question_list[11])
     print("                                    10      $ 32,000",current_question_list[10])
     print("                                    9       $ 16,000",current_question_list[9])
     print("                                    8       $ 8,000",current_question_list[8])
     print("                                    7       $ 4,000",current_question_list[7])
     print("                                    6       $ 2,000",current_question_list[6])
     print("                                    5       $ 1,000",current_question_list[5])
     print("                                    4       $ 500",current_question_list[4])
     print("                                    3       $ 300",current_question_list[3])
     print("                                    2       $ 200",current_question_list[2])
     print("                                    1       $ 100",current_question_list[1])
     print("")
     print("question:",next_question[1])
     print("")
     print("     A: ", answers_list[0])
     print("                             B: ", answers_list[1])
     print("     C: ", answers_list[2])
     print("                             D: ", answers_list[3])
     while(True):
          user_answer = input("\nEnter you Answer:  ")
          if (user_answer in ["a","b","c","d"]):
               if (user_answer == "a"):
                    user_answer = answers_list[0]
               elif (user_answer == "b"):
                    user_answer = answers_list[1]
               elif (user_answer == "c"):
                    user_answer = answers_list[2]
               elif (user_answer == "d"):
                    user_answer = answers_list[3]
               break
     return user_answer

# draw arrow on the current question in leader board
def set_current_question_list(question_number):
     current_question = [
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          "",
          ""             ]
     current_question[question_number] = " <---<--<-<"
     return current_question
