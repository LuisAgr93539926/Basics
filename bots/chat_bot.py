from difflib import get_close_matches
import json
import random


def get_knowledge(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)

    intents = data["intents"]
    return intents


def extract_patterns_and_responses(knowledge):
    patterns_dict = {}
    for intent in knowledge:  # intent is a dictionary
        for pattern in intent["patterns"]:  # patterns is a list
            patterns_dict[pattern.lower()] = intent["tag"]  # tag is a string
    responses_dict = {
        intent["tag"]: intent["responses"] for intent in knowledge
    }  # responses is a list
    return patterns_dict, responses_dict


def get_best_match(user_question: str, patterns: dict) -> str | None:
    matches: list = get_close_matches(
        user_question, patterns.keys(), n=1, cutoff=0.6
    )  # cutoff is the minimum similarity ratio
    if matches:
        return patterns[matches[0]]  # it will return the tag


def chat_bot(knowledge: dict):
    patterns, responses = extract_patterns_and_responses(knowledge)

    while True:
        user_question = input("You: ").lower()

        if user_question == "exit":
            break

        tag = get_best_match(user_question, patterns)

        if tag:
            response = random.randrange(
                0, len(responses[tag])
            )  # random response from the list
            answer = responses[tag][response]  # it will return the response
            print(f"Bot: {answer}")
        else:
            print("Bot: I'm sorry, I don't understand, try rephrasing")


if __name__ == "__main__":
    knowledge = get_knowledge("intents.json")

    chat_bot(knowledge)
