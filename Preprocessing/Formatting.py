import pandas as pd

file_path = 'C:/Users/asus/OneDrive/Documents/GitHub/Client-Predicting/Dataset/bank-full.csv' 
data = pd.read_csv(file_path, delimiter=';')

output_path = 'C:/Users/asus/OneDrive/Documents/GitHub/Client-Predicting/Dataset/DatasetML.csv' 
data.to_csv(output_path, index=False)

print(data.head())
