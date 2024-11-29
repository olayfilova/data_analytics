from typing import Optional
import pandas as pd
import logging
from pathlib import Path
import numpy as np

# 1
def clean_dataset(
        df: pd.DataFrame,
        output_file: str = "my_output.csv",
        yes_no_standardize: bool = True
) -> Optional[pd.DataFrame]:
    """
    Clean the dataset by removing null values and standardizing Yes/No values.

    Args:
        df: Input DataFrame
        output_file: Path to save the cleaned data
        yes_no_standardize: Whether to standardize Yes/No values

    Returns:
        Cleaned DataFrame or None if error occurs
    """
    try:
        # Validate input
        if df.empty:
            raise ValueError("Input DataFrame is empty")

        original_count = len(df)

        # Standardize Yes/No if requested
        if yes_no_standardize:
            df = df.replace({'Yes': 'YES', 'No': 'NO'}, regex=False)

        # Remove null values
        clean_df = df.dropna()

        if clean_df.empty:
            raise ValueError("All rows contained null values")

        # Save to CSV
        clean_df.to_csv(output_file, index=False)

        # Log results
        logging.info(f"Cleaned {original_count - len(clean_df)} rows")
        logging.info(f"Saved cleaned data to {output_file}")

        return clean_df

    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        # Read your data
        file_path = '/Users/olgafilova/Downloads/ChicagoCrimeData.csv'
        df = pd.read_csv(file_path)

        # Clean the data
        cleaned_df = clean_dataset(df)

        if cleaned_df is not None:
            print("Data cleaning successful")
            print(f"Original rows: {len(df)}")
            print(f"Cleaned rows: {len(cleaned_df)}")
        else:
            print("Data cleaning failed")

    except Exception as e:
        print(f"Error: {e}")



# serious = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# serious = [i * 2 for i in serious]
# print(serious)
# print(serious[9])
# print(serious[-1])
#
# shapes = ['square', 'circle', 'triangle', 'rectangle', 'trapezoid', 'rhombus', 'parallelogram', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']
# print(shapes)
# print(shapes[3])
#
# # 2
# salaries= pd.Series([100,200,500],
#         index=['John','Jane', "Bob"])
# # salaries = {'John': 100, 'Jane': 200, 'Bob': 300}
# salaries['car']=500
#
# salaries['Diva'] = np.nan
#
# df = pd.DataFrame(salaries, index=[0])
# df.fillna(salaries.median(), inplace=True)
# print(df)
#
# # df.to_csv('my_output2.csv', index=False)
#
#
# # 3
# salaries = {'John': 100, 'Jane': 200, 'Bob': 300}
# salaries['car']=500
#
# salaries['Diva'] = np.nan
#
# df = pd.DataFrame(salaries, index=[0])
# df.fillna(0, inplace=True)
# print(df)
# # df.to_csv('my_output.csv', index=False)
#
# # 4 dict to df
# salaries1 = {'John': 100, 'Jane': 200, 'Bob': 300}
# df = pd.DataFrame(salaries1, index=[0])
# print(df)

# # 5
# df1 = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), index=range(1, 101), columns=list('ABCDE'))
# # print(df1)
#
# df1.at[1, 'A'] = 100
# df1.at[1, 'B'] = 100
# df1.at[2, 'c'] = 100
# df1.at[2, 'd'] = 100
# df1.at[3, 'c'] = 100
# df1.at[3, 'd'] = 100
# df1.at[2, 'C'] = 0
# df1.at[2, 'D'] = 0
# print(df1)
# # print(pd.isnull(df1))
# print(df1.dropna(how='all', axis=0))
# print(df1.fillna(-76))
#
# df3 = pd.read_csv('/Users/olgafilova/Downloads/ChicagoCrimeData.csv')
# print(df3.head())
# print(df3.columns.tolist())
#
# print(df3.describe())
# # print(df3[df3['BEAT'] == df3['BEAT'].describe().loc['mean']])
# # # simplified
# # print(df3['BEAT'].describe().loc['mean'])
# # print(((df1['A']==100)&(df1['B']==100))|(df1['C']==100))
# print(df1['c'].apply(np.max))
# #
# print(df1['A'].apply(lambda x: x*2))
# print(df3)
#
# col_to_show=['LOCATION']
# col_to_show2 = ['LATITUDE', 'BEAT']
# print(df3.groupby(['BEAT'])[col_to_show].describe(percentiles=[0.5]))
# print(df3.groupby(['LATITUDE'])[col_to_show2].agg([min, max, np.std, np.mean]))
#
# #

# df1 = pd.DataFrame(np.random.randint(0, 100, size=(10, 5)), index=range(1, 11), columns=list('ABCDE'))
# print(df1)
# print(df1['A'].apply(lambda x: x*2))

df = pd.DataFrame({'A':[100, 2, 100, 100, 5],'B':[1, 2, 3, 4, 5]})
print(df)
print(df['B'].rolling(window=2).mean())
print(df['B'].expanding(min_periods=1).mean())
df['previous']=df.groupby('A')['B'].shift(1)
print(df)

