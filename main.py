import os
import sys
import asyncio

from urllib.parse import urlparse

from dotenv import load_dotenv

from core.crawler import crawl
from core.fetcher import fetch
from core.extractor import extract_main
from core.cleaner import clean_html

from core.exporter import (
    html_to_md,
    save_page
)

from core.book_builder import (
    save_book
)

from core.chunker import (
    save_chunks
)

load_dotenv()


BASE_URL = (
    sys.argv[1]
    if len(sys.argv) > 1
    else os.getenv("BASE_URL")
)

DOMAIN = os.getenv(
    "DOMAIN_FILTER"
)

MAX_CONCURRENT = int(
    os.getenv(
        "MAX_CONCURRENT",
        10
    )
)


def create_filename(url):

    path = (
        urlparse(url)
        .path
        .replace("/", "_")
        .replace(".html", "")
        .replace(".htm", "")
        .strip("_")
    )

    if not path:
        path = "home"

    return path


async def run():

    print(
        "\n🚀 Starting Crawler...\n"
    )

    links = await crawl(
        BASE_URL,
        DOMAIN,
        MAX_CONCURRENT
    )

    print(
        f"\n✅ Found {len(links)} pages\n"
    )

    # Save URLs
    with open(
        "output/urls.txt",
        "w",
        encoding="utf-8"
    ) as f:

        for link in links:
            f.write(link + "\n")

    for index, url in enumerate(
        links,
        start=1
    ):

        print(
            f"\n📄 [{index}/{len(links)}]"
        )

        print(url)

        try:

            html = fetch(url)

            content = extract_main(
                html
            )

            clean = clean_html(
                content
            )

            md_text = html_to_md(
                clean
            )

            filename = (
                create_filename(url)
            )

            # Save Page
            save_page(
                filename,
                md_text
            )

            # Save Book
            save_book(
                md_text
            )

            # Save Chunks
            save_chunks(
                content=md_text,
                title=filename,
                url=url
            )

        except Exception as e:

            print(
                f"❌ ERROR : {url}"
            )

            print(e)

            continue

    print(
        "\n✅ Finished\n"
    )


if __name__ == "__main__":

    asyncio.run(run())