#A simple interface for modifying Module manifests.

import os
import json
from prompt_toolkit import prompt

script_dir = os.path.dirname(os.path.realpath(__file__))

manifestStructure = {
    "ModuleName": "",
    "ModuleDescription": "",
    "EntryScript": "",
    "EntryFunction": "",
    "Parameters": {}
}

def GetManifest():
    try:
        with open(os.path.join(script_dir, "manifest.json"), 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def CreateManifestFile():
    with open(os.path.join(script_dir, "manifest.json"), 'w') as file:
        json.dump(manifestStructure, file, indent=4)

def PrintHeader():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Nova-Module Manifest Builder. Developed by Julian\n\n")

def MainInterface():
    PrintHeader()
    print("Opening manifest...")
    try:
        manifest = GetManifest()
    except:
        print("Error: The manifest file has an invalid structure. Exiting...")
        return
    
    if manifest is None:
        print("No manifest file found. Creating a new one...\n\n")
        CreateManifestFile()
        manifest = manifestStructure

    while True:
        PrintHeader()
        try:
            print("1. Module Name: " + manifest["ModuleName"])
            print("2. Module Description: " + manifest["ModuleDescription"])
            print("3. Entry Script: " + manifest["EntryScript"])
            print("4. Entry Function: " + manifest["EntryFunction"])
            print("5. Parameters: ")
            for param, details in manifest["Parameters"].items():
                print(f"   {param}: {details}")
        except:
            print("Error: The manifest file has an invalid structure. Exiting...")
            return

        print("\nChoose field to edit by typing the number. Press enter to save to file. Type 'Cancel' to discard changes.")
        inp = input("> ")

        if inp == "":
            with open(os.path.join(script_dir, "manifest.json"), 'w') as file:
                json.dump(manifest, file, indent=4)
            print("Saved manifest file. Exiting...")
            return
        
        if inp == "Cancel":
            print("Discarding changes. Exiting...")
            return

        PrintHeader()

        if inp == "1":
            print("Type the new value and press enter to save. Press enter to keep the current value.")
            manifest["ModuleName"] = prompt("Module Name: ", default = manifest["ModuleName"])
        elif inp == "2":
            print("Type the new value and press enter to save. Press enter to keep the current value.")
            manifest["ModuleDescription"] = prompt("Module Description: ", default = manifest["ModuleDescription"])
        elif inp == "3":
            print("Type the new value and press enter to save. Press enter to keep the current value.")
            manifest["EntryScript"] = prompt("Entry Script: ", default = manifest["EntryScript"])
        elif inp == "4":
            print("Type the new value and press enter to save. Press enter to keep the current value.")
            manifest["EntryFunction"] = prompt("Entry Function: ", default = manifest["EntryFunction"])
        elif inp == "5":
            while True:
                PrintHeader()
                print("Type the parameter name you want to edit. Type 'add' to add a new parameter. Type a parameter name followed by --del to delete it. Press enter to save.\n")
                for param, details in manifest["Parameters"].items():
                    print(f"{param}: {details}")

                inp = input("\n> ")

                if inp == "":
                    break

                if inp == "add":
                    print("Type the new parameter name and press enter to save. Press enter to cancel.")
                    newParam = prompt("New Parameter: ")

                    paramExists = False
                    for param, details in manifest["Parameters"].items():
                        if (newParam == param):
                            paramExists = True
                            print("Parameter already exists. Cancelling...")
                            break
                        
                    if paramExists:
                        break

                    if newParam != "":
                        manifest["Parameters"][newParam] = {"Description": "", "Type": ""}
                        print("Type the new value and press enter to save.")
                        manifest["Parameters"][newParam]["Description"] = prompt(f"{newParam} description: ")
                        manifest["Parameters"][newParam]["Type"] = prompt(f"{newParam} type: ")
                    else:
                        print("Name can not be empty. Cancelling...")

                for param, details in manifest["Parameters"].items():
                    if (inp == param):
                        print("Type the new value and press enter to save. Press enter to keep the current value.")
                        manifest["Parameters"][param]["Description"] = prompt(f"{param}: ", default = manifest["Parameters"][param]["Description"])
                        manifest["Parameters"][param]["Type"] = prompt(f"{param}: ", default = manifest["Parameters"][param]["Type"])
                        break

                    if (inp == param + " --del"):
                        confirm = input(f"Are you sure you want to delete {param} [y/n] ")
                        if (confirm == "y"):
                            del manifest["Parameters"][param]
                            break                       

MainInterface()