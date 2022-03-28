# Project Workspace File Structure Generator 

A Multi-language, All-in-One Project Workspace Filesystem Structure Generator
	- Aims to make the initial generating of project workspac
	- Allows for custom workspace layout, just by editing the layout in the python module

## Table of Contents
 
* [Background](#background)
# [Project Information](#project-information)
* [Obtaining](#obtaining)
* [Pre-Requisites](#pre-requisites)
* [Building/Making/Compilation](#building-making-compilation)
* [Documentation](#documentation)
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

Program Name : proj-genfs
Language : Python
Frameworks : NIL
Platform : Deskop
Operating System : Windows, GNU/Linux
Plans:
	- Mobile App Support

## Obtaining

## Pre-Requisites

## Building/Making/Compilation

## Documentation

- Syntax: python proj-genfs {options} <arguments> [--project "project-filename"]
- Parameters:
	> options:
		* --help : Get this help
		* --language : Specify Language
		* --framework : Specify Framework you are working with
		* --layout : Specify Layout to use; Needs to be used together with '--language'
		* --platform : Specify Device/Platform you are operating on
			> Examples:
				* Mobile  | Android, iOS
				* Desktop | Windows, MacOS, GNU/Linux
				* Website
	> Defaults:
		# No Options Provided
			- default layout
			- 

- Usage: 

To generate a simple Python project:
	python proj-genfs --language "python" --project "myProj"
	
## Remarks