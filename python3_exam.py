import random
from python_mock_exam import python_mock_exam

def print_question(num):
    dict_question = python_mock_exam[num]
    print(dict_question["question"])
    print(dict_question["code"])
    dict_var = {}
    pre_list = list(range(0,4))
    list_op = random.sample(pre_list,4)
    c = 1
    for i in list_op:
        print(f"{c}:{dict_question["choices"][i]}")
        dict_var[c] = dict_question["choices"][i]
        c += 1
    user_answer = input_user_answer()
    use_ans = dict_var[user_answer]
    return use_ans
   
def check_answer(num,ans):
    print(f"あなたの回答:{ans}")
    dict_question = python_mock_exam[num]
    answer_num = dict_question["answer"] - 1
    if dict_question["choices"][answer_num] == ans:
        print("正解")
        return 1
    else:
        print("不正解")
        return 0

def input_user_answer():
    input_answer = input("回答を入力してください 例）1 :")
    while input_answer not in range(1,5):
        try:
            if int(input_answer) in range(1,5):
                break
            elif input_answer not in range(1,5):
                input_answer = input("1~4で入力してください 例）1 :")
                continue
        except:
            input_answer = input("数字で入力してください 例）1 :")
    return int(input_answer)


def run_console_quiz():
    pre_list = list(range(1, len(python_mock_exam) + 1))
    list_num = random.sample(pre_list, len(python_mock_exam))
    win = 0
    c = 1
    for i in list_num:
        print(f"第{c}問:")
        users = print_question(int(i))
        quiz_list = python_mock_exam[int(i)]
        answer_num = quiz_list["answer"] - 1
        answer_word = quiz_list["choices"][answer_num]
        print(f"正解は...「{answer_word}」")
        result = check_answer(int(i), users)
        if result > 0:
            win += 1
        c += 1
    print(f"あなたの正解数は{win}/{len(python_mock_exam)}問！")


if __name__ == "__main__":
    run_console_quiz()
