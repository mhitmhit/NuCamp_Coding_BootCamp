# for i in range(0,5,1):
#     print(i)

# for x in "string":
#     print(x,x,x,x)

# for i in range(1,5):
#     print(i)

# def testFunction(num):
#     if num == 1:
#         return "success"

# print(testFunction(1)+testFunction(2))

# reverse = lambda text: "".join(f"{(text[-i-1])}" for i in range(len(text)))


# name = input("What is your name? ")
# print("Your name reversed is:", reverse(name))

# name = "yassine"
# for pat in range(1,5):
#     print(pat)


# my_string = "giraffe"

# print(my_string[-0])
# print(my_string[0])
# print(my_string[0:90])
# arr = []
# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

# print(arr)

# state_capitals ={"washington":"olympia",
#                  "oregon":"salem",
#                  "california":"sacramento"}

import requests, json, random, re
test = True
while True:
    # response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple'}).json()["results"][0]
    response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple'}).json()['results'][0]
    print("response: \n" ,response)
    # print("Correct\n" if input(re.sub(r'\&.*?\;', '', response['question'])+'\n'+('\n').join(map(lambda x: re.sub(r'\&.*?\;', '', str(x)), sorted(response['incorrect_answers'] + [response['correct_answer']], key=lambda k: random.random())))+'\n'+'\n').lower() == response['correct_answer'].lower() else f"Incorrect! The Correct Answer was: {response['correct_answer']}\n")
