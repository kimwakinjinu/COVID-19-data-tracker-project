# COVID-19-data-tracker-project

COVID-19 Data Analysis Project
Project Description
This project involves loading, cleaning, exploring, and visualizing COVID-19 data from the owid-covid-data.csv dataset. The analysis focuses on key metrics like total cases, total deaths, daily new cases, and vaccination progress for selected countries, as well as a global overview using choropleth maps.

Objectives
The primary objectives of this project were to:Load and understand the structure of a real-world dataset (owid-covid-data.csv).Clean and preprocess the data to handle missing values and ensure correct data types.Perform exploratory data analysis (EDA) to identify trends and patterns in COVID-19 cases and deaths.Visualize vaccination progress over time.Optionally, create a global visualization using a choropleth map.Summarize key findings and insights from the analysis.

Tools and Libraries Used
Python: The primary programming language used for the analysis.
pandas: Used for data loading, cleaning, manipulation, and analysis.
matplotlib: Used for creating static visualizations (line plots).
seaborn: Built on matplotlib, used for creating aesthetically pleasing statistical graphics (line plots).
plotly: Used for creating interactive visualizations, specifically the choropleth maps.

How to Run/View the Project
Save the Data: Ensure the owid-covid-data.csv file is in the same directory as your project files.
Install Libraries: Make sure you have Python and the required libraries installed. You can install them using pip:pip install pandas matplotlib seaborn plotly notebook
Open in Jupyter Notebook: The analysis is best viewed and run in a Jupyter Notebook.Save the Python code and markdown text from the project steps into a .ipynb file in a Jupyter Notebook environment.Alternatively, save the Python code into a .py file and run it, though the visualizations and narrative are best experienced in a notebook.Launch Jupyter Notebook from your terminal in the project directory:jupyter notebook
Open the .ipynb file in your browser.Run Cells: Execute the code cells sequentially in the notebook to perform the analysis and generate the visualizations.

Insights and Reflections
Based on the analysis:
Case Trends: The line plots clearly show the cumulative growth of total cases and the fluctuating patterns of daily new cases, highlighting different phases of the pandemic in Kenya, the United States, and India.
Death Rates: The calculated death rate provides a perspective on the fatality of reported cases, although it's important to consider factors like testing and reporting differences between countries when interpreting this metric.
Vaccination Progress: The vaccination charts illustrate the varying speeds and levels of vaccination coverage achieved in the selected countries over time.
This project demonstrates fundamental data science steps, from raw data to insightful visualizations, providing a basic understanding of the COVID-19 pandemic's progression based on this dataset.