import re
from localconfig import paths
import xlsxwriter

from utils.file_management import create_excel_copy

# with open("test.txt", "r") as file:
#     text = file.read()
#     text = text.replace("\\n", "\n")


def get_q_and_a(text: str) -> dict:
    question_answer_pairs = dict()
    pattern_question = re.compile(r"F:([\S\s]*?)\n")
    pattern_answer = re.compile(r"A:([\S\s]*?)\n")

    question_match = pattern_question.findall(text)
    answer_match = pattern_answer.findall(text)

    print(len(question_match))
    print(len(answer_match))

    for index in range(len(question_match)):
        # print(index, question_match[index])
        # print(index, answer_match[index])
        question_answer_pairs[question_match[index]] = answer_match[index]
    
    return question_answer_pairs

def write_excel(q_and_a_pairs: dict):
    template_copy = create_excel_copy(paths["xlsx_template"], paths["output_folder"])
    wb = xlsxwriter.Workbook(template_copy)
    ws = wb.add_worksheet("Sheet1")

    # add data to the worksheet
    ws.write('A1', 'Frage')
    ws.write('B1', 'Antwort A')
    ws.write('C1', 'Antwort ist korrekt (TRUE falls ja, FALSE falls nein)')
    ws.write('N1', 'Tags')
    ws.write('O1', 'Tipps')
    ws.write('P1', 'Erklärung')

    # Write questions and answers
    row = 2  # Start from row 2 to skip headers
    for question, answer in q_and_a_pairs.items():
        ws.write(f'A{row}', question)
        ws.write(f'B{row}', answer)
        ws.write(f'C{row}', "WAHR")
        row += 1

    # save the workbook
    wb.close()

def generate_output(gpt_response: list):
    for document in gpt_response:
        q_and_a_pairs = get_q_and_a(document)
        write_excel(q_and_a_pairs)
