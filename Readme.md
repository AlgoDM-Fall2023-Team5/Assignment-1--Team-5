# Link to CodeLab: 
[Assignment-1--Team-5 Report🔗](https://codelabs-preview.appspot.com/?file_id=1weK3M722C8g5DGMYXoKv_qOPIN3k-KORHFZ3oPvp8n0#0)

# Link to Snowflake Dashboard:
[Click Here🔗](https://app.snowflake.com/us-east-1/ikb40337/#/asssignment_1-dEJoIhYGa)


# Code Documentation for Streamlit App:
[Streamlit Code (Github)🔗](https://github.com/AlgoDM-Fall2023-Team5/Assignment-1--Team-5/tree/Main/streamlit)


## Setting up Virtual Environment:
### Requirements:
To run this project, you need to follow these steps:

 

1. **Snowflake Account**:
   - Sign up for a Snowflake account if you don't have one. You can use the trial version.
   - Get your Snowflake account credentials (account URL, username, password).

 

2. **Anaconda Environment (Recommended)**:
   - It is recommended to use Anaconda for managing the project environment.
   - Create a new Anaconda environment using the following command:

 

     ```bash
     conda create --name <environment name> python=3.8
     ```

 

   - Activate the environment:

 

     ```bash
     conda activate <environment name> 
     ```

 

3. **Install Required Packages**:
   - In the activated environment, navigate to the project directory.
   - Install the required packages using pip from the `requirements.txt` file:

 

     ```bash
     pip install -r requirements.txt
     ```

 

4. **Configure Snowflake Credentials**:
   - Store your Snowflake SQLAlchemy URL securely in a `.secrets` file within the `.streamlit` directory on your local machine.
   - The URL structure should look like this:

 

     ```ini
     [snowflake]
     url = snowflake://<username>:<password>@<account-url>/<database>/<schema>
     ```

 

   - Replace `<username>`, `<password>`, `<account-url>`, `<database>`, and `<schema>` with your Snowflake account details.

 

5. **Run the Application**:
   - Run the Streamlit application using the following command,
   Make sure you are in the strteamlit folder:

 

     ```bash
     streamlit run stremlit_dash.py
     ```

 

   - Access the application in your web browser at the specified URL (usually http://localhost:8501).




## Using the App
🚀 Welcome to the Retail Analytics Dashboard

This interactive tool allows you to run SQL queries on a Snowflake database and visualize the results using various chart types. Let's explore how to use it step by step.

### 👉 Getting Started

Choose how you want to proceed:

Select a predefined query from the "Given Queries" section.

Write your custom SQL query in the "Write your Query" section.

### 👉 Selecting a Predefined Query

In the "Given Queries" section:

Use the dropdown menu to select a query from the list.

Once you select a query, you'll see the results in a table, and you can choose to display a chart by selecting a chart type.

### 👉 Writing a Custom Query

In the "Write your Query" section:

Enter your custom SQL query in the text input box.

After entering your query, you'll see the query results in a table, and you can choose to display a chart using various chart types.

📈 Chart Types

(You can visualize your data using different chart types:)

📊 Bar Chart: Compare data with bars.

🥧 Pie Chart: Display data as a pie chart.

📉 Scatter Plot: Visualize data points.

📈 Line Chart: Show data trends over time.


### Additional Information

📚 Dataset Information and Table Schema: You can find dataset information and table schema [here](http://tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v3.2.0.pdf).

⚠️ Note: Certain columns may not be suitable for plotting due to the absence of a sufficient amount of data, leading to potential issues with data visualization or graphical representation

👩‍💻 Developed by Team-5
🤝Contributions: [Click here🔗](https://github.com/AlgoDM-Fall2023-Team5/Assignment-1--Team-5/blob/Main/requirements.txt) 