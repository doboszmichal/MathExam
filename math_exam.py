# user_input = input()
# result = eval(user_input)
# print(result)
import math
import random


def select_level():
    print('Select difficulty level:')
    print('1 - Simple operations with number 2 - 9')
    print('2 - Integral squares 11 - 29')
    select_level.num = input()
    if select_level.num == '1':
        create_task(choose_a(), choose_b(), choose_operation())
    elif select_level.num == '2':
        level2(generate_number())
    else:
        select_level()


def choose_a():  # Select first integer
    choose_a.num = int(random.randrange(2, 10))
    return choose_a.num


def choose_b():  # Select second integer
    choose_b.num = int(random.randrange(2, 10))
    return choose_b.num


def choose_operation():  # Select operation
    choose_operation.char = random.choice(['+', '-', '*'])
    return choose_operation.char


def generate_number():  # Select number
    generate_number.num = int(random.randrange(11, 30))
    return generate_number.num


def ask_user():  # Function to take an answer from user
    ask_user.user_input = input()
    if not ask_user.user_input.lstrip('-+').isdigit():
        print('Incorrect format.')
        ask_user()
    return ask_user.user_input


def global_vars():  # Function which defines global variables
    global_vars.count = 1
    global_vars.total_mark = 0


def check_if_run():
    if global_vars.count < 6:
        create_task(choose_a(), choose_b(), choose_operation())
        ask_user()
    else:
        print('Your mark is', global_vars.total_mark, '/5.')
        save_result()
        exit()


def check_if_run2():
    if global_vars.count < 6:
        level2(generate_number())
        ask_user()
    else:
        print('Your mark is', global_vars.total_mark, '/5.')
        save_result()
        exit()


def create_task(num1, num2, char):  # Function which create tasks for user
    if char == '+':
        result = num1 + num2
        print(num1, '+', num2)
        if result == int(ask_user()):
            global_vars.total_mark += 1
            print('Right!')
        else:
            print('Wrong!')
        global_vars.count += 1
        check_if_run()
    elif char == '-':
        result = num1 - num2
        print(num1, '-', num2)
        if result == int(ask_user()):
            global_vars.total_mark += 1
            print('Right!')
        else:
            print('Wrong!')
        global_vars.count += 1
        check_if_run()
    else:
        result = num1 * num2
        print(num1, '*', num2)
        if result == int(ask_user()):
            global_vars.total_mark += 1
            print('Right!')
        else:
            print('Wrong!')
        global_vars.count += 1
        check_if_run()


def level2(num1):
    result = num1 * num1
    print(num1)
    if result == int(ask_user()):
        global_vars.total_mark += 1
        print('Right!')
    else:
        print('Wrong!')
    global_vars.count += 1
    check_if_run2()


def save_result():
    print('Would you like to save your result to the file? Enter yes or no.')
    user_input = input()
    if user_input in ('yes', 'YES', 'y', 'Yes'):
        if select_level.num == '1':
            user_name = input('Enter your name:')
            result = open('results.txt', 'a', encoding='utf-8')
            str_result = user_name + ': ' + str(global_vars.total_mark) + '/5 in level 1 (simple operations with numbers 2-9).'
            result.write(str_result)
            print('The results are saved in "results.txt".')
            result.close()
        else:
            user_name = input('Enter your name:')
            result = open('results.txt', 'a', encoding='utf-8')
            str_result = user_name + ': ' + str(global_vars.total_mark) + '/5 in level 2  (simple operations with numbers 11-29).'
            result.write(str_result)
            print('The results are saved in "results.txt".')
            result.close()
    elif user_input in ('no', 'NO', 'n', 'No'):
        exit()


global_vars()
select_level()
