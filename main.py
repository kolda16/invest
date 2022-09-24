import streamlit as st


interest_rates_file = pandas.read_csv("/Users/Matej/Desktop/Stock/int_rates.csv", index_col=None)
date_lst = interest_rates_file.DATE.to_list()
interest_rate_list = interest_rates_file.INTDSRUSM193N.to_list()

interest_rate_chart_table = pandas.DataFrame(
    {'Date': date_lst,
     'Interest Rate': interest_rate_list,
    })



st.line_chart(interest_rate_chart_table)


