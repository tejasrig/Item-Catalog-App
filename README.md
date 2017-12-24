# Item Catalog App
Application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

# Major features of the application developed : 
* Home page with all the Categories information. Clicking the categories redirects to the page with all Items for that category. 
* Home page provides a Login feature to login using `Google Sign in` with the google credentials. This is implemented using the OAuth functionality explained in the course. 
* The user who logged in succesfully will have access to create Categories and Items. Also, user can edit/delete the items that are created by him/her. 
* JSON endpoints are configured for the app as below.
![json2](https://user-images.githubusercontent.com/28773669/34325580-4d5e0f56-e84a-11e7-8b4c-e159f9372cd8.jpg)
![json3](https://user-images.githubusercontent.com/28773669/34325581-4db4d61a-e84a-11e7-8c5c-02b64defc3e7.jpg)
![json1](https://user-images.githubusercontent.com/28773669/34325582-4dcb29ec-e84a-11e7-90db-6ac6801fbedd.jpg)


# Files
This Project consists of three files that you will see in the repository. 
### database_setup.py : 
_This is the file that has the database setup for building this app. It creates the database, necessary tables (Category, CategoryItem, User)_
### database_setup.pyc :
_This is the product file created after executing the `database_setup.py` file._
### lotsofitems.py : 
_This file holds the test data(categories and items) for the tables created using the `database_setup` file. It has to be executed before running `application.py` file for loading the tables._
### itemcatalog.db : 
_This is the database file created upon executing the `database_setup.py` and this file is also loaded with data after executing the `lotsofitems.py` file._
### application.py: 
_This is the main python file that holds the entire logic for the app._
### client_secrets.json:
_This is the file that holds the token value for OAuth.Obtained by configuring through Google API_
### static: 
_This folder holds the style sheets and other images needed for the application. Currently this holds the `styles.css` file responsible for all the styles of the App. Also some images embedded in the App_
### templates: 
_This folder contains all the templates necessary for every screen of the App. Templates are referred in the `application.py` file depending on the URL that it is routed to_


# Instructions to Operate Code
* Install the VM setup from this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
* Install Vagrant from [here](https://www.vagrantup.com/downloads.html)
* Use Github to fork and clone this [Repo](https://github.com/udacity/fullstack-nanodegree-vm) for VM configuration
* Start Virtual Machine with these commands 'vagrant.up' and 'vagrant.ssh'
* Check this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) if any queries/issues while doing the setup. 
* After the setup is done, Run the below python files in the terminal. 
  * `python database_setup.py` 
  * `python lotsofitems.py`
  * `python application.py`
* When the `application.py` starts running, connect to http://localhost:5000/ to access the application. From there on, you can navigate to various pages. 
