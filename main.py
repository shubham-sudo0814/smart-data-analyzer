# ==========================================
# SMART DATA ANALYZER
# ==========================================
# This Program:
# 1. Reads CSV or Excel files
# 2. Cleans rough data
# 3. Removes missing values
# 4. Removes duplicate values
# 5. Shows dataset information
# 6. Performs basic revenue analysis
# 7. Saves cleaned dataset
# ==========================================


# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# PROJECT INTRODUCTION
# ==========================================

print("=" * 60)
print("WELCOME TO SMART DATA ANALYZER")
print("Convert Rough Data Into Clean Structured Data")
print("=" * 60)


# ==========================================
# FILE TYPE SELECTION
# ==========================================

try:

    print("\nSelect File Type:")
    print("1. CSV File")
    print("2. Excel File")

    type_of_file = int(
        input("\nEnter 1 for CSV or 2 for Excel: ")
    )

except:

    print("\nInvalid Input! Please enter numbers only.")
    exit()


# ==========================================
# USER FILE INPUT
# ==========================================

user_file = input(
    "\nEnter Full File Path: "
)


# ==========================================
# FILE LOADING SECTION
# ==========================================

try:

    # CSV FILE
    if type_of_file == 1:

        print("\nCSV File Detected...")

        sales_data = pd.read_csv(user_file)

    # EXCEL FILE
    elif type_of_file == 2:

        print("\nExcel File Detected...")

        sales_data = pd.read_excel(user_file)

    # INVALID OPTION
    else:

        print("\nInvalid File Type Selected")
        exit()

    print("\nFile Loaded Successfully!")

except Exception as e:

    print("\nFailed To Load File")
    print("Error:", e)

    exit()


# ==========================================
# DATASET PREVIEW
# ==========================================

print("\n" + "=" * 60)
print("FIRST 5 ROWS OF DATASET")
print("=" * 60)

print(sales_data.head())


# ==========================================
# DATASET SIZE
# ==========================================

print("\n" + "=" * 60)
print("DATASET SIZE")
print("=" * 60)

print(f"Total Rows    : {sales_data.shape[0]}")
print(f"Total Columns : {sales_data.shape[1]}")


# ==========================================
# COLUMN NAMES
# ==========================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(sales_data.columns)


# ==========================================
# MISSING VALUES CHECK
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(sales_data.isnull().sum())


# ==========================================
# CLEAN MISSING VALUES
# ==========================================
# Select numeric columns only

numeric_columns = sales_data.select_dtypes(
    include=np.number
).columns


# Fill missing numeric values using mean

sales_data[numeric_columns] = sales_data[
    numeric_columns
].fillna(
    sales_data[numeric_columns].mean()
)

print("\nMissing Values Cleaned Successfully!")


# ==========================================
# DUPLICATE VALUES CHECK
# ==========================================

print("\n" + "=" * 60)
print("DUPLICATE VALUES")
print("=" * 60)

print(
    "Duplicate Rows :",
    sales_data.duplicated().sum()
)


# ==========================================
# REMOVE DUPLICATES
# ==========================================

sales_data.drop_duplicates(
    inplace=True
)

print("\nDuplicate Rows Removed Successfully!")


# ==========================================
# DATA TYPES
# ==========================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(sales_data.dtypes)


# ==========================================
# REVENUE ANALYSIS
# ==========================================

if (
    'Quantity' in sales_data.columns
    and
    'Price' in sales_data.columns
):

    # Create Revenue Column

    sales_data['Revenue'] = (
        sales_data['Quantity']
        *
        sales_data['Price']
    )

    print("\nRevenue Column Created Successfully!")


    # Total Revenue

    total_revenue = sales_data[
        'Revenue'
    ].sum()

    print(
        f"\nTotal Revenue : {total_revenue}"
    )


else:

    print(
        "\nQuantity and Price Columns Not Found"
    )

# ==========================================
# DATA VISUALIZATION
# ==========================================

print("\n" + "=" * 60)
print("DATA VISUALIZATION")
print("=" * 60)


# ==========================================
# MISSING VALUES GRAPH
# ==========================================

missing_values = sales_data.isnull().sum()

plt.figure(figsize=(10, 5))

missing_values.plot(
    kind='bar'
)

plt.title("Missing Values In Dataset")
plt.xlabel("Columns")
plt.ylabel("Missing Values")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("missing_values_graph.png")

plt.show()


# ==========================================
# REVENUE VISUALIZATION
# ==========================================

if (
    'Product' in sales_data.columns
    and
    'Revenue' in sales_data.columns
):

    # Revenue By Product

    revenue_by_product = sales_data.groupby(
        'Product'
    )['Revenue'].sum().sort_values(
        ascending=False
    )


    # GRAPH

    plt.figure(figsize=(12, 6))

    revenue_by_product.head(10).plot(
        kind='bar',
        color='green'
    )

    plt.title("Top 10 Products By Revenue")

    plt.xlabel("Products")

    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("revenue_by_product.png")

    plt.show()

    print(
        "\nRevenue Visualization Created Successfully!"
    )


else:

    print(
        "\nProduct or Revenue Column Not Found"
    )


# ==========================================
# CORRELATION HEATMAP
# ==========================================

numeric_data = sales_data.select_dtypes(
    include=np.number
)

if not numeric_data.empty:

    plt.figure(figsize=(10, 6))

    sns.heatmap(
        numeric_data.corr(),
        annot=True,
        cmap='coolwarm'
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("correlation_heatmap.png")

    plt.show()

    print(
        "\nCorrelation Heatmap Created Successfully!"
    )

else:

    print(
        "\nNo Numeric Data Available For Heatmap"
    )
# ==========================================
# SAVE CLEANED DATASET
# ==========================================

sales_data.to_csv(
    "cleaned_sales_data.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully!")
print("File Name : cleaned_sales_data.csv")


# ==========================================
# PROGRAM COMPLETED
# ==========================================

print("\n" + "=" * 60)
print("PROCESS COMPLETED SUCCESSFULLY")
print("=" * 60)
print("Your Data Has Been Cleaned Successfully!")