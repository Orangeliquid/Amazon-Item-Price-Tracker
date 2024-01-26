# Amazon Price Tracker

## Overview
This Python script tracks the price of a specified Amazon item through web scraping. If the current price falls below a user-defined threshold, an email notification is sent to alert the user.

## Features
- Web scraping of the desired Amazon URL to retrieve the current price of the item.
- Email notification to the user if the price drops below a predefined threshold.

## Requirements
- Python 3.x
- Required Python libraries: `requests`, `smtplib`, `os`, `bs4 (BeautifulSoup)`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Orangeliquid/amazon-price-tracker.git
   ```

1. Navigate to the project directory:
   ```bash
   cd amazon-price-tracker
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Set the following environmental variables in your configuration:
   - `AMAZON_ITEM_URL`: The URL of the Amazon item you want to track.
   - `USER_AGENT`: User agent string for the HTTP requests.
   - `MY_EMAIL`: Your Gmail address.
   - `MY_APP_PASS`: App password for Gmail authentication.

Usage

Run the script using the following command:
```bash
python amazon_price_tracker.py
```

Configuration

Ensure all environmental variables are set correctly in your configuration before running the script.

## License
This project is licensed under the [MIT License](LICENSE.txt).
