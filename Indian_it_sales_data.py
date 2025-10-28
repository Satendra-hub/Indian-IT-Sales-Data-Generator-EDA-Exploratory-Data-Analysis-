import pandas as pd
import numpy as np
import random

# Define categories
companies = ['TCS', 'Infosys', 'Wipro', 'HCL', 'Tech Mahindra']
regions = ['North', 'South', 'East', 'West', 'Central']
sectors = ['BFSI', 'Retail', 'Healthcare', 'Manufacturing', 'Telecom']
projects = ['Cloud', 'AI/ML', 'Cybersecurity', 'ERP', 'Data Analytics']
statuses = ['On-time', 'Delayed', 'Cancelled']

# Generate 100 rows
data = []
for _ in range(100):
    start = pd.to_datetime('2020-01-01') + pd.DateOffset(months=random.randint(0, 60))
    duration = random.randint(3, 24)
    end = start + pd.DateOffset(months=duration)
    data.append({
        'company_name': random.choice(companies),
        'region': random.choice(regions),
        'client_sector': random.choice(sectors),
        'project_type': random.choice(projects),
        'monthly_revenue': np.random.randint(50, 500),  # in lakhs
        'employee_count': np.random.randint(10, 100),
        'project_duration': duration,
        'client_rating': round(np.random.uniform(3.0, 5.0), 1),
        'delivery_status': random.choice(statuses),
        'start_date': start.date(),
        'end_date': end.date()
    })

df = pd.DataFrame(data)
df.to_csv("indian_it_sales_data.csv", index=False)
print("✔️ Realistic Indian IT company dataset created.")