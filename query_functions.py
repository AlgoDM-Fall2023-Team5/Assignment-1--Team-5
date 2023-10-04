import streamlit as st

def query41():
    
    # list of all options
    size_options = ['small','medium','petite','large','extra large','N/A']
    unit_options = ['Ounce','Oz','Bunch','Ton','N/A','Dozen','Box','Pound','Pallet','Gross','Cup','Dram','Each','Tbl','Lb','Bundle']
    color_options = ['powder','khaki','brown','honeydew','floral','deep','light','cornflower','midnight','snow','cyan','papaya','orange','frosted','forest','ghost']
    
    # arranging all buttons in one single column
    col1,col2,col3 = st.columns(3)
    with col1:
        size_multiselect = st.multiselect("Size",size_options,default=size_options,placeholder="Choose a size")
    with col2:
        unit_multiselect = st.multiselect("Unit",unit_options,default=unit_options,placeholder="Choose Unit")
    with col3:
        color_multiselect = st.multiselect("Color",color_options,default=color_options,placeholder="Choose Color")
    #st.write("Running the query with dynamic value")
    return size_multiselect,unit_multiselect,color_multiselect

def query42():
    col1,col2 = st.columns(2)
    
    with col1:
        month_slider = st.slider("Month",min_value=1,max_value=12,value=11)
    with col2:
        year_slider = st.slider("Year",min_value=1900,max_value=2049,value=2000)

    return month_slider,year_slider

def query43():
    gmt_options = [-5,-6,-7,-8,'N/A']
    col1,col2 = st.columns(2)

    with col1:
        year_slider = st.slider("Year",min_value=1900,max_value=2049,value=2000)
    with col2:
        gmt_select = st.multiselect("GMT",options =gmt_options,default=-5,placeholder="GMT")
    
    return year_slider,gmt_select
def query44():
    #store_slider = st.slider("Store_Number",min_value=1,max_value=1400,value=4)
    
    store_input = st.text_input("Enter Store Number (1-1400 only): ",value=4)

    if int(store_input)>=1 and int(store_input) <=1400:
        pass
    else:
        st.error("enter between 1-1400")

    return store_input

def query45():
    pass

def query46():
    pass

def query47():
    pass

def query48():
    pass

def query49():
    pass

def query50():
    pass