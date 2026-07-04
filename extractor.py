from bs4 import BeautifulSoup


def extract_main(html):

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    selectors = [
        "main",
        "article",
        '[role="main"]',
        ".content",
        ".markdown-body"
    ]

    for selector in selectors:

        obj = soup.select_one(
            selector
        )

        if obj:
            return str(obj)

    return str(soup)