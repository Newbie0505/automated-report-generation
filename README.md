#Title: AUTOMATED REPORT GENERATION

#Subtitle: A Python script that reads CSV data, analyzes it with Pandas, generates charts with Matplotlib, and creates a formatted PDF report using ReportLab.

#Name: Ankush Dhanokar

#Intern ID: CTIS9672

#Company: Codtech IT Solutions

#Domain: Python Programming

#Duration: 12 Weeks

#Mentor: Neela Santosh

#OutPut:
[final_report.pdf](https://github.com/user-attachments/files/28097254/final_report.pdf)

![Python](https://img.shields.io/badge/Python-3.10-blue) ![ReportLab](https://img.shields.io/badge/ReportLab-4.x-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.x-green) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A Python automation project that reads sales data from a CSV file, analyzes it using Pandas, generates charts using Matplotlib, and produces a professionally formatted PDF report using ReportLab.

---

## Task

> Develop a script that reads data from a file, analyzes it, and generates a formatted PDF report using libraries like FPDF or ReportLab.
>
> **Deliverable:** A script and a sample report.

---

## How It Works

CSV File → Pandas Analysis → Matplotlib Charts → ReportLab PDF

1. `data_loader.py` reads `sales_data.csv` into a Pandas DataFrame
2. `analyzer.py` computes revenue, profit, and regional statistics
3. `chart_gen.py` creates bar, line, and pie charts saved as PNG
4. `report_gen.py` assembles everything into a formatted PDF report

---

## Project Structure

    automated-report-generation/
    ├── data/
    │   └── sales_data.csv
    ├── src/
    │   ├── __init__.py
    │   ├── data_loader.py
    │   ├── analyzer.py
    │   ├── chart_gen.py
    │   └── report_gen.py
    ├── charts/
    ├── output/
    ├── main.py
    ├── requirements.txt
    └── README.md

---

## Setup and Run

Clone the repository

    git clone https://github.com/Newbie0505/automated-report-generation.git
    cd automated-report-generation

Create virtual environment

    python -m venv venv
    venv\Scripts\activate

Install dependencies

    pip install -r requirements.txt

Run the script

    python main.py

---

## Libraries Used

| Library | Purpose |
|---|---|
| pandas | Reading CSV file and data analysis |
| matplotlib | Generating bar, line and pie charts |
| reportlab | Creating the formatted PDF report |
| Pillow | Image handling for PDF embedding |

---

## Deliverables

| Deliverable | File |
|---|---|
| Script | main.py and all files in src/ |
| Sample Report | output/final_report.pdf |

---

## Author

Newbie0505
Internship Project — 2026
