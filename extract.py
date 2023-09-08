"""
 @project: extract.py
 @description: 定义提取答案函数
 @author: Harrison-1eo
 @date: 2023-09-08
 @version: 1.0
"""

from bs4 import BeautifulSoup


def get_answer(text: str, answer_type: str):
    '''
    param text: 网页源码
    param answer_type: 题目类型，des为选择题，des_2为判断题
    '''
    
    res = []
    
    if answer_type == 'des':
        m = {"A": 0, "B": 1, "C": 2, "D": 3}
    elif answer_type == 'des_2':
        m = {"T": "正确", "F": "错误"}
    else:
        print("answer_type参数错误")
        return res
    
    soup = BeautifulSoup(text, 'html.parser')
    # 查找所有包含题目和答案的<div>标签
    question_divs = soup.find_all('div', class_=answer_type)
    
    # 遍历所有<div>标签，提取题目和答案
    for div in question_divs:
        # 提取题目
        question = div.find('p').text.strip()
        # 去除题目中的题号
        question = question[question.find('.') + 1:].strip()

        # 提取答案
        answer_id = div.find('input', type='text').get('value').strip()
        # answer = div.find('li', string=lambda s: s and s.strip().endswith(f". {answer_id}")).text.strip()
        
        answers = div.find_all('li')
        answer = ''
        
        for option in answer_id:
            answer += answers[m[option]].text.strip() if answer_type == 'des' else m[option]
            answer += '  '
        
        # 打印题目和答案
        print(f"题目: {question}")
        print(f"答案: {answer}")
        
        res.append((question, answer))
    return res

        
if __name__ == '__main__':
    # 读取网页源码，打开txt测试文件
    with open('test.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        
    # 提取选择题答案
    get_answer(text, 'des')
    
    # 提取判断题答案
    get_answer(text, 'des_2')