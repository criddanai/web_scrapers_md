import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.text