import csv
import json

reader = csv.reader(open('fizykapytania2.csv', 'r'))

questions = []

for row in reader:
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

with open('src/assets/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False)
