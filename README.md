# IIT Bhubaneswar Summer Internship Assignment

This repository contains solutions for the IIT Bhubaneswar Summer Internship tasks implemented using Python.

The project covers:
- Python fundamentals
- File handling
- Error handling
- Data cleaning
- Data visualization
- Web scraping
- Data analysis
- Report generation

---

# Repository Structure

```bash
IITBBSR/
│
├── statics/
│   ├── task2/
│   ├── task5/
│   ├── task6/
│   ├── task8/
│   ├── task9/
│   └── task10/
│
├── .gitignore
├── task_1.py
├── task_2.py
├── task_3.py
├── task_4.py
├── task_5.ipynb
├── task_6.ipynb
├── task_7_report.md
├── task_8.ipynb
├── task_9.ipynb
└── task_10.py
```

---

# Requirements

- Python 3.10 or above

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
pandas
numpy
matplotlib
seaborn
requests
beautifulsoup4
scikit-learn
```

---

# Tasks Overview

## Task 1 — List & Dictionary Operations

Implemented:
- Duplicate removal
- Sorting integer list
- Frequency counting
- Maximum, minimum, and average calculation

Concepts used:
- Lists
- Dictionaries
- Loops
- Functions

---

## Task 2 — File Handling

Implemented:
- Reading log files
- Counting log types
- JSON output generation
- Most frequent log detection

Features:
- Random log generation support
- JSON file handling

---

## Task 3 — Functions & Error Handling

Implemented:
- `safe_divide(a, b)` function
- Division by zero handling
- Invalid input handling
- Meaningful error messages
- Proper docstrings

---

## Task 4 — Debugging

Implemented:
- Bug identification
- Corrected list removal logic
- Time complexity explanation

Covered:
- Why modifying lists during iteration causes issues
- Optimized approach explanation

---

## Task 5 — Data Cleaning

Dataset Used:
Digital Burnout and Productivity Analytics Dataset

Implemented:
- Missing value handling
- Duplicate row removal
- Dataset statistics
- Categorical encoding
- Clean dataset export

Libraries Used:
- Pandas
- NumPy
- Scikit-learn

---

## Task 6 — Data Visualization

Created multiple visualizations including:
- Histogram
- Scatter Plot
- Heatmap
- Bar Chart
- Boxplot

Features:
- Proper labels
- Titles
- Legends
- Saved plot images

Libraries Used:
- Matplotlib
- Seaborn

---

## Task 7 — Insights Report

Prepared a report containing:
- Dataset trends
- Observations
- Dataset issues
- Final conclusions

Report File:
```bash
task_7_report.md
```

---

## Task 8 — Web Scraper

Built a scraping pipeline using:
- Requests
- BeautifulSoup

Pipeline Features:
- Search-based scraping
- Video URL extraction
- Context-based collection
- CSV and JSON storage
- Exception handling
- Retry mechanisms
- Clean folder structure

Example contexts:
- AI generated videos
- Robotics demos
- Sports highlights
- Self-driving cars

---

## Task 9 — Context Based Scraping

Extended the scraping pipeline to:
- Accept multiple topics
- Merge collected results
- Remove duplicates
- Create categorized folders

Example structure:

```bash
videos/
├── robotics/
├── ai/
├── sports/
└── semiconductor/
```

---

## Task 10 — Data Summary & Analysis

Generated:
- Total videos collected
- Total unique creators
- Most common keywords
- Average engagement statistics
- Top-performing posts

Created visualizations:
- Videos per topic
- Top creators/websites

Generated outputs:
- `summary_report.txt`
- Visualization image files

---

# Features of the Project

- Modular and reusable code
- Proper folder organization
- Clean and maintainable implementation
- Meaningful comments and documentation
- Exception handling
- Avoided hardcoded paths
- CSV and JSON output support

---

# How to Run

Example:

```bash
python task_1.py
```

or run notebooks:

```bash
jupyter notebook
```

---

# Output Files

The repository includes:
- CSV files
- JSON files
- Cleaned datasets
- Visualization images
- Analysis reports
- Screenshots where necessary

---

# Author

Manohar Sripati

GitHub:
https://github.com/Manoharsripati6
