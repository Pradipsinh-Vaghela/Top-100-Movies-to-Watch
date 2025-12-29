import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")

movie_list = [title.getText() for title in titles]

with open(file="movies.txt", mode="a", encoding="utf-8") as file:
    for movie_name in movie_list[::-1]:
        file.write(movie_name+"\n")
