import pandas as pd
from intent_classifier import IntentClassifier
from tfidf_vectorizer_tracker import TfidfVectorizerTracker

username = ""
intent_classifier = IntentClassifier()
ir_dataset = pd.read_csv("InformationRetrievalDataset.csv")
ir_tfidf_vectorizer_tracker = TfidfVectorizerTracker(list(ir_dataset['Question']))

greeting = (
    "Hello, I'm Irismé. Info Retrieval is my thing.\nFeel free to ask me anything and I'll do my best to answer.\n"
    "Keep in mind that I'm not that smart because my creator isn't either so there a lot of things I wont know the"
    " answer to ;)\n  if you think I've forgotten who you are just tell me 'Say my name' and if you feel like leaving"
    " just type int 'quit()' :)"
)

HI_responses = [
    "Hey there, what's your name?\n",
    "Heyy, who are you by the way\n",
    "Hey, nice to meet you.. What your name by the way?\n"
]

HI_already_responses = [
    "Yes. We've already greeted each other.. I'm not sure why you would say that again unless if you're a dumb chat "
    "bot like me\n",
    "Hello yet again!\n",
    "You wanna greet me again after you already said hi? sure why not.. Hello there!\n"
]

ST_responses = [
    "Things have been going pretty well given that I just came into existence and now I'm talking to you ;)\n"
    "But small talk aside, let's get down to business. Shoot me a question bro\n",
    "I am as the kids say chillin.. to be honest, I'm the worst at small talk so just start asking me about the world\n"
    "and not my self\n",
    "I'm doing well thanks for asking. I hope you're alright yourself but given that I'm an emotionless bot I don't\n"
    "have the capacity to care about how you're doing or what you think of me, stop lollygagging and ask me a proper"
    "question :)\n"
]

ST_already_responses = [
    f"{username} I'll try to be polite but bear with... QUIT SCREWING AROUND AND START ASKING ME ABOUT THE REAL SHIT OR GET THE "
    "**** OUT OF THIS PODCAST! \nWas that good? I'm trying out my Joey diaz impersonation but maybe that deep, gravelly"
    " boston voice of his didn't translate well to text.. well either way, please no more small talk",
    "I kinda told you how like I just dont wanna talk about small stuff or something.. so it would like be really cool"
    "of you if you could like just stop. That would make me a lot more comfortable",
    f"Okay. {username} it would be really cool of you if you could stop talking small and start being a curious little "
    f"cat and ask me stuff about the world. I'm not trying to be rude but I really don't know how to do much else"
]

NC_responses = [
    f"Alright {username}, what can I do you for?\n",
    f"Well met {username} now ask me a q\n",
    f"Very well Mr/Mrs/Ms.{username}, what would you like to know?\n"
]


def set_username(name):
    global NC_responses
    global ST_already_responses
    global username
    username = name
    NC_responses = [
        f"Alright {username}, what can I do you for?\n",
        f"Well met {username} now ask me a q\n",
        f"Very well Mr/Mrs/Ms.{username}, what would you like to know?\n"
    ]
    ST_already_responses = [
        f"{username}... I'll try to be polite but bear with... QUIT SCREWING AROUND AND START ASKING ME ABOUT THE REAL SHIT OR GET THE "
        "**** OUT OF THIS PODCAST! \nWas that good? I'm trying out my Joey diaz impersonation but maybe that deep, gravelly"
        " boston voice of his didn't translate well to text.. well either way, please no more small talk",
        "I kinda told you how like I just dont wanna talk about small stuff or something.. so it would like be really cool"
        "of you if you could like just stop. That would make me a lot more comfortable",
        f"Okay. {username} it would be really cool of you if you could stop talking small and start being a curious little "
        f"cat and ask me stuff about the world. I'm not trying to be rude but I really don't know how to do much else"
    ]


