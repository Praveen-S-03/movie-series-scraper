from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# ------------------------------------------------------
# 1. Scrape  Movies List
# ------------------------------------------------------
print("Scraping  Best Movies...")

MOVIE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(MOVIE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract movie titles
scrapped_data = soup.find_all(name="h3", class_="title")
movie_list = [movie.get_text(strip=True) for movie in scrapped_data]

# Reverse order (since list is 100 → 1 on site)
movie_list = movie_list[::-1]

# Save to CSV
df_movies = pd.DataFrame(movie_list, columns=["Movie Title"])
df_movies.to_csv("movies.csv", index=False)
print("✅ Movies saved to movies.csv")

# ---------------------------------------------------
# 2. Scrape  Series List
# ---------------------------------------------------
print("Scraping IMDb Top TV Series...")

IMDB_URL = "https://www.imdb.com/search/title/?title_type=tv_series&sort=num_votes,desc"

# Setup Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(IMDB_URL)

# Scrape series titles
series_data = driver.find_elements(By.TAG_NAME,value="h3")
series_list = [series.text for series in series_data[:50]]  # top 50

# Save to CSV
df_series = pd.DataFrame(series_list, columns=["Series Title"])
df_series.to_csv("series.csv", index=False)
print("✅ Series saved to series.csv")

driver.quit()
print("🎉 Scraping complete!")
