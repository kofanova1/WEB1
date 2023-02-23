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
        'answer': 'X'
    },
    {
        'question': '삼국시대의 전쟁에서는 기병이나 화살, 창과 칼 등을 사용하는 전투가 주로 발생했다.' ,
        'answer': 'O'
    },
    {'question': '삼국통일 후 고구려와 발해는 새로운 국가로 재건되었다.', 'answer': 'X'},
    {'question': '신라와 발해는 동북아시아 거대한 유교 국가였다.', 'answer': 'X'},
    {'question': '백제는 경상도와 전라도에 걸쳐 있었다.', 'answer': 'O'},
    {'question': '삼국시대 후반에 신라가 가진 문화적 영향력은 당나라에서도 인정받았다.', 'answer': 'O'},
    {'question': '신라 시대의 대표적인 유물인 황룡사 석조 대불은 대형 석조물 중에서도 특히 기술적인 완성도가 높다.', 'answer': 'O'},
    {'question': '신라 시대에는 비로소 불교가 대중적으로 수용되었으며, 특히 서라벌 대공보살이나 월불 등의 광법사 승려들이 불교를 널리 퍼뜨리는 데 기여하였다.', 'answer': 'O'},
    {'question': '고구려의 수도는 현재의 평양에 위치해 있었다.', 'answer': 'O'},
    {'question': '삼국시대에는 철제가 주요한 생산물 중 하나였으며, 고구려는 철강 생산으로 인해 번성하였다.', 'answer': 'O'}
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
        questions.remove(question)

        
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
