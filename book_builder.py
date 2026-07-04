import os

MAX_WORDS = 100000

current_book = 1
current_words = 0


def save_book(content):

    global current_book
    global current_words

    os.makedirs(
        "output/books",
        exist_ok=True
    )

    words = len(
        content.split()
    )

    if (
        current_words + words
        > MAX_WORDS
    ):
        current_book += 1
        current_words = 0

    filename = (
        f"output/books/"
        f"book_{current_book:03d}.md"
    )

    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as f:

        f.write("\n\n")
        f.write(content)

    current_words += words