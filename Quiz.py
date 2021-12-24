# ---------------
def new_game():
    score = 0
    index = 0
    for question, answer in questions.items():
        print('--------------------------------')
        print(question)
        for option in choices[index]:
            print(option)
        student_answer = str(input('Enter (A, B, C, D): ')).upper()
        score += check_answer(answer, student_answer)
        index += 1
    display_score(score)

# ---------------

def check_answer(answer, choice):
    return 1 if answer == choice else 0


# ---------------
def play_again():
    continue_game = str(input('Re-take the quiz (yes/no)?: ')).lower()
    if continue_game == 'yes':
        return True
    else:
        return False


# ---------------
def display_score(score):
    print('--------------------------------')
    print('----------Results Time----------')
    print('--------------------------------')
    print("You Scored " + str(score) + " out of " + str(len(questions)))


# ---------------

questions = {
    "whats the quiz proctor's name": 'A',
    "where are you doing the exam": 'B',
    "what year are you taking the exam": 'C',
    "How is the exam": 'D'
}

choices = [
    ['A. Pradeep', 'B. Vinay', 'C. Udayani', 'D. Aadhya'],
    ['A. Office', 'B. Home', 'C. Ground', 'D. School'],
    ['A. 2020', 'B. 2022', 'C. 2021', 'D. 2023'],
    ['A. Could be better', 'B. Worst', 'C. Ok :)', 'D. The Best']
]
first_time = True
while first_time or play_again():
    first_time = False
    new_game()

print("Good luck!!")
