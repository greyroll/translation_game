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
			questions.append(Question(question=split_line[0], answer=split_line[1]))
		return questions


class QuestionJSONLoader(QuestionTextLoader):
	def __init__(self, path):
		super().__init__(path)

	def read(self):
		return json.loads(super().read())


class Question:
	def __init__(self, question: str, answer: str):
		self.question = question
		self.answer = answer
		self.options = []

	def __repr__(self):
		return f"Question(question={self.question}, answer={self.answer}, options={self.options})"

	def build_question_(self):
		print(self.question)
		number_of_element = 1
		for option in self.options:
			print(f"{number_of_element}) {option}")
			number_of_element += 1
