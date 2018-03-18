export PYTHONPATH=$PWD
export FLASK_APP=swvl_auth.py
export FLASK_DEBUG=1
source env/bin/activate

python -m flask db upgrade

python -m flask run 
