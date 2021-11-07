import requests
import json


class Client:
    def __init__(self):
        self.api = "https://randstuff.ru"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"}

    def generate_random_joke(self):
        request = requests.post(
            f"{self.api}/joke/generate/",
            headers=self.headers)
        return request.json()

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
            "tz": tz}
        request = requests.post(
            f"{self.api}/number/generate/",
            json=data,
            headers=self.headers)
        return request.json()

    def generate_random_wisdom(self):
        request = requests.post(
            f"{self.api}/saying/generate/",
            headers=self.headers)
        return request.json()

    def generate_random_fact(self):
        request = requests.post(
            f"{self.api}/fact/generate/",
            headers=self.headers)
        return request.json()

    def generate_random_ticket(self):
        request = requests.post(
            f"{self.api}/ticket/generate/",
            headers=self.headers)
        return request.json()

    def get_random_ask(self, question: str):
        data = {"question": question}
        request = requests.post(
            f"{self.api}/ask/generate/",
            headers=self.headers)
        return request.json()

    def generate_random_password(
            self,
            length: int = 8,
            numbers: int = 0,
            symbols: int = 0):
        data = {"length": length, "numbers": numbers, "symbols": symbols}
        request = requests.post(
            f"{self.api}/password/generate/", 
			json=data
            headers=self.headers)
        return request.json()

    def generate_random_question(self):
        request = requests.post(
            f"{self.api}/question/generate/",
            headers=self.headers)
        return request.json()

    def answer_to_question(self, id: int, number: int):
        data = {"id": id, "number": number}
        request = requests.post(
            f"{self.api}/question/answer/",
            json=data,
            headers=self.headers)
        return request.json()

    def generate_random_nickname(self, numbers: int = 1):
        data = {"numbers": numbers}
        request = requests.post(
            f"{self.api}/nickname/generate/",
            json=data,
            headers=self.headers)
        return request.json()

    def generate_random_city(self, country: str = "all"):
        data = {"country": country}
        request = requests.post(
            f"{self.api}/city/generate/",
            json=data,
            headers=self.headers)
        return request.json()
