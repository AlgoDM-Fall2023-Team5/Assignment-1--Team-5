import streamlit as st
import snowflake.connector

def chart_maker():
    st.area_chart()

# Connection Initialisation
conn = st.experimental_connection('snowflake',type='sql')

st.title("SNOWFLAKE SQL QUERY TOOL")

select_button = st.radio("Query Type",["Given Queries","Write your Query"],horizontal=True)

#Selection based on the button

if select_button == "Given Queries":
    option = st.selectbox("Select a Query",["Query41","Query42","Query43","Query44","Query45"])
    st.write("you selected {}".format(option))
    chart_maker()
else:
    query = st.text_input('Enter Your Query')
    chart_maker()