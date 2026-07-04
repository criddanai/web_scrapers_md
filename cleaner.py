from bs4 import BeautifulSoup


def clean_html(html):

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    for tag in soup(
        [
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside"
        ]
    ):
        tag.decompose()

    return str(soup)