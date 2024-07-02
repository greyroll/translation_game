from funcs import intro, txt_or_json, run_round

path = intro()
#  TODO перенести инпуты сюда вот, чтобы все взаимодействие с пользователем было на верхнем уровне
question_loader = txt_or_json(path)
questions = question_loader.get_questions()
run_round(questions)
