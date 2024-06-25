# def beautiful_input() -> str:
# 	user_input = input(" ")
# 	user_input = user_input.strip()
# 	user_input = user_input.lower()
# 	return user_input
import random

from classes import QuestionTextLoader, QuestionJSONLoader, Question


def intro():
	"""
	Функция приветствует пользователя и предлагает выбрать тему игры.
	Функция возвращает путь к файлу со словами выбранной темы.
	:return:
	"""
	print("Добро пожаловать!")
	print("Выбери одну из предложенных тем:")
	print(f"1) Путешествия \n2) Животные \n3) Ресторан \n4) Офис")
	print("Введи номер темы")
	try:
		topic_number = int(input())
	except ValueError:
		print("Это не цифра. Попробуй еще раз")
		exit()
	if topic_number == 1:
		path = "travel.txt"
	elif topic_number == 2:
		path = "animals.txt"
	elif topic_number == 3:
		path = "restaurants.json"
	elif topic_number == 4:
		path = "office.json"
	else:
		raise ValueError("Введи номер темы. 1, 2, 3 или 4.")
	return path


def txt_or_json(path) -> QuestionTextLoader | QuestionJSONLoader:
	"""
	Определяет тип файла, находящегося по данному пути.
	Возвращаает экземпляр класса QuestionTextLoader или QuestionJSONLoader
	:param path:
	:return:
	"""
	if path.endswith(".txt"):
		return QuestionTextLoader(path)
	if path.endswith(".json"):
		return QuestionJSONLoader(path)


def run_round(questions: list[Question]):
	counter = 0
	while counter < len(questions):
		question = random.choice(questions)
		if question.was_asked():
			continue
		question.build_question()
		# user_answer =
		question.check_answer_give_fb(question.get_answer())
		counter += 1
