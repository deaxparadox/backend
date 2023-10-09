# STEPS
# 1. Create python env
# 2. Activate python env
# 3. Upgrade pip and install packages


# 1. Create Python env
python -m venv "venv/$1"

# 2. Activate environment
source "venv/$1/bin/activate"

# 3. Upgrade pip and install packages
pip install --upgrade pip  && pip install -r "assets/requirements_django.txt"