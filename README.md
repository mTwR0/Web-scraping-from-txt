# Car Rental Data Extraction and Analysis

This Python script automates the extraction of car rental information from HTML files originally downloaded using UiPath automation. The script processes text files containing HTML code from two specific car rental websites, extracting details such as car type, provider, transmission, and price. It then organizes this data into Excel spreadsheets named after the cities for which the rentals were searched.

## Features

- **Automated Data Extraction**: Processes HTML content from text files downloaded via UiPath automation, avoiding bot detection issues encountered with direct Python scraping.
- **File Management**: Groups text files based on specific naming conventions derived from '_regula.txt', separating them into lists (`rentalcars_files` and `economybookings_files`).
- **HTML Parsing**: Utilizes BeautifulSoup to navigate through HTML elements (`div`, `span`, etc.) and extract relevant car rental details.
- **Dynamic Date Handling**: Computes `DATA_START` and `DATA_STOP` based on rules specified in '_regula.txt' for accurate date ranges.
- **Excel Output**: Generates Excel files for each city, containing structured data columns (`MARCA`, `PROVIDER`, `TRANSMISIE`, `PRET`, `DATA_START`, `DATA_STOP`).

## Usage

1. **Setup**: Ensure text files downloaded by UiPath are stored in the specified directories (`HTML_PATH` and `TXT_PATH`).
2. **Execution**: Run the script to parse HTML data from text files and organize it into Excel spreadsheets.

