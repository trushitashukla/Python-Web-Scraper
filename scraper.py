import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_website(url):
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Page title
    title = soup.title.string.strip() if soup.title else "No title found"

    # Headings
    headings = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(" ", strip=True)

        if text:
            headings.append(text)

    # Links
    links = []

    for tag in soup.find_all("a", href=True):
        full_url = urljoin(url, tag["href"])

        if full_url not in links:
            links.append(full_url)

    # Images
    images = []

    for tag in soup.find_all("img", src=True):
        full_url = urljoin(url, tag["src"])

        if full_url not in images:
            images.append(full_url)

    return {
        "title": title,
        "headings": headings,
        "links": links,
        "images": images
    }