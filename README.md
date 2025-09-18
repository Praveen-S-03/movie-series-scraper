Built an automated ETL pipeline that scrapes raw movie and TV series information from multiple web sources, cleans and transforms the data into structured CSV datasets, enabling further insights and analytics.

# movie-series-scraper
ETL Pipeline for Movie and TV Series Data (Web Scraping to Structured CSV)
# 🎬 Movie & TV Series Data Scraper

This project demonstrates automated web scraping using **Python, BeautifulSoup, Selenium, and Pandas**.  
It collects data from two sources:  

- **Empire Online (Archive)** → Top 100 Movies of All Time  
- **IMDb** → Top 50 TV Series (sorted by votes)  

The data is cleaned, structured, and exported into **CSV files** for further analytics.

---

## 📌 Features
- Scrapes **100 best movies** from Empire Online (archived version).  
- Scrapes **50 most popular TV series** from IMDb with details:  
  - Title  
  - Year  
  - IMDb Rating  
  - Number of Votes  
- Stores data into structured CSV files (`movies.csv` and `series.csv`).  
- Built using Python’s **BeautifulSoup, Selenium, and Pandas**.  
- Reusable and extendable for similar web scraping tasks.  

---

## 🛠️ Tech Stack
- **Python 3**  
- **BeautifulSoup** – for parsing static web pages  
- **Selenium** – for scraping dynamic IMDb content  
- **Pandas** – for cleaning and exporting data  

---

## 📂 Project Structure
├── movies.csv # Top 100 Movies dataset
├── series.csv # Top 50 TV Series dataset
├── scraper.py # Combined Python script
└── README.md # Project documentation
---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/movie-series-scraper.git
   cd movie-series-scraper
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the scraper:

bash
Copy code
python scraper.py
Output CSV files will be generated in the project folder:

movies.csv

series.csv

📊 Sample Output
movies.csv

Movie Title
The Godfather
The Shawshank Redemption
...

series.csv

Title	Year	Rating	Votes
Game of Thrones	(2011–2019)	9.2	2,000,000
Breaking Bad	(2008–2013)	9.5	1,800,000
...	...	...	...

🌟 Future Improvements
Add genres, runtime, and directors to the datasets.

Perform data analysis & visualization (e.g., rating distributions, vote trends).

Deploy as a data pipeline or API for real-time scraping.

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for educational or commercial purposes.

