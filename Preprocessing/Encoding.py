# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

uploaded = 'Dataset/DatasetML.csv' 

# Load the dataset
dataset_name = list(uploaded.keys())[0]
data = pd.read_csv(dataset_name)

# Display the first few rows and info of the dataset
print("Dataset Overview:")
print(data.head())
print("\nDataset Info:")
data.info()

# Analyze categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns
print("\nCategorical Columns:", categorical_columns)

# Check unique values in categorical columns
unique_values = {col: data[col].nunique() for col in categorical_columns}
print("\nUnique Values per Categorical Column:", unique_values)

# Encoding Process
# Copy of the dataset for encoding
encoded_data = data.copy()

# Apply One-Hot Encoding
one_hot_columns = ['marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome', 'y']
encoded_data = pd.get_dummies(encoded_data, columns=one_hot_columns, drop_first=True)

# Apply Label Encoding
label_encode_columns = ['job', 'month']
label_encoders = {}
for col in label_encode_columns:
    le = LabelEncoder()
    encoded_data[col] = le.fit_transform(encoded_data[col])
    label_encoders[col] = le  # Store encoders for possible inverse transformation later

# Display the encoded dataset
print("\nEncoded Dataset Overview:")
print(encoded_data.head())

# Save the encoded dataset to a CSV file
encoded_dataset_name = 'Dataset/encoded_dataset.csv'
encoded_data.to_csv(encoded_dataset_name, index=False)
print(f"\nEncoded dataset saved as {encoded_dataset_name}")
