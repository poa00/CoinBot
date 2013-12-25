#!/usr/bin/python
####################################################################################
# File: CoinBot_Utils.py
# Purpose: A module that contains general purpose functions
# Constraints: Must be imported into a main namespace Python file
# Usage: import CoinBot_Utils
####################################################################################
# Imports
####################################################################################
import os
####################################################################################
# Utilities
####################################################################################
# Gets the time and date
# Create directory if none exist
def ensureDirPath(path):
	if not os.path.exists(path):
		print "Directory does not exist"
		print path
		os.makedirs(path)
		return False
	else:
		return True