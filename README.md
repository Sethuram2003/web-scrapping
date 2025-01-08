# 🌐 Web Scraping Financial Data Toolkit

A comprehensive Python-based web scraping toolkit that extracts financial data using multiple approaches including Selenium, BeautifulSoup, and requests library, helping you gather and analyze financial metrics efficiently.

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/Beautiful_Soup-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

## 📚 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Contributing](#contributing)

## ✨ Features

- **Multiple Scraping Methods**: Support for Selenium, BeautifulSoup, and requests
- **Financial Data Extraction**: Comprehensive metrics collection
- **Automated Processing**: Batch URL processing capabilities
- **Data Management**: CSV input/output handling
- **Error Handling**: Robust error recovery system
- **Rate Limiting**: Smart request throttling

## 🗂️ Project Structure

```
web-scrapping/
├── apidata_webscarpping.py    # Single URL scraper (Selenium)
├── selenium_simple.py         # Multi-URL processor
├── webscrapping_csv.py        # CypherHunter product scraper
├── using_pandas.py            # Pandas data processing
├── final_testing.py          # Testing module
├── cypherhunter_products.csv # Product URLs database
├── output.csv                # Financial data output
└── moonwell_page_pretty.html # Sample HTML
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/Sethuram2003/web-scrapping.git
cd web-scrapping
```

2. Install required dependencies
```bash
pip install selenium
pip install beautifulsoup4
pip install requests
pip install pandas
```

3. Set up WebDriver
- Download ChromeDriver
- Add to system PATH or project directory

## ⚙️ Configuration

1. Configure User-Agent headers in scripts:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

2. Adjust rate limiting settings if needed

## 📖 Usage

### Product URL Collection
```bash
python webscrapping_csv.py
```

### Single URL Scraping
```bash
python apidata_webscarpping.py
```

### Bulk URL Processing
```bash
python selenium_simple.py
```

## 🔧 Technical Details

### Components

- **apidata_webscarpping.py**
  - Selenium-based single URL scraping
  - Headless browser automation
  - Financial data extraction

- **webscrapping_csv.py**
  - BeautifulSoup implementation
  - Product information gathering
  - Pagination handling

- **selenium_simple.py**
  - Batch URL processing
  - Data aggregation
  - CSV output generation

### Data Formats

#### Input CSV Format
```csv
Title,URL
Product1,https://example.com/product1
Product2,https://example.com/product2
```

#### Output CSV Format
```csv
Title,Market Cap,Fully Diluted Valuation,24H Trading Volume,Circulating Supply,Total Supply,Max Supply
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📝 Notes

- Respect website terms of service
- Monitor rate limiting
- Regular code maintenance recommended
- Check robots.txt before scraping

## ⚠️ Requirements

- Python 3.x
- Chrome Browser
- Internet connection
- Required Python packages:
  - selenium
  - beautifulsoup4
  - requests
  - pandas

## 📄 License

This project is licensed under the Apache2.0 License - see the LICENSE file for details.


---
<div align="center">

Created with ❤️ by Sethuram2003

</div>
