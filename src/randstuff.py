import requests

class RandStuff:
	def __init__(self):
		self.api = "https://randstuff.ru"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
			"x-requested-with": "XMLHttpRequest"
		}

	def generate_random_joke(self):
		return requests.post(
			f"{self.api}/joke/generate/",
			headers=self.headers).json()

	def generate_random_number(
			self,
			count: int = 1,
			start: int = 1,
			end: int = 100,
			list: str = None,
			unique: int = 0,
			tz: int = -480):
		data = {
			"count": count,
			"from": "range",
			"start": start,
			"end": end,
			"list": list,
			"unique": unique,
			"tz": tz
		}
		return requests.post(
			f"{self.api}/number/generate/",
			data=data,
			headers=self.headers).json()

	def generate_random_wisdom(self):
		return requests.post(
			f"{self.api}/saying/generate/",
			headers=self.headers).json()

	def generate_random_fact(self):
		return requests.post(
			f"{self.api}/fact/generate/",
			headers=self.headers).json()

	def generate_random_ticket(self):
		return requests.post(
			f"{self.api}/ticket/generate/",
			headers=self.headers).json()

	def get_random_ask(self, question: str):
		data = {
			"question": question
		}
		return requests.post(
			f"{self.api}/ask/generate/",
			data=data,
			headers=self.headers).json()

	def generate_random_password(
			self,
			length: int = 8,
			numbers: int = 0,
			symbols: int = 0):
		data = {
			"length": length,
			"numbers": numbers,
			"symbols": symbols
		}
		return requests.post(
			f"{self.api}/password/generate/", 
			data=data,
			headers=self.headers).json()

	def generate_random_question(self):
		return requests.post(
			f"{self.api}/question/generate/",
			headers=self.headers).json()

	def answer_to_question(
			self,
			id: int,
			number: int):
		data = {
			"id": id,
			"number": number
		}
		return requests.post(
			f"{self.api}/question/answer/",
			data=data,
			headers=self.headers).json()

	def generate_random_nickname(self, numbers: int = 1):
		data = {
			"numbers": numbers
		}
		return requests.post(
			f"{self.api}/nickname/generate/",
			data=data,
			headers=self.headers).json()

	def generate_random_city(self, country: str = "all"):
		data = {
			"country": country
		}
		return requests.post(
			f"{self.api}/city/generate/",
			data=data,
			headers=self.headers).json()
			
