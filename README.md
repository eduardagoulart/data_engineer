# The API
This API was designed with the goal of allowing users to easily search and extract information 
from the Fake Insurance company dataset: this dataset was taken from Kaggle. 
The API was implemented in Python3 and uses the following frameworks/libraries: 
  
  - Pandas
  - Django-Rest
  - Djnago-Rest-Pandas
  
  
To install all dependencies, one should download this repository and run:

 
pip install -r requirements.txt

## How to use the API

The initial page has some basic URLs that provide the user information regarding insurances. 
It is possible to obtain different summarized views that group all insurance information 
according to a given <em>month</em>, <em>year</em>, <em>agency id</em>, or <em>state</em>.

```
<strong>Implementation:</strong> This part of the API performs a simple query on all database.
As a result, four tables are generated. These tables are populated by running python3 csv_to_dabase.py. 
The first table contains information about the Company. 
The other tables group information in terms of 
<em>month</em>, <em>year</em>, <em>agency id</em>, or <em>state</em>.
```

![API initial screen](api_first.png)
### Searching for Specific Value

For instance, 
retrieving insurance information related to month 4 
entails running the following 
<em>'search/?months=4'</em>. 
In a similar way, 
it is also possible to run queries involving the fields below: 

###### Avaliable queries 
    - months, 
    - state_abbr,
    - agency_id
    - year

```
<strong>Implementation:</strong> To implement this method I take the 
request string (in the URL), 
and filter all database info so that 
the query returns all information that matches the request string/query. 
```
### Export report to a CSV file
Oten, a Company needs an important report concerning its situation within any given year. 
So, for every (valid) year, it is possible to obtain a report containing
<em>agency id</em>, <em>loss</em>, <em>earn</em>, and the <em>prod line</em>.

To generate said report, simply ust use <em>/report/data=2009</em>: 
in this case, for instance, 
a report containing everything that took place in 2009 will be downloaded as a CSV file.
(Naturally, it is possible to obtain a reporta concerning any valid year.  In case there is no such a year, an empty CSV will be generated).
http://127.0.0.1:8000/report/?data=year  

```
<strong>Implementation:</strong> This part was implemented using Django 
Rest and the Pandas framework. 
I filter a queryset using the specified value from url. After this, all 
unused fields are dropped from the resulting dataframe. 
Lastly, 
the resulting dataframe is turned into a CSV file (i.e., exported as a CSV file). 
<em>It is worth mentioning that, for some reason, this part of the API currently 
only runs properly in local host</em>
```

The application is available at: http://britecoreproject.xnm6eb7mad.us-west-2.elasticbeanstalk.com/
