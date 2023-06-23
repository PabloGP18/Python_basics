# importing Question class
from Question import Question

question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue \n\n"
]

# creating a questions array with the Question class that will result in an array of Question objects
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0

    #Looping true questions array of objects and accessing the prompt/answer attribute of the object
    for question in questions:
        answer = input(question.prompt)

        if answer == question.answer:
            score +=1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)