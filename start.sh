export FLASK_ENV=development

pip freeze < requirements.txt

export FLASK_APP=run.py

flask run