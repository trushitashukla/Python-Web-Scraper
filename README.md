# 🌐 Web Scraper & Data Extractor

A Python-based web scraping application that extracts useful information from websites and presents it in a simple, organized format.

## 📌 Project Description

Web Scraper & Data Extractor is a Python application that collects information from a given webpage. It extracts the page title, headings, links, and image URLs using web scraping techniques and displays the collected data through a Streamlit interface.

The extracted information can also be searched, filtered, and exported as a CSV file.

## ✨ Features

* Enter any accessible webpage URL
* Extract webpage title
* Extract H1, H2, and H3 headings
* Extract webpage links
* Extract image URLs
* Convert relative URLs into complete URLs
* Remove duplicate links and images
* Search and filter extracted information
* Display data in organized tables
* Export scraped data as a CSV file
* Basic error handling for invalid or inaccessible URLs

## 🛠️ Technologies Used

* **Python**
* **Requests** – Fetches webpage content
* **BeautifulSoup** – Parses HTML
* **Pandas** – Organizes data and creates CSV files
* **Streamlit** – Provides the web-based user interface

## 📂 Project Structure

```text
Python-Web-Scraper/
│
├── app.py
├── scraper.py
├── requirements.txt
├── README.md
│
└── data/
    └── scraped_data.csv
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Python-Web-Scraper
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

### Basic Workflow

```text
Enter Website URL
       ↓
Fetch Webpage
       ↓
Parse HTML
       ↓
Extract Data
       ↓
Display Results
       ↓
Search / Filter
       ↓
Export as CSV
```

## 📊 Data Extracted

The application extracts:

| Data       | Description                         |
| ---------- | ----------------------------------- |
| Page Title | Title of the webpage                |
| Headings   | H1, H2 and H3 headings              |
| Links      | Links available on the webpage      |
| Images     | Image URLs available on the webpage |

## 🎯 Applications

* Website content analysis
* Data collection
* Basic web research
* Learning web scraping
* Extracting structured information from webpages

## ⚠️ Note

The scraper works with publicly accessible webpages that allow automated requests. Some websites may block scraping or require JavaScript to display their content.

## 👥 Project

**Mini Project – Python**

Developed as part of the academic mini project.

## 📄 License

This project is created for educational purposes.
