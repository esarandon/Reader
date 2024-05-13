import requests
from bs4 import BeautifulSoup
import os


def extract_title(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    return h1.text if h1 else None


def get_paragraphs_from_url(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all("p")
    return [p.text for p in paragraphs]


def save_and_open_file(file_path, text):
    with open(file_path, "w") as f:
        if isinstance(text, list):
            f.write("\n".join(text))
        else:
            f.write(text)

    if os.name == "nt":
        os.startfile(file_path)
    else:
        os.system(f'open "{file_path}"')


url = input("Enter a URL: ")

try:
    title = extract_title(url)
    paragraphs = get_paragraphs_from_url(url)

    if title:
        file_name = f"{title}.txt"
        file_path = os.path.join(os.getcwd(), file_name)
        save_and_open_file(file_path, paragraphs)
    else:
        print("No title found on the page.")

except Exception as e:
    print(f"An error occurred: {e}")
