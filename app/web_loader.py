import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document


def load_urls(file_path):
    documents = []

    with open(file_path, "r") as f:
        urls = f.readlines()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        print(f"Fetching: {url}")

        try:
            response = requests.get(url, timeout=10)

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove scripts & styles
            for tag in soup(["script", "style", "nav", "footer"]):
                tag.extract()

            text = soup.get_text(separator="\n")

            documents.append(
                Document(
                    page_content=text,
                    metadata={"source": url}
                )
            )

        except Exception as e:
            print(f"Error loading {url}: {e}")

    return documents