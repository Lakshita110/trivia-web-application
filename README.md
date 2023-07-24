## About The Project
This is a Flask web application built using the [Open TriviaDB API](https://opentdb.com/api_config.php) that allows users to log in and play a trivia game and track their progress.

### Built With
* Flask
* Python
* SQLAlchemy
* Open TriviaDB API

## Contact
Lakshita Jain - [Linkedin](https://www.linkedin.com/in/lakshita-jain-072b4a19b/) - lak.jai110@gmail.com

Project Link: [https://github.com/Lakshita110/Trivia-Web-Application](https://github.com/Lakshita110/Trivia-Web-Application)

# Directory: 
	(within main directory)
	· app
		○ home 
			§ __init__.py
			§ forms.py 
			form which looks similar to the one here.
			§ routes.py
			# two routes, one to the home page with the form which then redirects to the start page for the quiz.
		○ auth/user
			§ __init__.py
			§ forms.py
			# login form, register form, logout form
			§ routes.py
			# four routes, login route, register route, logout route and profile route (displays all scores)
		○ quiz
			§ __init__.py
			§ forms.py
			# multiple choice question form
			§ routes.py
			# two routes, quiz route, score route 
		○ templates
			§ home.html
			§ login.html
			§ logout.html
			§ profile.html
			§ quiz.html
			§ register.html
			§ score.html
			§ start.html
	· config.py
	· .env
	· trivia_time.py
	· base.html
