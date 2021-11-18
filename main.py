import random
import settings
from answer_finding import retrieve_answer



def heisenberg():
    print("You're Heisenberg...")
    youre_god_damn_right = input()

    if youre_god_damn_right == "You're god damn right":
        print('HAHAHA YESS! Nice one')
    else:
        print("I don't want to be your friend anymore :(")

    if settings.username == "":
        print("In case you can't tell I looooove breaking bad. Anyway you haven't actually told me your name so idk")
    else:
        print(f"anyway, your name is {settings.username}")


intent_classifier = settings.intent_classifier

greeted = False
chit_chatted = False

print(settings.greeting)


while True:
    response = ""
    bad_match = False
    message = input("*Irismé is listening*\t")

    if message == 'quit()':
        print('Bye then!')
        break

    if message == 'Say my name':
        heisenberg()
        continue

    predicted_intent = intent_classifier.predict_intent(message)
    print(predicted_intent)

    if predicted_intent == 'HI':

        if greeted:
            response = random.choice(settings.HI_already_responses)
        else:
            response = random.choice(settings.HI_responses)
        greeted = True

    elif predicted_intent == 'ST':

        if chit_chatted:
            response = random.choice(settings.ST_already_responses)
        else:
            response = random.choice(settings.ST_responses)
        chit_chatted = True

    elif predicted_intent == 'NC':

        settings.set_username(message.split(" ")[-1])
        response = random.choice(settings.NC_responses)

    else:
        response, bad_match = retrieve_answer(message)

    if bad_match:
        print("I don't 'think' this is the right answer but its the closet thing I could find to your question :/\n")

    print("".join(response) + '\n')
