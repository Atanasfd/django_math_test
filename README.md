It's a simple django 2.0 project with allauth for user authentication, with MySQL as the database.The docs for allauth http://django-allauth.readthedocs.io/en/latest/overview.html.
The profiles app is made to handle the home page. The home page uses a session so the database may not be clogged with random answers from random visitors.
The wrong view (on the home page) shows the visitor/user his mistakes. 
The math_tests app is made to handle math tests. It is made so each user takes only one row in the database (if a user submits answers to the test again the row will be updated in the database instead of creating a new row).
Same with job_application. The job_to_text_cv.py fetches the job_application data and makes a text cv out of it.
They all use bootstrap 3.3.7. 
