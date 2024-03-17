import re
from collections import Counter

from PyPDF2 import PdfReader


def read_pdf(pdf_path) -> list[str]:
    with open(pdf_path, "rb") as pdf:
        reader = PdfReader(pdf, strict=False)

        print("Pages: ", len(reader.pages))
        print("*" * 10)
        print()
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())
        all_words += [word for word in split_text if word]

    return Counter(all_words)


if __name__ == "__main__":
    pdf_path = "sample.pdf"
    text = read_pdf(pdf_path)
    words = count_words(text)

    top_words = words.most_common(5)

    print(*text)
    print()
    print("*" * 10)
    print("Top words")
    for word, count in top_words:
        print(f"{word:10}: {count}")
    print("*" * 10)
    print()
    total_words = sum(words.values())
    print(f"Word count: {total_words}")

    total_char = sum(len(page) for page in text)
    print(f"Character count: {total_char}")
