"""
 @project: main.py
 @description: 
 @author: Harrison-1eo
 @date: 2023-09-08
 @version: 1.0
"""


from storage import create_excel, read_excel, write_excel
from extract import get_answer


create_excel()
ans_dict = read_excel()


with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()

answers = get_answer(text, 'des')
write_excel(ans_dict, answers)
answers = get_answer(text, 'des_2')
write_excel(ans_dict, answers)
    