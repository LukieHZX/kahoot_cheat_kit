import requests
import json


try:
    with open('login.kahoot', 'r') as f:
        f_ = f.read().splitlines()
        email = f_[0]
        pswd = f_[1]
except FileNotFoundError:
    print('Create file: login.kahoot and type in first line you email and in the second line your password (of your kahoot-account)')
    exit(-1)


def get_answers(quizid, email, pswd):
    resp = requests.post('https://create.kahoot.it/rest/authenticate', data=json.dumps({'username':email,'password':pswd,'grant_type':'password'}).encode(),headers={'content-type':'application/json'}).json()

    if 'error' in resp:
        print('Email or Password is wrong!')
        exit(-1)

    resp = requests.get(f'https://create.kahoot.it/rest/kahoots/{quizid}', headers={'content-type' : 'application/json','authorization' : resp['access_token']}).json()

    qs = []

    if 'error' in resp:
        print("Quiz not found!")
        exit(-1)
    else:
        print(f'[+] Title: "{resp.get("title")}"')
        for i in range(0, len(resp["questions"])):
            q = {"question": "", "answer": ""}
            q["question"] = resp["questions"][i]["question"]
            for j in range(0, len(resp["questions"][i]["choices"])):
                if resp["questions"][i]["choices"][j]["correct"]:
                    q["answer"] = resp["questions"][i]["choices"][j]["answer"]
            qs.append(q)
        return qs

id_ = input("Enter the Quiz-ID from host URL: ")
q_and_a = get_answers(id_, email, pswd)

print('\n'*5)
print('-'*30 + ' Questions and Answers ' + '-'*30)
for i in q_and_a:
    print(f'Question: {i.get("question")}\nAnswer: {i.get("answer")}\n\n\n\n')
