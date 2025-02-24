import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Create data
students = [f"Student_{i+1}" for i in range(10)]
subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Education']

# Generate random marks between 60 and 100
marks = np.random.randint(60, 101, size=(10, 6))

# Create a DataFrame
df = pd.DataFrame(marks, columns=subjects, index=students)

# Add a 'Total' column
df['Total'] = df.sum(axis=1)

# Add an 'Average' column
df['Average'] = df['Total'] / 6

# Round the 'Average' column to 2 decimal places
df['Average'] = df['Average'].round(2)

# Save to Excel file
excel_file = 'student_marks.xlsx'
df.to_excel(excel_file)

print(f"Excel file '{excel_file}' has been created successfully.")
