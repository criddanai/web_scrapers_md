import os

from markdownify import (
    markdownify as md
)


def html_to_md(html):

    return md(html)


def save_page(
    filename,
    content
):

    os.makedirs(
        "output/md",
        exist_ok=True
    )

    path = (
        f"output/md/"
        f"{filename}.md"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)