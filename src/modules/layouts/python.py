"""
Project Workspace Filesystem Structure Layout : Python
"""
import os
import sys

class Layouts():
	"""
	Your Layouts

	Syntax:
		my_layouts = {
			layout_name = [
				{ "alias" : "folder-alias-name", "type" : "File/Folder", "path" : "/path/to/folder/or/file" },
				# Only for files
				{ "alias" : "file-alias-name", "type" : "File", "path" : "/path/to/file", "contents" : "Contents Here" }
			]
		}
	"""

	def __init__(self, project_name, default_layout="main"):
		"""
		Set Layouts
		"""
		self.project_name = project_name
		self.default_layout = default_layout

		self.my_layouts = {
			"main" : [
				{ "alias" : "documents", "type" : "Folder", "path" : "{}/docs".format(self.project_name) },
				{ "alias" : "source", "type" : "Folder", "path" : "{}/src".format(self.project_name) },
				{ "alias" : "modules", "type" : "Folder", "path" : "{}/src/modules".format(self.project_name) },
				{ "alias" : "resources", "type" : "Folder", "path" : "{}/src/resources".format(self.project_name) },
				{ 
					"alias" : "main.py", 
					"type" : "File", 
					"path" : "{}/src/main.py".format(self.project_name), 
					"contents" : \
"""
import os
import sys

def main():
	print("Hello World")

if __name__ == \"__main__\":
	main()
""" 
				},
			]
		}