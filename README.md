# NOVA Development Tools and Guides

## Introduction
The [Next-Generation Open-Source Virtual Assistant](https://github.com/00Julian00/Nova.git) (or NOVA) is an easily expandable and modifyable virtual assistant. It uses Modules to add functionality. This repository will help you with developing Modules by providing tools, templates and guides.

## What is a Module?
A Module is essentially code that can be executed by NOVA. Every Module needs a manifest.json file with a predetermined structure in order for NOVA to use it. You can use the provided ManifestBuilder.py to build a correct manifest in the console.

## The File Structure of a Module
Each module is its own folder, all located in 'Modules'. In the folder, there needs to be a [manifest.json](#the-manifest-builder) and the [Entry Script](#the-entry-script). Other then that, the structure of your module is open and you can design it however you want.

## The Manifest Builder
When you run ManifestBuilder.py, it will search for a preexisting manifest.json file in the same directory. If it doesn't find one, it will create it. In the menu, you will be presented with a list of parameters that you have to fill out. Choose one by typing its number and press enter. Fill out the info and press enter again to return to the main menu.

## The Parameters in the Manifest
- Module Name (required): The name of your module.
- Module Description (required): A description of what your module does, what information it returns and when and how to use it.
- Entry Script (required): The name of the script in which the Entry Function is that will be called when the module is called. Must be in the root directory of the module. Include the file extension ('ScriptName.py').
- Entry Function (required): The function in the Entry Script that will be called. The parentheses at the end are not required ('EntryFunction').
- Parameters (optional): Opens a new menu. Here you can choose a parameter to edit, add a new one or deltete one. The parameters are passed to your entry function. The number of parameters must match the number of parameters your Entry Function takes. Each parameter needs a name, description and type (String, Integer, etc.)

## The Entry Script
- The Entry Script is a python file that sits in the root directory of your module and contains the Entry Function that will be called to activate the module. The Entry Script can either return None, or a String. These will be considered a sucessfull execution of the module. If a string is returned, it will be passed back to the AI. If False is returned, the execution is considered to have failed. You can use these to give the AI extra context about what your module is doing.

## Security
As a Module is, at its core, just Python code that gets executed by Nova, it allows bad actors to run harmful code on your machine that could damage your machine, steal your data or similar. To prevent this, certain Python libraries cannot be used in a module. These include os, sys, subprocess and keyring. When developing a module, do not use these libraries, as trying to import them in your code will result in your code being terminated by the Nova system and the user receiving a warning about the module. Keep in mind that this system is not perfect and bad actors can still find ways to execute harmful code on your machine using Nova Modules. This is why you should always double-check the source code of Modules before running them and just use Modules which you completely trust. Nova's security systems will be updated over time to improve security; however, the best way to protect yourself is to never trust a Module that you have not developed yourself or when you do not understand how it works.
