import csv
import json

reader = csv.reader(open('fizykapytania3.csv', 'r', encoding='utf-8'))

reader2 = csv.reader(open('fizykapytania2.csv', 'r', encoding='utf-8'))

questions = []

for row in reader2:
    print(row)
    questions.append({
        'question': row[0],
        'answer_a': row[1],
        'answer_b': row[2],
        'answer_c': row[3],
        'answer_d': row[4],
        'answer_a_correct': True,
        'answer_b_correct': False,
        'answer_c_correct': False,
        'answer_d_correct': False,
    })

for row in reader:
    print(row)
    questions.append({
        'question': row[0],
        'answer_a': row[1],
        'answer_b': row[2],
        'answer_c': row[3],
        'answer_d': row[4],
        'answer_a_correct': row[5]=='TRUE',
        'answer_b_correct': row[6]=='TRUE',
        'answer_c_correct': row[7]=='TRUE',
        'answer_d_correct': row[8]=='TRUE',
    })

with open('src/assets/questions4.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False)
