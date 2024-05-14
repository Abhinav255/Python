import json

questions = [
    {'question': 'who is the prime minister of India',
     'option1': "1 Narendra Modi",
     'option2': "2 Rahul Gandhi",
     'Answer': "1"
     },
    {'question': 'Which state is Ahmedabad located in',
     'option1': "1 Gujarat",
     'option2': "2 Maharashtra",
     'Answer': "1"
     },
    {'question': 'When did India get its independence',
     'option1': "1 1947",
     'option2': "2 1960",
     'Answer': "1"
     },
]


def play():
    print("\n==========QUIZ START==========")
    score = 0
    for question in questions:
        question_text = question.get("question")
        print(question_text)
        option1 = question.get("option1")
        print(option1)
        option2 = question.get("option2")
        print(option2)

        user_answer = input("Enter your answer: ")
        real_answer = question.get("Answer")
        if user_answer == real_answer:
            print("\nYou are correct")
            score += 1
        else:
            print("\nYou are incorrect")
    print(f'\nFINAL SCORE: {score}')


def addquizQuestions():
    print('\n==========ADD QUESTIONS==========\n')
    ques = input("Enter the question that you want to add: ")
    opt1 = input("Enter option 1: ")
    opt2 = input("Enter option 2: ")
    ans = input("Enter the answer (1 or 2): ")
    
    new_question = {
        'question': ques,
        'option1': "1 " + opt1,
        'option2': "2 " + opt2,
        'Answer': ans
    }
    
    questions.append(new_question)
    
    print("Question successfully added.")


def rules():
    print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press 1 or 2.
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
    ''')


def about():
    print('')


if __name__ == "__main__":
    choice = 1
    while choice != 3:
        print('\n=========WELCOME TO QUIZ MASTER==========')
        print('-----------------------------------------')
        print('1.  QUIZ CRACKER')
        print('2.  QUIZ MASTER')
        print('3. EXIT')

        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            play()
        elif choice == 2:
            addquizQuestions()
        elif choice == 3:
            break
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')
