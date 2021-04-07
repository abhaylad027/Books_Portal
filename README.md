## Books_Portal
Application Name: Books Portal


## Description of what the project is for

Portal has one file with the name books.csv. 

The CSV file contains the general information about the books, like book name, author, year of publication, etc. 

In portal has two API endpoints are available, as below

**1.	This API will return number of rows requested from the books.csv file.**

**URL: http://127.0.0.1:12xx/get_books/<rows>** 

(Here for <rows> integer value should pass as number of rows and as input)

Example: http://127.0.0.1:5067/get_books/3

Such as no_of_rows = 3 input value

(Here rows value is passing with URL)

**2.	This API can filter and give any rows as per user requirement from the books.csv file.**

**URL: http://127.0.0.1:12xx/filter_rows** 

Example: http://127.0.0.1:5067/filter_rows

Input:  JSON 

Example: {"authors":"Jesse Grant"}

(Here JSON input data passing to backend)

**At the time of using POSTAMN to check rest calls this input have to send in body by selecting

Raw and JSON format 


## Files in Codebase :

**Portal.py**

Contains main code base of application

**unit_tests.py**

Contains unit test cases for main code base

**local_setting.py**

Contains configurable variables required in main code base.

This file is used to change configurable variable values without touching main code base.

**requirements.txt**

Contains list of external libraries used.


## To Run Application:
From main code base location have to run command as below:

**python Portal.py**

(Before running code have to install list libraries from requirements.txt and

Have to configure variables in local_setting.py)
