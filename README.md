# Project Workspace File Structure Generator 

A Multi-language, All-in-One Project Workspace Filesystem Structure Generator
	- Aims to make the initial generating of project workspac
	- Allows for custom workspace layout, just by editing the layout in the python module

## Table of Contents
 
* [Background](#background)
* [Project Information](#project-information)
* [Obtaining](#obtaining)
* [Pre-Requisites](#pre-requisites)
* [Building/Making/Compilation](#building-making-compilation)
* [Documentation](#documentation)
* [Contacts](#contacts)
* [Remarks](#remarks)

## Background

The function of the program is simple : To generate an appropriate filesystem structure layout according to the required 
	1. Programming/Scripting Language
	2. Framework
	3. Specific Layout
	4. Platform

Certain project workspace file structures can be very big, such as
	- Android + Gradle
Thus, this project aims to assist in making the trouble of generating of workspace for these kinds of layouts easier 

## Project Information

- Program Name : proj-genfs
- Language : Python
- Frameworks : NIL
- Platform : Deskop
- Operating System : Windows, GNU/Linux
- Plans:
	- Mobile App Support

## Obtaining

via Cloning
	- Full Clone
		git clone https://github.com/Thanatisia/proj-genfs

## Pre-Requisites

- No dependencies at the moment

## Building/Making/Compilation

- Planning to include pyinstaller support to compile program to executable

## Documentation

- Syntax: python proj-genfs {options} <arguments> [--project "project-filename"]
- Parameters:
	- options:
		* --help : Get this help
		* --language : Specify Language
		* --framework : Specify Framework you are working with; Needs to be used together with '--language'
		* --layout : Specify Layout to use; Needs to be used together with '--language'
		* --platform : Specify Device/Platform you are operating on
			- Examples:
				* Mobile  | Android, iOS
				* Desktop | Windows, MacOS, GNU/Linux
				* Website
	- Defaults:
		- No Options Provided
			- default layout
			

- Customization:
 
	- Background:
		* The method of customization is primarily done in the layout modules.

		* The layout modules are found in 'proj-genfs/src/modules/layouts/[file.py]
			- all files are categorised with the option '--language'
			- Ensure that the language you input has a language python module created in the layout modules directory
				- Recommend to copy the default.py file and paste as '[your-file].py'

		* Every layout is specified in the 'self.my_layouts' variable in the Layouts() class found in [your-file].py
			- The syntax is provided in the docfile in the class definition
			- All you need to change is the layouts inside the 'self.my_layouts' dictionary

	- Layout Content Definitions:
		- Keywords:
			* alias : A simple, easy to understand name for the file/folder you are creating. Used for identification after creating
			* type	: The type of item you are creating. Options : File/Folder
			* path	: Full path of the file (including file name if is file)
			- Files Only
				* contents : Content/Text you want to write into the file


	* Example:
		
		```
		NOTES:
			- Language : cpp
			- File Name : cpp.py
			- Layout Name : "main"
			- Info:
				- In this, I want all subdirectories and subfiles to be under the Project Workspace/Folder

		self.my_layouts = {
			"main" : [
				{ "alias" : "root", "type" : "Folder", "path" : "{}".format(self.project_name) },
				{ 
					"alias" : "main", 
					"type" : "File", 
					"path" : "{}/main.cpp".format(self.project_name), 
					"contents" : \ 
"""
#include <stdio.h>
#include <iostream>
#include <string>
using std::cout;
using std::cin;
using std::endl;
using std::getline;
using std::to_string;
int main(int argc, const char *argv[])
{
	cout << \"Hello World\" << endl;
	return 1;
}
"""					
				},
			],
			"layout_2" : [
				{ "alias" : "
			],
		}
		```

- Usage: 

	- To generate a default project:
		
		python proj-genfs --project "myProj"

	- To generate a simple Python project:

		python proj-genfs --language "python" --project "myProj"

	- To use a specific layout:
		```
		NOTE: You need to use this together with '--language <language>' 
		```
		
		python proj-genfs --language "cpp" --layout "layout_2" --project "myProj"

	- To generate for a specific platform
		```
		NOTE: This is still a WIP and is still being implemented
		```

		python proj-genfs --platform android --project "myProj"

	- To generate for a specific framework
		```
		NOTE: 
			- This is still a WIP and is still being implemented
			- You need to use this together with '--language <language>' 
		```

		python proj-genfs --language python --framework kivy --project "myProj"
	

## Contacts

- [Twitter](https://twitter.com/phantasu)
- [GitHub](https://github.com/Thanatisia)

## Remarks

- Please contact me if you have any bugs, ideas, feedback or if you would like to just talk to me about anything
