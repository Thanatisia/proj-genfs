"""
Arguments Utility
"""

import os
import sys

def get_opts(*argv):
	"""
	Get Options and Linked Arguments
	"""
	opts = {
		# "option" : "argument"
	}
	argc = len(argv)

	for i in range(argc):
		curr_arg = argv[i]

		# Check Even-Position Arguments
		if( (i % 2) == 0 ):
			opt = curr_arg
			if not(argv[i] in opts.keys()):
				opts[opt] = ""
		else:
			opt = argv[i-1]
			arg = curr_arg
			opts[opt] = arg 
	return opts