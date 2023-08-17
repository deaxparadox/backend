# create virtuan environment and activate it
python -m venv venv/django && source venv/django/bin/activate

# update pip and install requirements
pip install --upgrade pip && pip install -r asset/requirements.txt