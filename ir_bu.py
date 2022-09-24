import pandas
import pandas_datareader.data as web
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

from main import stock_name
from main import start_date
from main import end_date

#selected perion - first day of the month only
#start_date = "2020-01-01"
#end_date = "2020-12-01"



#start_date = "2015-01-01"
#end_date = "2020-12-01"




#INTEREST RATES

#importing cvs file
interest_rates_file = pandas.read_csv("/Users/Matej/Desktop/Stock/int_rates.csv", index_col=None)

#conversion of specific column to list
date_lst = interest_rates_file.DATE.to_list()
interest_rates_lst = interest_rates_file.INTDSRUSM193N.to_list()

#slicing the lists for the selected period
start_date_index = date_lst.index(start_date)
end_date_index = date_lst.index(end_date)

interest_rates_lst_sliced = interest_rates_lst[start_date_index:end_date_index+1]
date_lst_sliced = date_lst[start_date_index:end_date_index+1]

#combination of the two interest rates lists where date is the key and rate is the value
interest_rates_dict = dict()
for key in date_lst_sliced:
    for value in interest_rates_lst_sliced:
        interest_rates_dict[key] = value
        break

#STOCK
#importing cvs file
#stock_file = pandas.read_csv(stock_name)

stock_file = web.DataReader(name=stock_name, data_source='yahoo', start=start_date, end=end_date)
stock_file = stock_file.reset_index()


#conversion of specific column to list
date_stock_lst = list()
for date in stock_file.Date:
    date_new = pandas.Timestamp.date(date)
    date_time_obj = datetime.strptime(str(date_new), "%Y-%m-%d")
    date_str = date_time_obj.strftime('%Y-%m-%d')
    date_stock_lst.append(date_str)

price_stock_lst = stock_file.Close.to_list()


#combination of the two stock lists where date is the key and price is the value

stock_dict = dict()
for key in date_stock_lst:
    for value in price_stock_lst:
        stock_dict[key] = value
        price_stock_lst.remove(value)
        break




#ANALYSIS

#finding dates when interest rate was decreased
increased_rate_date_index = list()
decreased_rate_date_index = list()

support_value_1 = [0]
interest_rates_lst_sliced_compare_intermediate = interest_rates_lst_sliced[1:]
interest_rates_lst_sliced_compare = interest_rates_lst_sliced_compare_intermediate + support_value_1


#list of increasing
for idx in range(1, len(interest_rates_lst_sliced)):
    if interest_rates_lst_sliced[idx - 1] < interest_rates_lst_sliced[idx]:
        increased_rate_date_index.append(True)
    else:
        increased_rate_date_index.append(False)

increase = [i for i, x in enumerate(increased_rate_date_index) if x]


#list of decreasing
for idx in range(1, len(interest_rates_lst_sliced)):
    if interest_rates_lst_sliced[idx - 1] > interest_rates_lst_sliced[idx]:
        decreased_rate_date_index.append(True)
    else:
        decreased_rate_date_index.append(False)

decrease = [i for i, x in enumerate(decreased_rate_date_index) if x]

#conversion of indexes to dates of increase and decreased
#increased
date_increase_interest_rate=list()
for index in increase:
    index = int(index)
    date_ipt = date_lst_sliced[index]

    date_increase_interest_rate.append(date_ipt)



#decreased
date_decrease_interest_rate=list()
for index in decrease:
    index = int(index)
    date_dipt = date_lst_sliced[index]

    date_decrease_interest_rate.append(date_dipt)




#Allocation the stock price to the increase/decrease dates
#increase
increased_stock_price_lst = list()
increased_stock_price_lst_30 = list()
increased_stock_price_lst_90 = list()
increased_stock_price_lst_180 = list()

for date in date_increase_interest_rate:
    date = date

# + 0 days price list (test set to be repeted below)
    try:
        increased_stock_price = stock_dict[date]
    except:
        increased_stock_price = 0

    if increased_stock_price == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            increased_stock_price = stock_dict[date1]
        except:
            increased_stock_price = 0
        if increased_stock_price == 0:
            date_str = date
            dto = datetime.strptime(date_str, '%Y-%m-%d').date()
            dto_1 = dto.replace(day=5)
            date1 = str(dto_1)
            try:
                increased_stock_price = stock_dict[date1]
            except:
                increased_stock_price = 0

    increased_stock_price_lst.append(increased_stock_price)

# + 30 days price list
date_increase_interest_rate_30=list()
for index in increase:
    index = int(index) + 1
    date_ipt_30 = date_lst_sliced[index]

    date_increase_interest_rate_30.append(date_ipt_30)

for date in date_increase_interest_rate_30:
    date = date
    try:
        increased_stock_price_30 = stock_dict[date]
    except:
        increased_stock_price_30 = 0
    if increased_stock_price_30 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            increased_stock_price_30 = stock_dict[date1]
        except:
            increased_stock_price_30 = 0
        if increased_stock_price_30 == 0:
            date_str = date
            dto = datetime.strptime(date_str, '%Y-%m-%d').date()
            dto_1 = dto.replace(day=5)
            date1 = str(dto_1)
            try:
                increased_stock_price_30 = stock_dict[date1]
            except:
                increased_stock_price_30 = 0

    increased_stock_price_lst_30.append(increased_stock_price_30)

# + 90 days price list
date_increase_interest_rate_90=list()
for index in increase:
    index = int(index) + 3
    date_ipt_90 = date_lst_sliced[index]

    date_increase_interest_rate_90.append(date_ipt_90)

for date in date_increase_interest_rate_90:
    date = date
    try:
        increased_stock_price_90 = stock_dict[date]
    except:
        increased_stock_price_90 = 0

    if increased_stock_price_90 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            increased_stock_price_90 = stock_dict[date1]
        except:
            increased_stock_price_90 = 0
            if increased_stock_price_90 == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    increased_stock_price_90 = stock_dict[date1]
                except:
                    increased_stock_price_90 = 0

    increased_stock_price_lst_90.append(increased_stock_price_90)


# + 180 days price list
date_increase_interest_rate_180=list()
for index in increase:
    index = int(index) + 6
    date_ipt_180 = date_lst_sliced[index]

    date_increase_interest_rate_180.append(date_ipt_180)

for date in date_increase_interest_rate_180:
    date = date
    try:
        increased_stock_price_180 = stock_dict[date]
    except:
        increased_stock_price_180 = 0

    if increased_stock_price_180 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            increased_stock_price_180 = stock_dict[date1]
        except:
            increased_stock_price_180 = 0
            if increased_stock_price_180 == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    increased_stock_price_180 = stock_dict[date1]
                except:
                    increased_stock_price_180 = 0

    increased_stock_price_lst_180.append(increased_stock_price_180)



#decrease
decreased_stock_price_lst = list()
decreased_stock_price_lst_30 = list()
decreased_stock_price_lst_90 = list()
decreased_stock_price_lst_180 = list()

for date in date_decrease_interest_rate:
    date = date
# + 0 days price list
    try:
        decreased_stock_price = stock_dict[date]
    except:
        decreased_stock_price = 0

    if decreased_stock_price == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            decreased_stock_price = stock_dict[date1]
        except:
            decreased_stock_price = 0
            if decreased_stock_price == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    decreased_stock_price = stock_dict[date1]
                except:
                    decreased_stock_price = 0

    decreased_stock_price_lst.append(decreased_stock_price)

# + 30 days price list
date_decrease_interest_rate_30=list()
for index in decrease:
    index = int(index) + 1
    date_ipt_30 = date_lst_sliced[index]

    date_decrease_interest_rate_30.append(date_ipt_30)

for date in date_decrease_interest_rate_30:
    date = date
    try:
        decreased_stock_price_30 = stock_dict[date]
    except:
        decreased_stock_price_30 = 0

    if decreased_stock_price_30 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            decreased_stock_price_30 = stock_dict[date1]
        except:
            decreased_stock_price_30 = 0
            if decreased_stock_price_30 == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    decreased_stock_price_30 = stock_dict[date1]
                except:
                    decreased_stock_price_30 = 0

    decreased_stock_price_lst_30.append(decreased_stock_price_30)

# + 90 days price list
date_decrease_interest_rate_90=list()
for index in decrease:
    index = int(index) + 3
    date_ipt_90 = date_lst_sliced[index]

    date_decrease_interest_rate_90.append(date_ipt_90)

for date in date_decrease_interest_rate_90:
    date = date
    try:
        decreased_stock_price_90 = stock_dict[date]
    except:
        decreased_stock_price_90 = 0

    if decreased_stock_price_90 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            decreased_stock_price_90 = stock_dict[date1]
        except:
            decreased_stock_price_90 = 0
            if decreased_stock_price_90 == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    decreased_stock_price_90 = stock_dict[date1]
                except:
                    decreased_stock_price_90 = 0

    decreased_stock_price_lst_90.append(decreased_stock_price_90)


# + 180 days price list
date_decrease_interest_rate_180=list()
for index in decrease:
    index = int(index) + 6
    date_ipt_180 = date_lst_sliced[index]

    date_decrease_interest_rate_180.append(date_ipt_180)

for date in date_decrease_interest_rate_180:
    date = date
    try:
        decreased_stock_price_180 = stock_dict[date]
    except:
        decreased_stock_price_180 = 0

    if decreased_stock_price_180 == 0:
        date_str = date
        dto = datetime.strptime(date_str, '%Y-%m-%d').date()
        dto_1 = dto.replace(day=3)
        date1 = str(dto_1)
        try:
            decreased_stock_price_180 = stock_dict[date1]
        except:
            decreased_stock_price_180 = 0
            if decreased_stock_price_180 == 0:
                date_str = date
                dto = datetime.strptime(date_str, '%Y-%m-%d').date()
                dto_1 = dto.replace(day=5)
                date1 = str(dto_1)
                try:
                    decreased_stock_price_180 = stock_dict[date1]
                except:
                    decreased_stock_price_180 = 0

    decreased_stock_price_lst_180.append(decreased_stock_price_180)

#Change calculation
#increase
index = 0

percentage_change_increase = list()
direction_increase = list ()
summary_list = list()
for number in increased_stock_price_lst:


    t = increased_stock_price_lst_180[index]


    if number < t:
        percentage = (t / number - 1) * 100
        percentage_change_increase.append(percentage)
        direction_increase.append("Ʌ")
        summary_list.append(1)
    if number > t:
        percentage = t / number
        percentage = 100 - (percentage * 100)
        percentage_change_increase.append(percentage)
        direction_increase.append("V")
    if number == t:
        percentage = 0
        percentage_change_increase.append(percentage)
    index = index + 1

#decreased
index = 0

percentage_change_decrease = list()
direction_decrease = list ()
for number in decreased_stock_price_lst:


    t = decreased_stock_price_lst_180[index]


    if number < t:
        percentage = (t / number - 1) * 100
        percentage_change_decrease.append(percentage)
        direction_decrease.append("Ʌ")
    if number > t:
        percentage = t / number
        percentage = 100 - (percentage * 100)
        percentage_change_decrease.append(percentage)
        direction_decrease.append("V")
    if number == t:
        percentage = 0
        percentage_change_decrease.append(percentage)
    index = index + 1



#Building presentation table
#(date_increase_interest_rate)
#(increased_stock_price_lst)
#(increased_stock_price_lst_30)
#(increased_stock_price_lst_90)
#(increased_stock_price_lst_180)

#Increase table



increase_table = pandas.DataFrame(
    {'Month of interest rate increase': date_increase_interest_rate,
     'Price at interest rate increase': increased_stock_price_lst,
     '+ 30 days': increased_stock_price_lst_30,
     '+ 90 days': increased_stock_price_lst_90,
     '+ 180 days': increased_stock_price_lst_180,
     "delta direction": direction_increase,
     "delta in %": percentage_change_increase
    })
#print ("The table below shows impact of increase of interest rates on the stock")



#Decrease table
decrease_table = pandas.DataFrame(
    {'Month of interest rate decrease': date_decrease_interest_rate,
     'Price at interest rate decrease': decreased_stock_price_lst,
     '+ 30 days': decreased_stock_price_lst_30,
     '+ 90 days': decreased_stock_price_lst_90,
     '+ 180 days': decreased_stock_price_lst_180,
     "delta direction": direction_decrease,
     "delta in %": percentage_change_decrease
    })
#print ("The table below shows impact of decrease of interest rates on the stock")



#Summary output
#increase
summary_output_len = len(percentage_change_increase)

summary_list_len = len(summary_list)

percentage_summary = summary_list_len/summary_output_len*100

print ("The stocks were up in", summary_list_len, "cases out of", summary_output_len, "hence in", percentage_summary, "%")

#decrease




