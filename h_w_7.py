import boto3
import json

from openpyxl import Workbook
import requests
from openpyxl.chart import Reference, LineChart
from openpyxl.chart.axis import DateAxis


rates = []
for year in range(2020, 2024):
    for month in range(1, 13):
        r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
        if r.status_code == 200:
            response = json.loads(r.text)
            rate_usd = [i for i in response['exchangeRate'] if i['currency'] == 'USD']
            if rate_usd:
                print(year, month, rate_usd[0]['saleRate'])
                rates.append((f'01.{month:02}.{year}', rate_usd[0]['saleRate']))

print(rates)

wb = Workbook()
ws = wb.active
ws['A1'] = 'Date'
ws['B1'] = 'Rate'

for idx, rate in enumerate(rates, start=2):
    ws[f'A{idx}'] = rate[0]
    ws[f'B{idx}'] = rate[1]

data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(rates) + 1)
c1 = LineChart()
c1.title = "USD RATE"
c1.style = 13
c1.y_axis.title = 'Rate'
c1.x_axis.title = 'Date'
c1.y_axis.crossAx = 500
c1.x_axis = DateAxis(crossAx=100)
c1.x_axis.number_format = 'dd.mm.yyyy'
c1.x_axis.majorTimeUnit = "months"

c1.add_data(data, titles_from_data=True)
dates = Reference(ws, min_col=1, min_row=2, max_row=len(rates) + 1)
c1.set_categories(dates)

#smooth to False
for series in c1.series:
    series.smooth = False

ws.add_chart(c1, "D1")

wb.save("my_rate.xlsx")

#########################################################################################################################

# rates=[]
# for year in range(2020,2024):
#     for month in range(1,12):
#         r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
#         if r.status_code == 200:
#             response = json.loads(r.text)
#             rate_usd = [i for i in response['exchangeRate'] if i['currency'] == 'USD']
#                 # if not rate_usd:
#                 #     res = []
#                 #     print(res)
#             if rate_usd:
#                 print( year, month, rate_usd[0]['saleRate'])
#                 rates.append((f'01.{month:02}.{year}', rate_usd[0]['saleRate']))
#
# print(rates)
#
#
# wb = Workbook()
# ws = wb.active
# ws[f'A1'] = 'Date'
# ws[f'B1'] = 'Rate'
#
#
# for idx, rate in enumerate(rates, start=2):
#     ws[f'A{idx}'] = rate[0]
#     ws[f'B{idx}'] = rate[1]
#
#
# data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(rates)+1)
# c1 = LineChart()
#
# c1.title = "USD RATE"
# c1.style = 13
# c1.y_axis.title = 'Rate'
# c1.x_axis.title = 'Date'
# c1.y_axis.crossAx = 500
# c1.x_axis = DateAxis(crossAx=100)
# c1.x_axis.number_format = 'dd.mm.yyyy'
# c1.x_axis.majorTimeUnit = "months"
# # c1.x_axis.title = "Date"
# # s2 = c1.series[2]
# for series in c1.series:
#     series.smooth=False
#
#
#
# c1.add_data(data, titles_from_data=True)
# dates = Reference(ws, min_col=1, min_row=2, max_row=len(rates)+1)
# c1.set_categories(dates)
#
#
#
# ws.add_chart(c1, "d1")
#
# wb.save("my_rate.xlsx")




# ########################################################################################################################
#
# rates=[]
# for year in range(2020,2021):
#     for month in range(1,4):
#         r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
#         if r.status_code == 200:
#             response = json.loads(r.text)
#             rate_usd = [i for i in response['exchangeRate'] if i['currency'] == 'USD']
#                 # if not rate_usd:
#                 #     res = []
#                 #     print(res)
#             if rate_usd:
#                 print( year, month, rate_usd[0]['saleRate'])
#                 rates.append((f'01.{month:02}.{year}', rate_usd[0]['saleRate']))
#
# print(rates)
#
#
# wb = Workbook()
# ws = wb.active
# for idx, rate in enumerate(rates, start=1):
#     ws[f'A{idx}'] = rate[0]
#     ws[f'B{idx}'] = rate[1]
#
#
# c1 = LineChart()
# c1.title = "USD RATE"
# c1.style = 13
# c1.y_axis.title = 'Rate'
# c1.x_axis.title = 'Date'
#
# data = Reference(ws, min_col=1, min_row=1, max_col=3, max_row=len(rates))
# c1.add_data(data, titles_from_data=True)
#
# # Style the lines
# s1 = c1.series[0]
# s1.marker.symbol = "triangle"
# s1.marker.graphicalProperties.solidFill = "FF0000" # Marker filling
# s1.marker.graphicalProperties.line.solidFill = "FF0000" # Marker outline
#
# s1.graphicalProperties.line.noFill = True
#
# s2 = c1.series[1]
# s2.graphicalProperties.line.solidFill = "00AAAA"
# s2.graphicalProperties.line.dashStyle = "sysDot"
# s2.graphicalProperties.line.width = 100050 # width in EMUs
#
# # s2 = c1.series[2]
# s2.smooth = True # Make the line smooth
#
# ws.add_chart(c1, "d1")
#
# wb.save("my_rate.xlsx")




# ######################################
# for year in range(2020,2024):
#     for month in range(1,13):
# #         for day (but we look for 1st day of the month in conditions)
#         print(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
#
# r = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014')
# if r.status_code == 200:
#     # print(r.text)
#     response = json.loads(r.text)
#     # print(response)
#     rate_usd = [i for i in response['exchangeRate'] if i['currency'] == 'USD']
#     if not rate_usd:
#         res = []
#         print(res)
#     elif rate_usd:
#         res = rate_usd[0]
#         print(res)
#         print(res['saleRate'])




