import random
import argparse

questions = [
    {
        'question': '삼국시대가 발생한 시기는 1세기에서 7세기 사이이다.', 
        'answer': 'O'
    },
    {
        'question': '삼국시대를 이룬 나라는 고구려, 백제, 신라, 가야, 당나라, 위만성, 마무리, 우분성 등이 있다.', 
        'answer': 'X'
    },
    {
        'question': '삼국시대의 처음에는 서로 군사적으로 경쟁하지 않았다.',
        'answer': 'X'
    },
    {
        'question': '삼국시대의 끝에서는 이인영이 집권하여 권력을 누리고 있었다.',
        'answer': 'O'
    },
    {
        'question': '삼국시대의 전쟁에서는 기병이나 화살, 창과 칼 등을 사용하는 전투가 주로 발생했다.' ,
        'answer': 'O'
    }
    # Add more questions here
]

def print_question(question):
    print(question['question'])

def check_answer(question, answer):
    return answer == question['answer']

def get_random_question(questions):
    return random.choice(questions)

def create_cli_interface():
    parser = argparse.ArgumentParser(description='삼국시대 OX 퀴즈 게임')
    parser.add_argument('--num_questions', type=int, default=5, help='출제할 문제 수')
    return parser

def start_game(num_questions):
    score = 0
    
    for i in range(num_questions):
        question = get_random_question(questions)
        print_question(question)
        user_answer = input('O 또는 X를 입력하세요: ')
        
        if check_answer(question, user_answer):
            print('정답입니다!')
            score += 1
        else:
            print('오답입니다.')
        
        print('==================')
    
    print(f'최종 점수: {score}/{num_questions}')

def main():
    parser = create_cli_interface()
    args = parser.parse_args()
    start_game(args.num_questions)

if __name__ == '__main__':
    main()

import os

if os.name == "nt":
    os.system("pause")
