import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# change your subfolder path to the query folder of your system
subfolder_path = "C:/Users/shiri/Documents/Assg1ADM/Assignment-1--Team-5/sql queries"

# variables declaration
query_names_list = ["Query41","Query42","Query43","Query44","Query45"]
chart_types = ["Bar Chart","Pie Chart","Scatter Plot","Line Chart"]

# bar chart 
def bar_chart_maker(df):
    col1,col2 = st.columns([1,1])
    with col1:
        x_axis = st.selectbox("Select X_axis: ",df.columns)
    with col2:
        y_axis = st.selectbox("Slect Y axis :",df.columns)

#=======================================================================
#pie chart maker
def pie_chart_maker(df):
    pass
#========================================================================
# scatter plot maker
def scatter_plot_maker(df):
    pass
#=========================================================================
# line chart
def line_chart_maker(df):
    pass
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
        st.write("Please select the type of chart")
#========================================================================
def sql_query_reader(option):
    option = option.lower()
    with open(subfolder_path+'/'+option+".sql",'r') as file:
        query = file.read()
    return query
#=========================================================================
def query_executor(option):
    try:
        #get the query from another folder
        query = sql_query_reader(option)
        # executing the sql query based on the selection
        table = conn.query(query,ttl=600)
        table_button = st.checkbox("Table",["Show Table"])
        if table_button:
            st.write(table)
        return table
    except Exception as e:
        st.error("Error Executing the Query : {}".format(str(e)))
    

#=========================================================================
# smaple code
#df = pd.DataFrame()


#==========================================================================
# Connection Initialisation
conn = st.experimental_connection('snowflake',type='sql')

st.title("SNOWFLAKE SQL QUERY TOOL")

select_button = st.radio("Query Type",["Given Queries","Write your Query"],horizontal=True)


#Selection based on the button

if select_button == "Given Queries":
    option = st.selectbox("Select a Query",query_names_list)
    df = query_executor(option)

    chart_maker(df)
else:
    query = st.text_input('Enter Your Query')
    #chart_maker(df)