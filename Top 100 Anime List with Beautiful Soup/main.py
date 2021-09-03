from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://www.sbs.com.au/popasia/blog/2017/10/12/votes-are-top-100-greatest-anime-all-time-voted-you")
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")
all_anime = soup.find_all(name="h3")
# print(all_anime[:-3])
anime_titles = [anime.text for anime in all_anime]
animes = anime_titles[:-3][::-1] # Reversing the list here with [::-1]

with open("animes.txt", mode="w") as file:
    for anime in animes:
        file.write(f"{anime}\n")