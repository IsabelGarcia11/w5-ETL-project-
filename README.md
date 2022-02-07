# New York - Bike Sharing

<img src = "fotos/sky.jpg" width="800" height="200">

**TARGET**

The objective of the project is to relate data obtained from different sources in order to highlight certain conclusions 
after analysis.  

It is divided into two Jupyter Notebooks:
* *ETL_Cleaning*: Has been used to unify all analyze all the data.

* *pd_SQL*: Collects the process in which we export the different DataFrames to SQL and create a relationship between all of them.

### ETL_Cleaning
<img src = "FOTOS/bici2.jpg" width="800" height="200">

First, we downloaded a dataset from [Kaggle.](https://www.kaggle.com/ongks1986 new-york-city-bike-sharing-2019) consisting of 12 CSVs containing bike sharing data in New York City during 2019.
Subsequently, to complement this information, we have  performed Web Scraping from two different sources.
On the one hand, with the information from [NYC Open Data.](https://data.cityofnewyork.us/Health/Open-Streets-Locations/uiay-nctu) 
we have created a DataFrame with the opening streets daily 
for pedestrians and cyclists for social distancing during the COVID-19 crisis.

On the other hand, with data from [Wikipedia.](https://en.wikipedia.org/wiki/Boroughs_of_New_York_City), we have created another DataFrame with demographic data of the different neighborhoods of New York.

<img src = "FOTOS/py.jpg" width="50" height="50">

All the functions used in this process are located in the cleaning3 file inside the src folder.

### Data_SQL

With the data already analyzed, we export the different DataFrames to SQL and unify them into a single one in order to obtain the conclusions.

**CONCLUSIONS**

<img src = "fotos/wall.jpg" width="800" height="200">


The idea is to contrast whether those neighborhoods where bike sharing was most used during 2019 were the ones where pedestrianization was most enhanced during the covid 19 crisis.
In addition, with the demographics of the new york neighborhoods we wanted to see if the gdp of each neighborhood influences the use of bike sharing.

Once all the analysis has been carried out, we conclude that there is a relationship, the neighborhoods where more streets have been pedestrianized are directly related to the use of bike sharing. Regarding the gdp highlight that Manhattan, is the area with by far the highest gdp as well as the area with the highest population density and  with the highest use of bike sharing by far.

**LINKS & RESOURCES**
* https://www.kaggle.com/ongks1986/new-york-city-bike-sharing-2019
* https://en.wikipedia.org/wiki/Boroughs_of_New_York_City
* https://numpy.org/doc/1.18/
* https://pandas.pydata.org/
* https://docs.python.org/3/library/functions.html
* https://docs.python-requests.org/en/latest/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://docs.python.org/3/library/json.html
* https://python-visualization.github.io/folium/
* https://selenium-python.readthedocs.io/
* https://docs.python.org/3/library/time.html
