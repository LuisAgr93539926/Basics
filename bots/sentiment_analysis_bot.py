from dataclasses import dataclass

from textblob import TextBlob


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_sentiment(
    text: str, *, sensitivity: float
) -> Mood:  # * is to force-write sensitivity={value}
    polarity: float = TextBlob(text).sentiment.polarity

    good: float = sensitivity
    bad: float = -sensitivity

    if polarity > good:
        return Mood("😀", polarity)
    elif polarity < bad:
        return Mood("🙅‍♂️", polarity)
    else:
        return Mood("😐", polarity)


if __name__ == "__main__":
    while True:
        user_input: str = input("Enter how you feeling today (to exit write EXIT)-> ")
        mood: Mood = get_sentiment(user_input, sensitivity=0.3)

        if user_input == "EXIT":
            break

        print(f"'{mood.emoji} | ({mood.sentiment})")

    print("\nHave a good day!")
