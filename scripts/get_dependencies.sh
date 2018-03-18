#!/bin/bash
set -e
# get parent dir
home="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ && pwd )"

# delete Python virtual environment and recreate it
rm -rf $home/env

if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform
    virtualenv --python=python2.7 $home/env
    echo "export PYTHONPATH='$home'" >> $home/env/bin/activate
    # enter the venv and install dependencies
    source $home/env/bin/activate
    # allows the code to explore modules in the same folder
    # installs project dependencies
    pip install -r $home/requirements.txt

fi

