import asyncio
import aiohttp

from bs4 import BeautifulSoup
from urllib.parse import (
    urljoin,
    urlparse
)

visited = set()


def normalize_url(url):

    parsed = urlparse(url)

    return (
        f"{parsed.scheme}://"
        f"{parsed.netloc}"
        f"{parsed.path}"
    )


async def fetch_html(session, url):

    try:

        async with session.get(
            url,
            timeout=20,
            ssl=False
        ) as response:

            if response.status != 200:
                return None

            return await response.text()

    except Exception as e:

        print(
            f"❌ FETCH ERROR: {url}"
        )

        print(e)

        return None


def allow_url(url):

    url = url.lower()

    exclude_patterns = [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".pdf",
        ".zip",
        ".csv",
        ".json",
        ".xml",
        ".ico",

        "/login",
        "/logout",
        "/signup",
        "/register",
        "/privacy",
        "/terms",
        "/cookies",
    ]

    for item in exclude_patterns:

        if item in url:
            return False

    return True


async def crawl(
    base_url,
    domain,
    max_concurrent=10
):

    queue = asyncio.Queue()

    await queue.put(base_url)

    results = []

    connector = aiohttp.TCPConnector(
        limit=max_concurrent
    )

    async with aiohttp.ClientSession(
        connector=connector,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    ) as session:

        async def worker():

            while True:

                url = await queue.get()

                normalized = normalize_url(
                    url
                )

                if normalized in visited:

                    queue.task_done()
                    continue

                visited.add(normalized)

                print(
                    f"🔎 Crawling: {url}"
                )

                html = await fetch_html(
                    session,
                    url
                )

                if html:

                    results.append(url)

                    soup = BeautifulSoup(
                        html,
                        "lxml"
                    )

                    for a in soup.find_all(
                        "a",
                        href=True
                    ):

                        href = (
                            a["href"]
                            .strip()
                        )

                        if href.startswith("#"):
                            continue

                        if href.startswith("mailto:"):
                            continue

                        if href.startswith(
                            "javascript:"
                        ):
                            continue

                        full_url = urljoin(
                            url,
                            href
                        )

                        full_url = normalize_url(
                            full_url
                        )

                        if domain not in full_url:
                            continue

                        if not allow_url(
                            full_url
                        ):
                            continue

                        if (
                            full_url
                            not in visited
                        ):

                            await queue.put(
                                full_url
                            )

                queue.task_done()

        tasks = [

            asyncio.create_task(
                worker()
            )

            for _ in range(
                max_concurrent
            )
        ]

        await queue.join()

        for task in tasks:
            task.cancel()

    MAX_PAGES = 300
    if len(results) >= MAX_PAGES:
        return results

    print(
        f"\n✅ Total Pages Found: "
        f"{len(results)}"
    )

    return results