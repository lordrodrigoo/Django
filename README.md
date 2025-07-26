# This content is about my course. So here I'll make some anotations that help me with the commands
# My system is Windows, so all commands will be for Windows .

# Git and Git Hub
ssh-keygen

# 1- Creating Enviroment 
python -m env env
.\venv\Scripts\activate 

# 2 - Creating the Project 
pip install django 
python.exe -m pip install --upgrade pip  (optional)

django-admin --help (if want know more about commands)
django-admin startproject project . (note: I used . for created my folders in root on the project )

python manage.py runserver 

python manage.py migrate  (make your migration when necessary )



# About testing
-- For use coverage:
    pip install coverage
    coverage run -m pytest

-- for visualization:
    coverage html (crete a folder htmlvoc (into this folder you can access the file index.com ))
