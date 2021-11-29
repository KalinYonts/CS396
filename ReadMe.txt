ReadMe

Name 
This Django website project is in the second phase. At present, the name displayed as the webpage is ‘Kalin Yonts’. When the project is fully-functioning for the intended purpose, the name will be updated accordingly.

Description
The website is locally hosted and is composed of Django, Python, AWS-S3, Bootstrap, HTML/CSS. The author wrote this program using a MacBook Pro and had previously installed the software requirements. 

The website at present has the following functionalities:
1.	An administrator account. This user can delete other users, delete/edit all posts, create new discussion topics through the admin page. The administrator page is password protected and fully functioning using the built-in Django admin function. 
2.	Registration and Login function for users. This is stored in the database used by Django. 
3.	Post features which allows registered users to write new posts, update/delete older posts and view posts written by others. 
4.	File upload/storage. Users can upload a profile picture to their user profile which is displayed on user posts. 
5.	The number of posts and users is stored in the database and can be viewed by administrators. 
6.	Link to Google Calendar in the sidebar. The website is dynamic and the sidebar moves if the user is on mobile or changes the size of the view window. 
7.	Warning messages appear when a user inputs incorrect information or attempts to click something they do not have access to. 
8. 	The following applications stored in the database and displayed for the user:
	Activités (Type, Time, Location, Description)
	Shopping (Item, Quantity, Price, Store, Related Activity)
	Meeting (Meeting name, ID, # of participants, participant name, meeting files)
	Health (Doctor name, email, phone number, medicine, dose, dosage time)


Installation
1.	Begin by opening a terminal window. 
2.	cd to file save location
3.	Create project directory
kalin@raspberrypi:~ $ mkdir website
kalin@raspberrypi:~ $ cd website

4.	Create a virtual environment
kalin@raspberrypi:~/website $ virtualenv newenv
kalin@raspberrypi:~/website $ source newenv/bin/activate
(newenv) kalin@raspberrypi:~/website $ pip install django

5.	Within the virtual environment, start a project
(newenv) kalin@raspberrypi:~/website $ django-admin startproject blog

6.	Enter the website project and create blog 

(newenv) kalin@raspberrypi:~/website $ cd website
(newenv) kalin@raspberrypi:~/website/website $ python manage.py startapp blog

7.	In the Website directory, locate the urls.py file and update to the following:
 
Create urls.py files in the userprofile and forum subdirectories and place the same information in each file. 

8.	(newenv) kalin@raspberrypi:~/website/website $ python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 23, 2021 - 14:36:38
Django version 3.2.7, using settings 'website.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

9.	Test that the server is running successfully.

10.	Quit the server. Locate the forum directory, add a new directory called templates. Enter the templates directory and make a new directory called forum. Here, create the HTML template files that will be visible on the website.

11.	Repeat step 10 inside the userprofile directory. Name the directories templates and userprofile. Create the HTML files.

12.	Once webpages are written and linked, run the python server. Navigate to the IP address of your RPi and test the website functionality.

13. 	For additional functions added in Phase II, update your files or re-download the source code from the GitHub repository. 

**In the event of errors, refer to the GitHub repository to review the code examples for this project. 



Usage
At present, the website is not publicly launched. The website is hosted on localhost on a private WIFI network and anyone who wishes to access the Django project must be on the machine. 

GitHub
Project files have been pushed using Git to serve as a reference for this project and as a save file for future edits.

Authors and Acknowledgements
Kalin Yonts – primary author
Corey Shafer <https://coreyms.com/development/python/python-django-tutorials-full-series>

Project Status
The project is in the second phase and contains the functionalities outlined above. 
