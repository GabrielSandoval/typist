source ~/.bash_profile

ECHO "ACTIVATING ENVIRONMENT"

conda activate typist-dev

ECHO "RUNNING APPLICATION ($PWD)/app.py"

python ${PWD}/app.py
