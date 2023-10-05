import streamlit as st



# change your subfolder path to the query folder of your system
subfolder_path = "C:/Users/shiri/Documents/Assg1ADM/Assignment-1--Team-5/sql queries dynamic"

# this is used to read the query
def sql_query_reader(option):
    option = option.lower()
    with open(subfolder_path+'/'+option+".sql",'r') as file:
        query = file.read()
    return query

#=======================================================
def query41(option):
    
    query = sql_query_reader(option)
    
    # list of all options
    size_options = ['small','medium','petite','large','extra large','N/A']
    unit_options = ['Ounce','Oz','Bunch','Ton','N/A','Dozen','Box','Pound','Pallet','Gross','Cup','Dram','Each','Tbl','Lb','Bundle']
    color_options = ['powder','khaki','brown','honeydew','floral','deep','light','cornflower','midnight','snow','cyan','papaya','orange','frosted','forest','ghost']
    
    size_multiselect = []
    unit_multiselect = []
    color_multiselect =[]

    # arranging all buttons in one single column


    col1,col2,col3 = st.columns(3)
    with col1:
        size_multiselect = st.multiselect("Size",size_options,default=size_options,placeholder="Choose a size" )
    with col2:
        unit_multiselect = st.multiselect("Unit",unit_options,default=unit_options,placeholder="Choose Unit")
    with col3:
        color_multiselect = st.multiselect("Color",color_options,default=color_options,placeholder="Choose Color")
    
    # need to check here again ==>
    count = 0
    while not size_multiselect or not unit_multiselect or not color_multiselect:
        if count == 0:
            if len(size_multiselect) == 0 or len(unit_multiselect) == 0 or len(color_multiselect) == 0:
                st.warning("Please select at least one option for each category.")
        count = count +1    
    
    # if length is one then convert into string

    size_multiselect = size_multiselect[0] if len(size_multiselect) == 1 else size_multiselect
    unit_multiselect = unit_multiselect[0] if len(unit_multiselect) == 1 else unit_multiselect
    color_multiselect = color_multiselect[0] if len(color_multiselect) == 1 else color_multiselect
    
    exe_query = query.format(size_multiselect, unit_multiselect, color_multiselect)

    exe_query = query.format(tuple(size_multiselect),tuple(unit_multiselect),tuple(color_multiselect))
    
    return exe_query
#======================================================
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
    col1,col2 = st.columns(2)

    with col1:
        qoy_slider = st.slider("QOY",min_value=1,max_value=4,value=2)
    with col2:
        year_slider = st.slider("Year",min_value=1900,max_value=2049,value=2001)

    return qoy_slider,year_slider

def query46():
    col1,col2,col3,col4 = st.columns(4)
    city_options = ["Pleasant Hill", "Corinth", "Oakdale", "Mount Vernon", "Mount Carmel",
    "Jackson", "Maple Grove", "Dover", "Rosedale", "Brownsville", "Needmore",
    "Harmony", "Georgetown", "Bethel", "Milltown", "Green Acres", "Riverview",
    "Webster", "Highland", "Hebron", "Bethlehem", "Oakland", "Smyrna",
    "Arlington", "Centerville", "Oxford", "Sulphur Springs", "Beulah", "Vernon",
    "Marion", "Newport", "Chester", "Harrisburg", "Oak Hill", "Wildwood",
    "Monroe", "Cedar Grove", "Greenfield", "Manchester", "Fairview", "Waterloo",
    "Franklin", "Plainview", "Red Hill", "Pleasant Grove", "Clayton", "Shiloh",
    "Macedonia", "Woodland", "Four Corners", "Mount Olive", "Jacksonville",
    "Hollywood", "Wilson", "Spring Valley", "Salem", "Newtown", "Woodville",
    "Hopewell", "Stringtown", "Hillcrest", "Lakeside", "White Oak", "Washington",
    "Highland Park", "Springfield", "Pine Grove", "Spring Hill", "Rockville",
    "Glendale", "Walnut Grove", "Oakwood", "Oak Grove", "Mill Creek", "Woodlawn",
    "Grandview", "Pleasant Valley", "Bellevue", "Lincoln", "Belmont", "Riverside",
    "Dayton", "Mount Zion", "Midway", "Lakeview", "Winchester", "Concord",
    "Springdale", "Bunker Hill", "Rose Hill", "Crossroads", "Dixie", "Enterprise",
    "Oak Ridge", "Valley View", "Florence", "Watson", "Kingston", "Anderson",
    "Avondale", "Hilltop", "Melrose", "Hillsdale", "Pleasant View", "Buena Vista",
    "Farmington", "Union Hill", "Greenville", "Friendship", "Troy", "Ashland",
    "Jefferson", "Summit", "Smithville", "Clinton", "Lakewood", "Eureka",
    "Jamestown", "Edgewood", "Deerfield", "Cloverdale", "Union", "Glenwood",
    "Mountain View", "Independence", "Hamilton", "Cross Roads", "Pine Hill",
    "Greenwood", "Sharon", "Shady Grove", "Eden", "Prospect", "Unionville",
    "Fairfield", "Five Points", "Bridgeport", "Magnolia", "Forest Hills",
    "Williamsburg", "Liberty", "Sherwood Forest", "Petersburg", "Middletown",
    "Lebanon", "Five Forks", "Jericho", "Buffalo", "Waverly", "Antioch",
    "Riverdale", "Westwood", "Mount Pleasant", "Milton", "New Hope", "Sunnyside",
    "Pleasant Ridge", "Richland", "Ebenezer", "Forest Park", "Providence", "Norwood",
    "Columbia", "Clifton"]
    with col1:
        city_multiselect = st.multiselect("Cities",options=city_options,default=["Fairview","Midway"])
    with col2:
        vehicle_count_select = st.slider("Vehicle Count",min_value=-1,max_value=4,value=3)
    with col3:
        year_select = st.slider("Year",min_value=1900,max_value=2049,value=(1999,1999+2))
    with col4:
        dept_slider = st.slider("DEPT Count",min_value=0,max_value=9,value=4)     
    return city_multiselect,vehicle_count_select,year_select,dept_slider

def query47():
    year_select = st.slider("Year",min_value=1900,max_value=2049,value=1999)
    return year_select

def query48():
    col1,col2,col3,col4 = st.columns(4)

    MS_options = ['M','S','D','W','U']
    ES_options = ["Primary", "Secondary", "College", "2 yr Degree",
    "4 yr Degree", "Advanced Degree", "Unknown"]
    state_options = ["CO", "AR", "TX", "FL", "WA", "NM", "MA", "CT", "ME", "SC", "VT", "MI",
    "KS", "MO", "NE", "OK", "NC", "AL", "WY", "MT", "LA", "AZ", "HI", "VA",
    "NJ", "WI", "SD", "ID", "GA", "KY", "IN", "MN", "NH", "TN", "WV", "NY",
    "IA", "DC", "RI", "IL", "OH", "MD", "CA", "ND", "DE", "AK", "NV", "UT", "OR", "MS", "PA"]
    with col1:
        MS_multiselect = st.multiselect(label="Marital Status",options=MS_options,default=['M','D','S'])
    with col2:
        ES_multiselect = st.multiselect(label="Education Status",options=ES_options,default=['4 yr Degree','2 yr Degree','College'])
    with col3:
        State_multiselect = st.multiselect(label="State",options=state_options,deafult=['CO','OH','TX','OR','MN','KY','VA','CA','MS'])
    with col4:
        year_select = st.slider("Year",min_value=1900,max_value=2049,value=2000)


    return MS_multiselect,ES_multiselect,State_multiselect,year_select

def query49():
    pass

def query50():
    col1,col2 = st.columns(2)
    
    with col1:
        month_slider = st.slider("Month",min_value=1,max_value=12,value=8)
    with col2:
        year_slider = st.slider("Year",min_value=1900,max_value=2049,value=2001)

    return month_slider,year_slider