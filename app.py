#Implementação machine chatbot in python
import random
# from speech import *
from pip._vendor.distlib.compat import raw_input

CONVERSING = True

memory = []
greetings = ['ola', 'olar', 'inicio', 'start']
questions = ['Como você está?', 'Esta bem?', 'Está tudo bem?']
responses = ['Ok!', 'Estou bem']
validations = ['Sim', 'Com certeza', 'não']
items = ['Frutas', 'Chocolates']
verifications = ['Você ta bem?']

par = (greetings, greetings), (questions, responses), (verifications, validations)

while CONVERSING:
    lang = 'en-US'
    speed = .3

    userInput = raw_input(">>>Eu: ")
    for triggers, outputs in par:
        if not userInput in triggers:
            continue

        random_output = random.choice(outputs)

        print(random_output)
        memory.append((userInput, random_output))
        break

    else:
        if 'bem' in userInput:
            response = "Você tem certeza?"
            memory.append(('bem', response))
            print(response)
        else:
            CONVERSING = False
