# SkyScraper: Python Web Scraping for Air Travel Insights

SkyScraper is a Python web scraping project using Selenium to extract air travel information from the Kayak website. It includes three scripts, each tailored to provide insights into different aspects of air travel.


## Table of Contents

- [List Of Flights](#list-of-flights)
- [List Of Airlines](#list-of-airlines)
- [Airline Ratings](#airline-ratings)
- [Dependencies](#dependencies)
- [Output](#output)
- [Notes](#notes)
- [License](#license)

## List Of Flights

The `list_of_flights.py` script navigates the Kayak flights page, collects available flights, and saves the data to "List_Of_Flights.csv."

## List Of Airlines

The `list_of_airlines.py` script explores details about different airlines, gathering information like names and prices. The results are saved to "List_Of_Airlines.csv."

## Airline Ratings

The `airline_ratings.py` script delves into airline ratings, extracting overall ratings, reviews, and specific category ratings. The outcomes are saved to "Airline_ratings.csv."



## Dependencies

- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)


## Output

Upon successful execution, the project generates three CSV files in the root directory:

- "List_Of_Flights.csv"
- "List_Of_Airlines.csv"
- "Airline_ratings.csv"

## Notes

- Adjust the paths and configurations in the scripts as needed.
- Ensure the correct version of ChromeDriver for your Chrome browser.

## License

This project is licensed under the [MIT License](LICENSE).