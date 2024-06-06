import requests, json, random, re
while True:
    response = requests.get(url="https://opentdb.com/api.php", params={'amount': 1, 'type':'multiple'}).json()["results"][0]
    print("Correct\n" if input(re.sub(r'\&.*?\;', '', response['question'])+'\n'+('\n').join(map(lambda x: re.sub(r'\&.*?\;', '', str(x)), sorted(response['incorrect_answers'] + [response['correct_answer']], key=lambda k: random.random())))+'\n'+'\n').lower() == response['correct_answer'].lower() else f"Incorrect! The Correct Answer was: {response['correct_answer']}\n")
