# zip_radius_tool
Tool for grabbing a list of zips in a specified radius for a list of provided zips

## Steps to start server locally for deveopment

* Note: This project utilizes Pyenv and Peotry for version and dependency management.

From the "zip_radius_tool/" directory:
1) Ensure the correct version of python is install and set using:
	- "pyenv install 3.9"
	- "pyenv local 3.9"
2) Run "poetry install"
1) Run "poetry shell"
2) Run "cd zip_radius_app/"
3) Run "python3 manage.py runserver"
4) Open the application by pasting the server link given in the terminal into your browser and appending "zip_app/"
