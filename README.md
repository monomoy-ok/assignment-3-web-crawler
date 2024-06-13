# Web Scraper for Medical Diseases Data

## Overview
This Python script utilizes Selenium and BeautifulSoup to scrape medical disease information from 1mg.com, focusing on disease names, URLs, overview, and key facts. The data is then stored in a JSON file for further analysis or use.

## Requirements
- Python 3.x
- Selenium
- ChromeDriver (ensure it matches your Chrome browser version)
- BeautifulSoup

## Installation
1. **Install Python**: If Python is not installed, download and install it from [python.org](https://www.python.org/).
2. **Install Dependencies**: Install required Python packages using pip:
   ```bash
   pip install selenium beautifulsoup4
   ```
3. **Download ChromeDriver**: Download ChromeDriver matching your Chrome browser version from [chromedriver.chromium.org](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the executable and set `CHROME_DRIVER_PATH` in the script to its location.

## Usage
1. **Run the Script**:
   - Ensure ChromeDriver is set up and `CHROME_DRIVER_PATH` is correctly configured in the script.
   - Execute the script `app.py` using Python:
     ```bash
     python app.py
     ```
2. **Output**:
   - The script will start scraping disease data from [1mg.com](https://www.1mg.com/).
   - It will print each disease found along with its URL.
   - Data for the first 10 diseases (name, URL, overview, key facts) will be scraped and stored in a JSON file named `diseases_data.json`.

## Script Details
- **get_diseases_list**: Fetches a list of diseases from the 1mg.com page using Selenium for dynamic content loading and BeautifulSoup for HTML parsing.
- **get_disease_details**: Retrieves detailed information (overview, key facts) for a specific disease from its URL.
- **scrape_all_diseases**: Main function that orchestrates the scraping process, collects data for multiple diseases, and saves it to a JSON file.

## Notes
- **Headless Mode**: The script runs in headless mode (no visible browser window) to avoid interruptions during scraping.
- **Delay**: Time delays are implemented to ensure the website responds correctly and to adhere to ethical scraping practices.
- **Error Handling**: Minimal error handling is included; adjustments may be necessary based on website changes or exceptions encountered during runtime.

## Future Improvements
- Enhance data extraction to include additional details such as symptoms, causes, types, and treatment options.
- Implement logging for better debugging and monitoring of the scraping process.
- Optimize performance by refining wait times and enhancing the scraping logic.

