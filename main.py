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

interest_rate_chart_table = pandas.DataFrame(
    {'Date': date_lst,
     'Interest Rate': interest_rate_list,
    })


st.dataframe(interest_rate_chart_table)
st.line_chart(interest_rate_chart_table)


