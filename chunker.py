import os
import json

CHUNK_SIZE = 1000
OVERLAP = 150


def split_text(text):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + CHUNK_SIZE

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += (
            CHUNK_SIZE - OVERLAP
        )

    return chunks


def save_chunks(
    content,
    title,
    url
):

    os.makedirs(
        "output/chunks",
        exist_ok=True
    )

    chunks = split_text(
        content
    )

    with open(
        "output/chunks/chunks.jsonl",
        "a",
        encoding="utf-8"
    ) as f:

        for index, chunk in enumerate(
            chunks,
            start=1
        ):

            record = {
                "title": title,
                "url": url,
                "chunk_id": index,
                "content": chunk
            }

            f.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                )
                + "\n"
            )