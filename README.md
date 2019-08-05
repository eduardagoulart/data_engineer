# How to execute API

### Run filtering query

http://127.0.0.1:8000/purshcase/?my_query=12

##### Avaliable querys 
  - months, 
  - state_abbr,
  - agency_id
  - stat_profile_date_year,
  
### Export CSV with Agency id and Prod line
http://127.0.0.1:8000/report/?data=year

This will be generate an report with agency id and Product line from the 
year used in parameter. 

  