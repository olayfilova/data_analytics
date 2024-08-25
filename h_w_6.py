import csv
import pandas as pd
import sqlite3
import numpy as np

try:
    url = "https://lms.ithillel.ua/api/lms/files/66c39e4e7fb551d0ac564712"
    df = pd.read_csv(url)
    con = sqlite3.connect("archive.zip")
    df.to_sql("archive.zip", con, if_exists='replace', index=False, method='multi')
except:
    print("raise HTTPError(req.full_url, code, msg, hdrs, fp\
    urllib.error.HTTPError: HTTP Error 500: Internal Server Error\nкогда будем подключаться к базам? и кстати, не смогла сама округлить :) сама бы я недокрутила бы никогда в жизни")



file = '/Users/olgafilova/Downloads/student_performance_prediction.csv'


class MissingValueError(Exception):
    """Exception raised for rows with missing values."""
    pass

file = '/Users/olgafilova/Downloads/student_performance_prediction.csv'

data = []
try:
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            data.append(i)
    # print(data)

    df = pd.DataFrame(data[1:], columns=data[0])
    # print(df)


    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if df[col].dtype in [np.float64, np.int64]:
                df[col] = df[col].round(0)
        except ValueError:
            pass
        ## for i in df:
        ##    if isinstance(i, (float, int)):
        ##       res = df.round(i)
        ##print(res)
        # print(df)


    df = df.replace({'Yes':'YES', 'No': 'NO'})


    clean_data = []
    for index, row in df.iterrows():
        if row.isnull().any():
            print(f"Рядок {index + 1} містить пропуски. Пропущено.")
        else:
            clean_data.append(row)


    output_file = "my_output2.csv"
    clean_df = pd.DataFrame(clean_data, columns=df.columns)
    clean_df.to_csv(output_file, index=False)
    print(f"Файл '{output_file}' успішно збережено.")

except MissingValueError as e:
    print(e)



##################################################################################################я_сдалась_оч_сложно_а_а_а_а
# data = []
# try:
#     with open(file, 'r') as f:
#         reader = csv.reader(f)
#         for i in reader:
#             data.append(i)
#     # print(data)
#
#
#
#     df = pd.DataFrame(data)
#     df[df.select_dtypes(include=np.number).columns[:]] = df.select_dtypes(include=np.number).round(0)
#     # print(df)
#
#     for i in df:
#         if isinstance(i, (float, int)):
#             res = df.round(i)
#     # print(res)
#
#     res_replace = df.replace({'Yes':'YES', 'No': 'NO'})
#     print(res_replace)
#
# except MissingValueError:
#     for index, row in df.iterrows():
#         if row.isnull().any():
#             print("MissingValueError" f"Рядок {index + 1} містить пропуски. Пропущено.")
#
#
# output_file = "my_output.csv"
# df.to_csv(output_file, index=False)
# print(f"Файл '{output_file}' успішно збережено.")




