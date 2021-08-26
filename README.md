# Countries Report Technical Specifications
# Descriptions
 This projecyt acts as a reporting system of Administrational Division of a Country and provides simple Rest APIs for handling simple information storage and retrieval requests for countries' reports.
 
 # Requirements
 Python + Django Rest Framework:
 Django is an open source web framework that helps you create a web app quickly as it takes care of additional web-development needs. Django Rest Framework's modular, flexible, and customizable architecture makes the development of both simple, turnkey API endpoints and complicated REST constructs possible.
 
 PostgreSQL:
 It is a highly stable database management system, backed by more than 20 years of community development which has contributed to its high levels of resilience, integrity, and correctness. PostgreSQL is used as the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications.
 
 # Requirements and how to run the application
  For your convenience to run the application without errors, there is a docker-compose file that will install every service needed to run the program.
  1. Ensure that docker is installed on your system and is running.
  2. Git clone the project from GitHub repository and navigate to that repository folder with your terminal.
  3. Run in your terminal the command "docker-compose up"    
  -The program will install all the requirements services for you and run the program
  
  # Some more Commands
  1. The project comes with an empty database. If you want to install some dummy data to check the program without losing your time to create them, just write the command <docker-compose run --rm app sh -c "python manage.py fill_with_dummy_data" >
  
  2. If you want to clear your database and be able to use the program for your own data, run the command < docker-compose run --rm app sh -c "python manage.py clear_database" > . BE CAREFULL!!!! All the Countries, Regions and Cities WILL BE DELETED!!!!!!!!!

# Testing
The testing files are located inside the rootapp/tests folder!

![Screenshot (17)](https://user-images.githubusercontent.com/30272549/131003729-df346537-c7fc-40c3-b3b2-1e3503f1ff2e.png)

If you want to run the testing procedure, run the command < docker-compose run --rm app sh -c "python manage.py test" >

![Screenshot (15)](https://user-images.githubusercontent.com/30272549/131003319-e91b8909-6de9-44c6-9e89-e81e9d65f839.png)

# Data Modelling
There are three relational Models, each for one Administrational Division level

1 Country - Level 1

![Screenshot (20)](https://user-images.githubusercontent.com/30272549/131005315-47a0740c-01b7-45ba-a43e-c92c6015d012.png)

2 Region - Level 2

![Screenshot (21)](https://user-images.githubusercontent.com/30272549/131005514-f3b5f7d6-eeb0-4da8-8622-0124374a721b.png)

3 City - Level 3

![Screenshot (22)](https://user-images.githubusercontent.com/30272549/131005656-ee492a22-6853-42b4-8f90-2bddcd7c4197.png)


# Manage your data
## From admin console
Admin Console Interface is an interface available to users that belong in the admin group. Through this interface one has access to data models entries and modification rights. 
I created an admin user for you.
If you want to access in the admin console connect with your browser to the next link:  http://localhost:8000/admin/

username: admin  
password: admin  
email: admin@admin.com  
 
![Screenshot (25)](https://user-images.githubusercontent.com/30272549/131007502-5befeb31-93da-4497-8c66-91f7077fb8a2.png)

## From APIs end points
  Every model has it's own endpoint that you can get by id, get list with all model's objects, create, partial update, total update and delete
  
### APIs end points
Country's API :   http://localhost:8000/api/countries/    
Region's API  :   http://localhost:8000/api/regions/     
City's API    :   http://localhost:8000/api/cities/     

### Ιn detail
Method: GET      path:   http://localhost:8000/api/countries/          returns all the Model's entries    

Method: GET      path:   http://localhost:8000/api/countries/ID        returns the Model's entry that has the given ID     

Method: POST     path:   http://localhost:8000/api/countries/          creates a new Model record, from the given JSON data    

Method: PUT      path:   http://localhost:8000/api/countries/ID        updates totally the Model's record that has the given ID     

Method: PATCH    path:   http://localhost:8000/api/countries/ID        updates partial field from the Model's record that has the given ID     

Method: DELETE   path:   http://localhost:8000/api/countries/ID        deletes the Model's record that has the given ID    

Method: GET      path:   http://localhost:8000/api/countries/?id=ID    returns all the Country's entries(exept the given one), after sorting them by distance in relation to the given id     

Method: Get      path:   http://localhost:8000/api/countries/?name=NAME  returns all the Model's entries which contain in their name the given string (the string must have at list 3 characters lenght)      

You can also combine the query parameters for sorting by name and distance   http://localhost:8000/api/countries/?id=ID&name=NAME     
###### All the above paths are working for all Models
   
### One MORE end point
You can get all models' entries from one end point
Method: GET      path:   http://localhost:8000/api/places/     
You can also filter them by name (the string must have at least 3 characters length)
Method: GET      path:   http://localhost:8000/api/places/?name=NAME

# Distance filter
The program calculates the distance between two latitude-longitude coordinates by using the Haversine Formula.
You can find the DistanceCalculator class inside the rootapp/utils/    
![Screenshot (27)](https://user-images.githubusercontent.com/30272549/131015346-9d5a0924-6ee1-4098-85d4-d5ed11c8ac11.png)

            

# Ιmprovements
We could configure Django settings for multiple enviroments with different '.env' files with the desired settings.py variables. We could read the values of these variables from the configuration file instead of directly declaring them in settings.py. This is very useful in deploying the app in UAT and production, where I need different settings for each server.
Also we could create REST API documentation by using some extra libraries as the Swagger, Redoc etc
