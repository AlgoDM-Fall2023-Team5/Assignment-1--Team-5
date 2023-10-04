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
        unit_multiselect = st.multiselect("Color",color_options,default=color_options,placeholder="Choose Color")
    #st.write("Running the query with dynamic value")

def query42():
    pass

def query43():
    pass

def query44():
    pass

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