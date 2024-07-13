import pandas as pd
import numpy as np

def preprocess_dataframe(df):
    # Create a copy of the DataFrame to avoid modifying the original
    df_processed = df.copy()
    
    # Identify numeric and categorical columns
    numeric_columns = df_processed.select_dtypes(include=[np.number]).columns
    categorical_columns = df_processed.select_dtypes(exclude=[np.number]).columns
    
    # Handle missing values
    # For numeric columns, impute with median
    for col in numeric_columns:
        df_processed[col].fillna(df_processed[col].median(), inplace=True)
    
    # For categorical columns, impute with most frequent value
    for col in categorical_columns:
        df_processed[col].fillna(df_processed[col].mode()[0], inplace=True)
    
    # Normalize numeric columns
    for col in numeric_columns:
        mean = df_processed[col].mean()
        std = df_processed[col].std()
        df_processed[col] = (df_processed[col] - mean) / std
    
    # Encode categorical columns
    df_processed = pd.get_dummies(df_processed, columns=categorical_columns, drop_first=True)
    
    return df_processed

# Example usage
# Create a sample DataFrame
df = pd.DataFrame({
    'age': [25, 30, np.nan, 40, 35],
    'income': [50000, 60000, 75000, np.nan, 65000],
    'gender': ['M', 'F', 'M', 'F', np.nan],
    'education': ['Bachelor', 'Master', np.nan, 'PhD', 'Bachelor']
})

print("Original DataFrame:")
print(df)

df_cleaned = preprocess_dataframe(df)

print("\nProcessed DataFrame:")
print(df_cleaned)
