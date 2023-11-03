import os
import random

JokesArrayFull = []

class Dadjokes:
    def __init__(self, prompt, answer):
        self.__prompt = prompt
        self.__answer = answer

    def joker(self):
        print(self.__prompt)
        users = input("")
        if str(users) == str(self.__prompt):
            print("Correct! You Win")
        return self.__answer

    def jokes(self):
        message = self.__prompt + " " + self.__answer
        return message

def Constructor():
    try:
        with open("DadJokes.txt", "r") as file:
            for i in range(10):
                start = file.readline().strip()
                finish = file.readline().strip()
                JokesArrayFull.append(Dadjokes(start, finish))

    except:
        print("File found at ", os.getcwd())

Constructor()

def PrintRandomJoke():
    j = random.randint(0,9)
    print(JokesArrayFull[j].joker())

PrintRandomJoke()
