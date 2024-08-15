#!/bin/bash

<<License

This file is part of PlayNexus.

Copyright (C) 2024

* Guilherme Oliveira Santos [gssantoz2012@gmail.com],
* 

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

License

# ================== Variables ==================

VENV_DIR="venv"

# Color codes for debug messages
DEBUG_COLOR="\033[0;36m"  
ERROR_COLOR="\033[0;31m"  
RESET_COLOR="\033[0m"    

# ================== Functions ==================

_debug () {
  local message="$1"
  local type="$2"
  
  if [ "$type" -eq 0 ]; then
    echo -e "${DEBUG_COLOR}[ DEBUG ]: ${message}${RESET_COLOR}"
  elif [ "$type" -eq 1 ]; then
    echo -e "${ERROR_COLOR}[ ERROR ]: ${message}${RESET_COLOR}"
  fi
}

check_install_package() {
  local package_name="$1"
  if ! dpkg -l | grep -q "^ii\s*$package_name"; then
    _debug "Package $package_name is not installed. Installing..." 0
    sudo apt install -y $package_name > /dev/null
    if [ $? -ne 0 ]; then
      _debug "Failed to install $package_name." 1
      exit 1
    fi
  else
    _debug "Package $package_name is already installed." 0
  fi
}

create_and_activate_venv() {
  if [ ! -d "$VENV_DIR" ]; then
    _debug "Creating virtual environment..." 0
    python3 -m venv $VENV_DIR
    if [ $? -ne 0 ]; then
      _debug "Failed to create the virtual environment." 1
      exit 1
    fi
  fi

  if [ -f "$VENV_DIR/bin/activate" ]; then
    _debug "Activating virtual environment..." 0
    source $VENV_DIR/bin/activate
    if [ $? -ne 0 ]; then
      _debug "Failed to activate the virtual environment." 1
      exit 1
    fi
  else
    _debug "Activation script not found at $VENV_DIR/bin/activate" 1
    exit 1
  fi
}

install_libs(){
  pip install -r requirements.txt
}

# ================== Main ==================

check_install_package python3.11-venv
check_install_package python3-pip

create_and_activate_venv

install_libs

if [ $? -ne 0 ]; then
  _debug "Library installation failed." 1
  exit 1
fi

## Run the main script

python3 src/main.py