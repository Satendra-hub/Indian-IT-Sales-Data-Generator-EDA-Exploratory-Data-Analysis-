# Indian-IT-Sales-Data-Generator-EDA-Exploratory-Data-Analysis-
This project generates a realistic synthetic dataset of Indian IT companies and performs a complete exploratory data analysis (EDA) using Python. It’s ideal for students, analysts, and developers looking to practice data visualization, statistical analysis, and portfolio building.
## 📦 Features

### 🔧 Dataset Generator (`data_generator.py`)
- Creates 100 rows of realistic IT project data
- Includes fields like company, region, sector, project type, revenue, duration, ratings, and delivery status
- Saves output as `indian_it_sales_data.csv`

### 📊 EDA Script (`eda_script.py`)
- Loads and inspects the dataset
- Displays:
  - Shape, columns, nulls, data types
  - Summary statistics
  - Unique value counts
- Visualizes:
  - Revenue distribution
  - Company-wise project count
  - Region-wise average revenue
  - Project duration histogram
  - Client rating distribution
  - Correlation heatmap
  - Revenue trend over time (if `start_date` exists)
- Saves summary to `eda_summary.txt`

## 📊 What You Can Do with EDA

EDA helps you **understand the data before modeling or decision-making**. Here's how you can use this dataset in EDA:

### 🔍 1. **Descriptive Statistics**
- Mean, median, mode of `monthly_revenue`, `employee_count`, `client_rating`
- Distribution of `project_duration`

### 📈 2. **Trend Analysis**
- Revenue growth over time (`start_date` vs `monthly_revenue`)
- Which regions or sectors generate the most revenue

### 📊 3. **Categorical Insights**
- Count of projects by `company_name`, `region`, `project_type`
- Delivery performance by company (`delivery_status`)

### 📉 4. **Correlation & Relationships**
- Does higher `employee_count` lead to better `client_rating`?
- Is `project_duration` linked to `delivery_status`?

### 📍 5. **Visualizations**
- Bar charts for project counts
- Line plots for revenue trends
- Heatmaps for correlation
- Pie charts for sector distribution

# 
## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/indian-it-sales-eda.git
   cd indian-it-sales-eda

pip install -r requirements.txt
python EDA_indian_it_sales_data.py
