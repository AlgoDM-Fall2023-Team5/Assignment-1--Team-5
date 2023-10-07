import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from query_functions import *
from sqlalchemy import create_engine,text


snowflake_url = st.secrets["snowflake"]["url"]

# change your subfolder path to the query folder of your system
subfolder_path = "sql queries dynamic"

# variables declaration
query_names_list = ["Query41","Query42","Query43","Query44","Query45"
                    ,"Query46","Query47","Query48","Query49","Query50"]
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
    'Query41':'Query41',
    'Query42':'Query42',
    'Query43':'Query43',
    'Query44':'Query44',
    'Query45':'Query45',
    'Query46':'Query46',
    'Query47':'Query47',
    'Query48':'Query48',
    'Query49':'Query49',
    'Query50':'Query50'
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
        #table = conn.query(query,ttl=600)
        with engine.connect() as conn:
            result = conn.execute(text(query))
            table = result.fetchall()
            column_names = result.keys()  # Get the column names from the query result

    # Convert the query result to a Pandas DataFrame
            table = pd.DataFrame(table, columns=column_names)
        
        return table
    except Exception as e:
        st.error("Error Executing the Query : {}".format(str(e)))
    

#=========================================================================

# Connection Initialisation
#conn = st.experimental_connection('snowflake',type='sql')

engine = create_engine(snowflake_url)

#---=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=--==-=-=-=-
# Main Code Execution

st.title("SNOWFLAKE SQL QUERY TOOL")
select_button = st.radio("Query Type",["Given Queries","Write your Query"],horizontal=True)

#Selection based on the button
if select_button == "Given Queries":
    col3,col4 = st.columns(2)
    with col3:
        option = st.selectbox("Select a Query",query_names_list)
    
    if option in question_to_answer:
        option = question_to_answer[option]
    # call fucntions based on the query selected
    if option in query_options:
        query_function = query_options[option]
        # calls that particular function
        st.write("Attributes")
        query = query_function(option)
    df = query_executor(query)

    # This is for showing table 
    with col4:
        st.write("")
        st.write("")
        table_button = st.checkbox("Show Table",["Show Table"])
    if table_button:
        st.write(df)

    chart_maker(df)


# Custom Query
else:
    
    col5,col6,col7 = st.columns(3)
    with col5:
        url = "https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.1.0.pdf"
        st.write("dataset info and table schema can be found on this [link](%s)" %url)
        query = st.text_input('Enter Your Query',value="Select * from store_sales limit 10")
    
    df = query_executor(query)
    

    st.write("Table Results:")
    st.write(df)
    chart_maker(df)