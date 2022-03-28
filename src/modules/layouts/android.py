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
			"layout_name" : [
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
				{ "alias" : "workspace", "type" : "Folder", "path" : "{}".format(self.project_name) },
				{ "alias" : "top-level gradle", "type" : "File", "path" : "{}/build.gradle".format(self.project_name), "contents" : "" },
				{ "alias" : "gradle settings", "type" : "File", "path" : "{}/settings.gradle".format(self.project_name), "contents" : "" },
				{ "alias" : "gradle-configs", "type" : "Folder", "path" : "{}/.gradle".format(self.project_name) },
				{ "alias" : "gradle properties", "type" : "File", "path" : "{}/.gradle/gradle.properties".format(self.project_name), "contents" : "" },
				{ "alias" : "app", "type" : "Folder", "path" : "{}/app".format(self.project_name) },
				{ "alias" : "module-level gradle", "type" : "File", "path" : "{}/app/build.gradle".format(self.project_name), "contents" : "" },
				{ "alias" : "build", "type" : "Folder", "path" : "{}/app/build".format(self.project_name) },
				{ "alias" : "libraries", "type" : "Folder", "path" : "{}/app/libs".format(self.project_name) },
				{ "alias" : "source", "type" : "Folder", "path" : "{}/app/src".format(self.project_name) },
				{ "alias" : "main", "type" : "Folder", "path" : "{}/app/src/main".format(self.project_name) },
				{ "alias" : "main-java", "type" : "Folder", "path" : "{}/app/src/main/java".format(self.project_name) },
				{ "alias" : "main-java-app_folder_root", "type" : "Folder", "path" : "{}/app/src/main/java/com".format(self.project_name) },
				{ "alias" : "main-java-organization", "type" : "Folder", "path" : "{}/app/src/main/java/com/organization".format(self.project_name) },
				{ "alias" : "main-java-project_name", "type" : "Folder", "path" : "{}/app/src/main/java/com/example/project-name".format(self.project_name) },
				{ "alias" : "main-java-project_classes", "type" : "File", "path" : "{}/app/src/main/java/com/example/project-name/MyApp.java".format(self.project_name), "contents" : "" },
				{ "alias" : "main-res", "type" : "Folder", "path" : "{}/app/src/main/res".format(self.project_name) },
				{ "alias" : "main-res-drawable", "type" : "Folder", "path" : "{}/app/src/main/res/drawable".format(self.project_name) },
				{ "alias" : "main-res-layout", "type" : "Folder", "path" : "{}/app/src/main/res/layout/".format(self.project_name) },
				{ "alias" : "main-res-layout-xml", "type" : "File", "path" : "{}/app/src/main/res/layout/myapp.xml".format(self.project_name), "contents" : "" },
			]
		}



	

