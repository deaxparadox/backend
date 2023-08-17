BACKEND="fastapi"

# create virtuan environment and activate it
python -m venv "venv/$BACKEND" && source "venv/$BACKEND/bin/activate"

# update pip and install requirements
pip install --upgrade pip && pip install -r asset/requirements.txt