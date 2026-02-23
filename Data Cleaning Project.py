# ─────────────────────────────────────────────
# 🧼✨ WIZARD'S DATA CLEANING SPELLBOOK ✨🧼
# ─────────────────────────────────────────────
"""
Wizard’s Data Cleaning Spellbook is a colorful Python CLI tool that safely loads 
a dataset, checks structure, removes duplicates, handles missing values 
(drop or smart replace), previews results, and exports a cleaned CSV. 
Designed with soft, readable colors for bright screens.
"""

import pandas as pd
import os
import sys
from tabulate import tabulate

# 🎨 Soft Terminal Colors (White-Screen Friendly)
class Colors:
    HEADER = '\033[38;5;25m'     # Soft Blue
    BLUE = '\033[38;5;31m'       # Calm Blue
    CYAN = '\033[38;5;37m'       # Teal
    GREEN = '\033[38;5;34m'      # Soft Green
    GOLD = '\033[38;5;136m'      # Muted Gold
    ERROR = '\033[38;5;124m'     # Soft Dark Red
    END = '\033[0m'
    BOLD = '\033[1m'

# ────────────── Helper Functions ──────────────
def line(char="─"):
    print(f"{Colors.CYAN}{char*70}{Colors.END}")

def box_title(title_text):
    line()
    print(f"{Colors.HEADER}{Colors.BOLD}{title_text:^70}{Colors.END}")
    line()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_table(df, rows=5, table_name="Table Preview"):
    box_title(f"👀 {table_name}")
    try:
        print(tabulate(df.head(rows), headers='keys',
                       tablefmt='fancy_grid', showindex=True))
    except Exception as e:
        print(f"{Colors.ERROR}⚠️ Could not display table: {e}{Colors.END}")
    print()

# ────────────── Load Dataset Safely ──────────────
file_path = "data_cleaning_practice_dataset.csv"  # ← Keep file in same folder

try:
    data = pd.read_csv(file_path, encoding="latin1")
except FileNotFoundError:
    print(f"{Colors.ERROR}❌ File not found: {file_path}{Colors.END}")
    sys.exit()
except Exception as e:
    print(f"{Colors.ERROR}❌ Error loading file: {e}{Colors.END}")
    sys.exit()

# ────────────── Start Message ──────────────
clear()
box_title("✨ DATA CLEANING STARTED ✨")
print(f"{Colors.CYAN}Welcome, Data Wizard! Let the cleaning begin...{Colors.END}\n")

# ────────────── Dataset Overview ──────────────
box_title("📊 DATASET OVERVIEW")
info_df = pd.DataFrame({
    "Column": data.columns,
    "Data Type": [data[col].dtype for col in data.columns],
    "Non-Null Count": [data[col].count() for col in data.columns]
})
print(tabulate(info_df, headers='keys',
               tablefmt='fancy_grid', showindex=False))
print()

# ────────────── Duplicate Check ──────────────
box_title("🧾 DUPLICATE CHECK")
duplicates = data.duplicated().sum()
print(f"{Colors.GOLD}Duplicates found → {duplicates}{Colors.END}")

if duplicates > 0:
    data = data.drop_duplicates()
    print(f"{Colors.GREEN}Duplicates removed successfully!{Colors.END}")
print()

# ────────────── Missing Values ──────────────
box_title("❌ MISSING VALUES")
missing_df = pd.DataFrame({
    "Column": data.columns,
    "Missing Count": data.isnull().sum()
})
print(tabulate(missing_df, headers='keys',
               tablefmt='fancy_grid', showindex=False))
print()

# ────────────── User Cleaning Choice ──────────────
choice = input(
    f"{Colors.CYAN}Remove or replace missing values? (d / r) → {Colors.END}"
).strip().lower()

box_title("🔄 CLEANING IN PROGRESS")

if choice == "d":
    data = data.dropna()
    print(f"{Colors.GREEN}Rows with missing values removed!{Colors.END}")

elif choice == "r":
    for col in data.columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
        elif pd.api.types.is_object_dtype(data[col]):
            mode_val = data[col].mode()
            if not mode_val.empty:
                data[col] = data[col].fillna(mode_val[0])

    print(f"{Colors.GREEN}Missing values replaced successfully!{Colors.END}")

else:
    print(f"{Colors.ERROR}Invalid choice — no changes made.{Colors.END}")

# ────────────── Preview Cleaned Data ──────────────
display_table(data, rows=5, table_name="CLEANED DATA PREVIEW")

# ────────────── Save Cleaned Dataset ──────────────
output_file = "final_cleaned_data.csv"
try:
    data.to_csv(output_file, index=False)
    print(f"{Colors.GREEN}Clean data saved as → {output_file}{Colors.END}\n")
except Exception as e:
    print(f"{Colors.ERROR}Could not save file: {e}{Colors.END}")

box_title("🎉 DATA CLEANING COMPLETE 🎉")