"""
Project Workspace File Structure Generator 

A Multi-language, All-in-One Project Workspace Filesystem Structure Generator
	- Aims to make the initial generating of project workspac
	- Allows for custom workspace layout, just by editing the layout in the python module
"""

import os
import sys
from importlib import import_module
from pathlib import Path

# External Libraries
import modules.argutils as argutils

# [Variables]

# Command Line Arguments
all_args = sys.argv
curr_script = all_args[0] # 1st Argument
argv = all_args[1:]
argc = len(argv)

# Global Variables
all_opts = {
	"Help" : "--help",
	"Language" : "--language",
	"Framework" : "--framework",
	"Layout" : "--layout",
	"Platform" : "--platform",
	"Project" : "--project"
}

considerations = [
	# Target parameters
	# to consider when generating
]

options = {
	# "option" : "argument"
}

# [Functions]

def genfs():
	"""
	Read Layout from Modules and
	Generate Workspace File Structure

	:: Params
		params
			Name : Parameters
			Type : Keywords Variable-Length Arguments
			Desc : Parameters to consider when generating the workspace
	"""
	lang = ""
	framework = ""
	layout = ""
	platform = ""
	project = options["--project"]

	# Import layout class according to your parameters
	if "Language" in considerations:
		flags = all_opts["Language"]
		lang = options[flags]
	else:
		# Default Layout
		lang = ""

	if "Layout" in considerations:
		flags = all_opts["Layout"]
		layout = options[flags]
	
	# Error handling : Defaults
	if lang == "":
		lang = "default"
	if layout == "":
		layout = "main"

	# [Process]

	# Check if project folder already exists in current working directory
	if not (os.path.exists(project)):
		# Does not exist
		# Proceed to create

		# Import according to language
		lang_module = import_module("modules.layouts.{}".format(lang))

		# Get Layout of your choice
		all_layouts = lang_module.Layouts(project).my_layouts

		# if layout in all_layouts.keys():
			# Layout exists
			# WIP			

		for layout, file_structure in all_layouts.items():
			print("Layout : {}".format(layout))
			print("")
			number_of_files = len(file_structure)
			for i in range(number_of_files):
				curr_path_desc = file_structure[i]
				alias = curr_path_desc["alias"]
				path_type = curr_path_desc["type"]
				path = curr_path_desc["path"]

				print("[C] => Creating {}...".format(path))

				if path_type == "Folder":
					# Folders	

					# Make Directory
					os.makedirs(path, exist_ok=True)

					# Verify
					if os.path.exists(path):
						print("[D] Folder {} has been created at [{}] successfully".format(alias, path))
				else:
					# Files

					# Verify contents exist
					if "contents" in curr_path_desc.keys():
						# Get contents specified
						contents = curr_path_desc["contents"]
					else:
						# Default to empty
						contents = ""

					# Create File
					with open(path, "a+") as f_create:
						f_create.write(contents)					
	
						# Close after using
						f_create.close()

					# Verify
					if os.path.exists(path):
						print("[D] File {} has been created at [{}] successfully".format(alias, path))
						print("with contents:")
						print("	{}".format(contents))

				print("")
	else:
		print("[E] Project Folder [{}] already exists.".format(project))

		
def setup():
	global options

	options = argutils.get_opts(*argv)
	action = ""

	# Ensure that non-optional arguments exist
	if "--project" in options.keys():
		# Switch Case Options
		# To get flags to consider
		for opt,arg in options.items():
			# Validate Parameter
			if opt in all_opts.values():
				if opt == "--help":
					considerations.append("Help")
				elif opt == "--language":
					considerations.append("Language")
				elif opt == "--framework":
					considerations.append("Framework")
				elif opt == "--layout":
					# must be used together with --language
					if "--language" in options.keys():
						considerations.append("Layout")
					else:
						print("[W] Warning : '--language' option is not used, --layout flag is ignored.")
				elif opt == "--platform":
					considerations.append("Platform")	
				elif opt == "--project":
					considerations.append("Project")
		print("")
	else:
		print("[X] Error : Project Not Specified, please specify '--project <project_name>'")

def main():
	setup()

	if "Project" in considerations:
		number_of_flags = len(considerations)
		if(number_of_flags > 0):
			print("Generating Project Workspace File Structure with the following parameters:")
			# Loop through all flags to consider in the generating of the workspace
			for i in range(number_of_flags):
				curr_todo = considerations[i]
				flag = all_opts[curr_todo]
				arg = options[flag]
		
				print("	{} : {}".format(curr_todo, arg))

		print("")

	
		proceed_conf = input("Proceed with generating workspace file structure? [Y|N]: ")

		print("")

		# Switch Case
		if proceed_conf == "Y" or proceed_conf == "y":
			# Yes
			print("[O] Generating : Project Workspace File Structure...")
			genfs()
		else:
			# No
			print("Operation has been cancelled.")


if __name__ == "__main__":
	main()