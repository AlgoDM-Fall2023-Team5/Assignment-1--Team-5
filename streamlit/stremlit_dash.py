import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from query_functions import *

# change your subfolder path to the query folder of your system
subfolder_path = "sql queries dynamic"

# variables declaration
query_names_list = [ 'Quantity of items for specific size, units, and color',
    'Extended sales price of each category for specific month and year',
    'Store sales for each day of the week throughout the specific year and time zone',
    'Best and Worst performing products for specific store',
    'Web Sales in Various States for specific Quarter and year',
    'Weekend Shopping Trends of Out-of-Town Customers for specific city, year, vehicle count and dependent count',
    'Three-Year Cumulative Sales with Monthly Deviations > 10 percentage from Average Monthly Sales for specific years',
    'Sales by Marital Status, Education, and State',
    'Return Ratios by channel for specific month and year',
    'Product Returns Over Time After Purchase  for specific month and year']
chart_types = ["Bar Chart","Pie Chart","Scatter Plot","Line Chart"]

# dictonary instead of if else to call functions
query_options = {'Query41':query41,
                 'Query42':query42,
                 'Query43':query43,
                 'Query44':query44,
                 'Query45':query45,
                 'Query46':query46,
                 'Query47':query47,
                 'Query48':query48,
                 'Query49':query49,
                 'Query50':query50}

#dictonary based on selection
question_to_answer = {
    'Quantity of items for specific size, units, and color':'Query41',
    'Extended sales price of each category for specific month and year':'Query42',
    'Store sales for each day of the week throughout the specific year and time zone':'Query43',
    'Best and Worst performing products for specific store':'Query44',
    'Web Sales in Various States for specific Quarter and year':'Query45',
    'Weekend Shopping Trends of Out-of-Town Customers for specific city, year, vehicle count and dependent count':'Query46',
    'Three-Year Cumulative Sales with Monthly Deviations > 10 percentage from Average Monthly Sales for specific years':'Query47',
    'Sales by Marital Status, Education, and State':'Query48',
    'Return Ratios by channel for specific month and year':'Query49',
    'Product Returns Over Time After Purchase  for specific month and year':'Query50'
}



# bar chart 
def bar_chart_maker(df):
    col1,col2 = st.columns([1,1])
    try:
        with col1:
            x_axis = st.selectbox("Select X_axis: ",df.columns)
        with col2:
            y_axis = st.selectbox("Select Y axis :",df.columns)
        
        fig = px.bar(df, x=x_axis, y=y_axis, title=f'Bar Chart: {x_axis} vs {y_axis}')
        st.plotly_chart(fig)
    except Exception as e:
        st.error("Please Check your Bar chart",e)

#=======================================================================
#pie chart maker
def pie_chart_maker(df):
    try:
        column = st.selectbox("Select a Column :",df.columns)
        
        fig = px.pie(df, names=column, values=column, title=f'Pie Chart: {column}')
        st.plotly_chart(fig)
    except Exception as e:
        st.error("please check you pie chart",e)
#========================================================================
# scatter plot maker
def scatter_plot_maker(df):
    col1,col2 = st.columns([1,1])
    try:
        with col1:
            x_axis = st.selectbox("Select X_axis: ",df.columns)
        with col2:
            y_axis = st.selectbox("Select Y axis :",df.columns)
        
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot: {x_axis} vs {y_axis}')
        st.plotly_chart(fig)
    except Exception as e:
        st.error("Please Check your Scatter Plot",e)
#=========================================================================
# line chart
def line_chart_maker(df):
    col1,col2 = st.columns([1,1])
    try:
        with col1:
            x_axis = st.selectbox("Select X_axis: ",df.columns)
        with col2:
            y_axis = st.selectbox("Select Y axis :",df.columns)
        
        fig = px.line(df, x=x_axis, y=y_axis, title=f'Line Chart: {x_axis} vs {y_axis}')
        st.plotly_chart(fig)
    except Exception as e:
        st.error("Please Check your Line chart",e)
#=========================================================================
def chart_maker(df):
    chart_selection = st.selectbox("Select Chart Type",chart_types)

    # chart display based on the selection
    if chart_selection == "Bar Chart" and len(df) > 0:
        bar_chart_maker(df)
    elif chart_selection == "Pie Chart" and len(df) > 0:
        pie_chart_maker(df)
    elif chart_selection == "Scatter Plot" and len(df) > 0:
        scatter_plot_maker(df)
    elif chart_selection == "Line Chart" and len(df)>0:
        line_chart_maker(df)
    else:
        st.write("Empty Table Returned")
#========================================================================
# this is used to read the query
# def sql_query_reader(option):
#     option = option.lower()
#     with open(subfolder_path+'/'+option+".sql",'r') as file:
#         query = file.read()
#     return query
#=========================================================================
# this is used to execute the query
@st.cache_data
def query_executor(query):
    try:
        #get the query from another folder
        #query = sql_query_reader(option)
        # executing the sql query based on the selection
        table = conn.query(query,ttl=600)
        
        return table
    except Exception as e:
        st.error("Error Executing the Query : {}".format(str(e)))
    

#=========================================================================

# Connection Initialisation
conn = st.experimental_connection('snowflake',type='sql')
#---=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=--==-=-=-=-
# Main Code Execution

st.title("Retail Analytics Dashboard: Insights on Sales🤑, Returns, and Trends🚀")
select_button = st.radio("Mode Selection",["Simple Search 🔎 ","Custom Search 🛠️ "],horizontal=True)

#Selection based on the button
if select_button == "Simple Search 🔎 ":
    col3,col4 = st.columns(2)
    with col3:
    
        option = st.selectbox("Pick a pre-defined action",query_names_list)
    
    if option in question_to_answer:
        option = question_to_answer[option]
    # call fucntions based on the query selected
    if option in query_options:
        query_function = query_options[option]
        # calls that particular function
        st.write("Attributes")
        with st.spinner("⏳ Running... ⏳"):
            query = query_function(option)
    with st.spinner("⏳ Running... ⏳"):
        df = query_executor(query)
    st.success("✅ Done!")
    # This is for showing table 
    with col4:
        st.write("")
        st.write("")
        table_button = st.checkbox("Show Table",["Show Table"])
    if table_button:
        st.write(df)

    chart_maker(df)

    if st.button("Help"):        
        url = "https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.1.0.pdf"
        st.write("dataset info and table schema can be found on this [link](%s)" %url)   
        st.balloons()
        

# Custom Query
else:
    
    col5,col6,col7 = st.columns(3)
    with col5:
        url = "https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.1.0.pdf"
        st.write("dataset info and table schema can be found on this [link](%s)" %url)
        query = st.text_input('Enter Your Query',value="Select * from store_sales limit 10")
    
    with st.spinner("⏳ Running... ⏳"):
        df = query_executor(query)
    st.success("✅ Done!")
    

    st.write("Table Results:")
    st.write(df)
    chart_maker(df)