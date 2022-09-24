import streamlit as st


st.markdown("Understand your investments!")

stock_name = st.text_input("Stock ticker")


start_year, end_year = st.select_slider(
    'Select a period!',
    options=[2010, 2011, 2012, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    value=(2010, 2020))


start_year = str(start_year)
end_year = str(end_year)
start_date = start_year+"-01-01"
end_date = end_year+"-12-01"

#stock_name = "AAPL"
#start_date = "2015-01-01"
#end_date = "2020-12-01"
#request the stock ticker, which will be inputted into ir_bu script
#stock_name = input("Input stock ticker:")


#after ir_bu script finishes, the code takes the output into this script
if __name__ == "__main__":
    from ir_bu import increase_table
    st.dataframe(increase_table)
    


