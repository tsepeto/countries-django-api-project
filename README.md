# Countries Report Technical Specifications
# Descriptions
 This projecyt acts as a reporting system of Administrational Division of a Country and provides simple Rest APIs for handling simple information storage and retrieval requests for countries' reports.
 
 # Requirements
 Python + Django Rest Framework:
 Django is an open source web framework that helps you create a web app quickly as it takes care of additional web-development needs. Django Rest Framework's modular, flexible, and customizable architecture makes the development of both simple, turnkey API endpoints and complicated REST constructs possible.
 
 PostgreSQL:
 It is a highly stable database management system, backed by more than 20 years of community development which has contributed to its high levels of resilience, integrity, and correctness. PostgreSQL is used as the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications.
 
 #Requirements and how to run the application
  For your convenience to run the application without errors, there is a docker-compose file that will install every service is needed to run the program.
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
Admin Console Interface is an interface available to users that belong to the admin group. Through this interface one has access to data models entries and modification rights. 
I created an admin user for you.
If you want to access in the admin console connect with your browser to the next link:  http://localhost:8000/admin/

username: admin  
password: admin  
email: admin@admin.com  
 
![Screenshot (25)](https://user-images.githubusercontent.com/30272549/131007502-5befeb31-93da-4497-8c66-91f7077fb8a2.png)

## From APIs end points
  Every model has it's own endpoint that you can get by id, get list with all model's objects, create, partial update, total update and delete
  
### APIs end points
http://localhost:8000/api/countries/
