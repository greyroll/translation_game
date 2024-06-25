import json


class QuestionTextLoader:
	def __init__(self, path):
		self.path = path

	def read(self):
		with open(self.path, "r") as file:
			return file.read()

	def get_questions(self):
		data = self.read()
		lines = data.split("\n")
		questions: list[Question] = []
		options = []
		for line in lines:
			split_line = line.split(": ")
			options.append(split_line[1])
		for line in lines:
			split_line = line.split(": ")
			questions.append(Question(question=split_line[0], answer=split_line[1], options=options))
		return questions


class QuestionJSONLoader(QuestionTextLoader):
	def __init__(self, path):
		super().__init__(path)

	def read(self):
		return json.loads(super().read())

	def get_questions(self):
		data = self.read()
		questions: list[Question] = []
		options = []
		for dictionary in data:
			options.append(dictionary["translation"])
		for dictionary in data:
			questions.append(Question(question=dictionary["word"], answer=dictionary["translation"], options=options))
		return questions


class Question:
	def __init__(self, question: str, answer: str, options: list[str]):
		self.question = question
		self.answer = answer
		self.options_list = options
		number_of_element = 1
		self.options = {}
		for option in self.options_list:
			self.options[number_of_element] = option
			number_of_element += 1
		self.__was_asked = False

	def __repr__(self):
		return f"Question(question={self.question}, answer={self.answer}, options={self.options_list})"

	def build_question(self):
		print(self.question)
		for key, value in self.options.items():
			print(f"{key}. {value}")
		self.__was_asked = True

	def get_answer(self):
		print("Введи номер правильного ответа:")
		user_answer = None
		try:
			user_answer = int(input())
		except ValueError:
			print("Это не цифра")
		return user_answer

	def check_answer_give_fb(self, user_answer):
		for number, option in self.options.items():
			if number == user_answer:
				if option == self.answer:
					print("Это верный ответ!")
				else:
					print(f"Неверно! Правильный ответ {self.answer}")

	def was_asked(self) -> bool:
		return self.__was_asked
