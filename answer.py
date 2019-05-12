from utils import save_answer,load_answer

def return_answer(class_name):
    answers = load_answer()
    try:
        return answers[class_name]
    except:
        return 'Não entendi :('

