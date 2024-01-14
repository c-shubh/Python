import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}


# World
world_URL = "https://www.worldometers.info/coronavirus/"
world_page = requests.get(world_URL, headers=headers)
world_src = BeautifulSoup(world_page.content, "html.parser")

world = world_src.find_all(class_="maincounter-number")
world = [item.get_text().strip() for item in world]

world = world_src.find_all(class_="maincounter-number")
world = [item.get_text().strip() for item in world]
cases, deaths, recovered = world
print(f"world {cases=} {deaths=} {recovered=}")

# India
india_URL = "https://www.worldometers.info/coronavirus/country/india/"
india_page = requests.get(india_URL, headers=headers)
india_src = BeautifulSoup(india_page.content, "html.parser")

india = india_src.find_all(class_="maincounter-number")
india = [item.get_text().strip() for item in india]

india = india_src.find_all(class_="maincounter-number")
india = [item.get_text().strip() for item in india]
cases, deaths, recovered = india
print(f"india {cases=} {deaths=} {recovered=}")
