# A Python Script that calculates basic descriptive statistics 
# for data files used in psychology.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data_questionnaire.csv', sep=';')



#Function to calculate descriptive statistics
def descriptive_statistics(data, variables, include_median=True, include_se=True):
    results = {}
    
    for var in variables:
        if data[var].dtype in ['object', 'string']:
            continue
        clean_data = data[var].dropna()
        
        stats = {
            'Mean': clean_data.mean(),
            'Std_Deviation': clean_data.std(),
            'Minimum': clean_data.min(),
            'Maximum': clean_data.max(),
        }
        
        if include_median:
            stats['Median'] = clean_data.median()
        
        if include_se:
            stats['Standard_Error'] = clean_data.std() / np.sqrt(len(clean_data))
        
        results[var] = stats
    
    return pd.DataFrame(results).T



variables = df.columns.tolist()

desc_stats = descriptive_statistics(df, variables, include_median=True, include_se=False)
print(desc_stats)

def create_bar_charts(data, variables):
    for var in variables:
        if data[var].dtype in ['object', 'string']:
            continue
        
        plt.figure(figsize=(8, 6))
        data[var].hist(bins=20)
        plt.title(f'Distribution of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.show()

create_bar_charts(df, variables)