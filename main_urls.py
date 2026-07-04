import os

from core.fetcher import fetch
from core.extractor import extract_main
from core.cleaner import clean_html
from core.exporter import (
    save_page,
    html_to_md
)

from core.book_builder import (
    save_book
)

from core.chunker import (
    save_chunks
)


def load_urls():

    with open(
        "input_urls.txt",
        encoding="utf-8"
    ) as f:

        return [
            line.strip()
            for line in f
            if line.strip()
        ]


def create_name(url):

    return (
        url
        .replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
        .replace("#", "_")
    )


def main():

    urls = load_urls()

    print(
        f"Found {len(urls)} URLs"
    )

    for index, url in enumerate(
        urls,
        start=1
    ):

        print(
            f"[{index}/{len(urls)}]"
        )

        print(url)

        html = fetch(url)

        content = extract_main(
            html
        )

        clean = clean_html(
            content
        )

        md = html_to_md(
            clean
        )

        name = create_name(
            url
        )

        save_page(
            name,
            md
        )

        save_book(
            md
        )

        save_chunks(
            md,
            name,
            url
        )


if __name__ == "__main__":

    main()