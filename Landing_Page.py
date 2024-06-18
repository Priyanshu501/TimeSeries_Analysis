import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the stock dataset
stock_data = pd.read_csv("./data/AAPL.csv")

st.set_page_config(
    page_title='Landing Page'
)

st.sidebar.success('test')

# Create a function for each page

# def data_summary_page():
#     st.title("Data Summary")
#     st.write("This page provides a summary of the stock dataset.")
#     st.write(stock_data.describe())

# def visualizations_page():
#     st.title("Visualizations")
#     st.write("This page provides visualizations of the stock dataset.")
#     fig, ax = plt.subplots()
#     sns.lineplot(x=stock_data.index, y=stock_data["Close"])
#     st.pyplot(fig)

# def correlation_analysis_page():
#     st.title("Correlation Analysis")
#     st.write("This page provides a correlation analysis of the stock dataset.")
#     corr_matrix = stock_data.corr()
#     st.write(corr_matrix)


# Create a dictionary to store the pages of the app
# pages = {
#     "EDA": EDA,
    # "Data Summary": data_summary_page,
    # "Visualizations": visualizations_page,
    # "Correlation Analysis": correlation_analysis_page
# }

# # Add buttons to navigate between pages
# st.sidebar.title("Navigation")
# selected_page = None
# for page_name in pages.keys():
#     if st.sidebar.button(page_name):
#         selected_page = page_name

# # Run the selected page function
# if selected_page:
#     pages[selected_page]()
# else:
#     st.sidebar.write("Select a page to display its content.")