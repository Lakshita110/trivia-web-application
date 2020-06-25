# Trivia-Web-Application

# Plan for Trivia-Time Directory: 
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
README.md 