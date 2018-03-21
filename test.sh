# Runs unit tests on the whole project

# stops the script if any of the commands fail
set -e

export PYTHONPATH=$PWD
export FLASK_APP=swvl_auth.py
export FLASK_DEBUG=1
source env/bin/activate


nosetests -xv --all-modules --ignore-files="server.py" --exe -w app

# Explain nosetests flags
#   exe= run tests included in executable files
#   x= stop on first