import streamlit as st
import pandas
import pandas_datareader.data as web
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import requests


interest_rates_file = pandas.read_csv("int_rates.csv", index_col=None)
date_lst = interest_rates_file.DATE.to_list()
interest_rate_list = interest_rates_file.INTDSRUSM193N.to_list()

interest_rate_chart_table_new = list()
for date in date_lst:
    date_chart = date[0:4]
    interest_rate_chart_table_new.append(date_chart)


interest_rate_chart_table = pandas.DataFrame(
    {'Interest Rate': interest_rate_list,
     'Date': interest_rate_chart_table_new
    })

df = pandas.DataFrame(
    {'Interest Rate': [1, 3, 4, 3, 2],
     'Date': [2, 3, 1, 4, 3]
    })

st.dataframe(interest_rate_chart_table)
st.line_chart(df)
st.line_chart(interest_rate_chart_table)


