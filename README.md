# Data-Cleaning-Sample-Project
Wizard’s Data Cleaning Spellbook is a colorful Python CLI tool that safely loads a dataset, checks structure, removes duplicates, handles missing values (drop or smart replace), previews results, and exports a cleaned CSV. Designed with soft, readable colors for bright screens and beginner-friendly clarity. ✨
🧼 Wizard’s Data Cleaning Spellbook

A professional, beginner-friendly Python CLI data cleaning tool designed to safely inspect, clean, and export structured CSV datasets. Built with structured formatting and soft, eye-friendly terminal colors for clarity and readability.

📌 Overview

Wizard’s Data Cleaning Spellbook allows users to:

Load a dataset safely

Inspect dataset structure

Detect and remove duplicates

Identify missing values

Drop or intelligently replace missing data

Preview cleaned results in a formatted table

Export a cleaned CSV file

This project demonstrates practical data preprocessing using pandas in a clean command-line interface.

✨ Features

📊 Dataset overview (columns, data types, non-null counts)

🧾 Duplicate detection and removal

❌ Missing value summary table

🔄 Two cleaning options:

Drop rows with missing values

Replace numeric values with mean

Replace text values with mode

👀 Cleaned data preview using tabulate

💾 Automatic export to a new CSV file

🎨 Soft, white-screen optimized terminal color design

🛠️ Technologies Used

Python 3.x

pandas

tabulate

ANSI terminal formatting

📂 Project Structure
wizard-data-cleaning/
│
├── data_cleaning_practice_dataset.csv
├── final_cleaned_data.csv
├── wizard_data_cleaner.py
└── README.md
🚀 Installation

Clone the repository:

git clone https://github.com/your-username/wizard-data-cleaning.git
cd wizard-data-cleaning

Install dependencies:

pip install pandas tabulate
▶️ Usage

Place your dataset in the same folder as the script.

Run:

python wizard_data_cleaner.py

Choose:

(d) → Drop missing values  
(r) → Replace missing values

The cleaned dataset will be saved as:

final_cleaned_data.csv
🎯 Learning Value

This project demonstrates:

Data inspection techniques

Handling missing values correctly

Removing duplicates

CLI user interaction

Structured and readable terminal UI design
