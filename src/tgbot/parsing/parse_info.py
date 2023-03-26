from typing import Callable, Iterator
import aiohttp
from bs4 import BeautifulSoup


def get_bachelor_text(text: str) -> Iterator[tuple[str, str]]:
    soup = BeautifulSoup(text, "html.parser")
    titles = soup.find_all("h3", {"class": "card__title"})
    texts = soup.find_all("div", {"class": "card__subtitle"})
    return zip(
        [f"📑{title.text.lower()}" for title in titles],
        [f"✅{info.text.strip()}" for info in texts]
    )


def get_master_text(text: str) -> Iterator[tuple[str, str]]:
    soup = BeautifulSoup(text, "html.parser")
    titles = soup.find_all("h2", {"class": "how-to-proceed__info-title"})
    texts = soup.find_all("div", {"class": "how-to-proceed__info-text"})
    return zip(
        [f"📑{title.text.lower()}" for title in titles],
        [f"✅{info.text.strip()}" for info in texts]
    )


def get_postgraduate_text(text: str) -> Iterator[tuple[str, str]]:
    soup = BeautifulSoup(text, "html.parser")
    titles = soup.find_all("h3", {"class": "card__title"})
    texts = soup.find_all("div", {"class": "card__subtitle"})
    return zip(
        [f"📑{title.text.lower()}" for title in titles],
        [f"✅{info.text.strip()}" for info in texts]
    )


async def parse(
        url: str,
        get_info: Callable[[str], Iterator[tuple[str, str]]]) -> list[str]:
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            html = await response.text()
    return ["\n\n".join(x) for x in get_info(html)]
