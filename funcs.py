import random

from classes import QuestionTextLoader, QuestionJSONLoader, Question, User

# TODO нарушается SRP, разделить на две функции: одна приветствовать пользователя, а вторая будет возвращать путь
def intro():
	"""
	Функция приветствует пользователя и предлагает выбрать тему игры.
	Функция возвращает путь к файлу со словами выбранной темы.
	:return:
	"""
	print("Добро пожаловать!")
	print("Выбери одну из предложенных тем:")
	# TODO название категорий полезно будет вынести в словарь CATEGORIRES = {
	#  1: {name: Путешествия, path="travel.txt"}m
	#  2: {name: Животные, path="animals.txt"},
	# }
	print(f"1) Путешествия \n2) Животные \n3) Ресторан \n4) Офис")
	print("Введи номер темы")
	# TODO попробовать использовать while

	try:
		topic_number = int(input())
	except ValueError:
		print("Это не цифра. Попробуй еще раз")
		exit()
	# TODO за счет использования словаря избавиться от мультиусловий
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

# TODO переназвать load_questions
def txt_or_json(path: str) -> QuestionTextLoader | QuestionJSONLoader:
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


# TODO если хочешь  перенести в main или в класс типа GameUI
def run_all_rounds(questions: list[Question]):
	"""
	Задает все вопросы
	:param questions:
	:return:
	"""
	user = User()
	counter = 0
	while counter < len(questions):
		question = random.choice(questions)
		if question.was_asked():
			continue
		question.build_question()
		if question.check_answer_give_fb(question.get_answer()):
			user.points += 10
		counter += 1
	print(f"Вы набрали {user.points} очков.")
