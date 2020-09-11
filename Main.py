# in order for VS Code to recognize the Python Env. you need to add the interpreter 
# with [Ctrl]+[Shift]+[P] and the command Python: Select Interpreter
# the JSON Lib is natively shipped with Python 3.8
import json

# writing to JSON file   
json_data = '{"people":[{"Employee ID":1,"Name":"Abhishek","Designation":"Software Engineer"},' \
            '{"Employee ID":2,"Name":"Garima","Designation":"Email Marketing Specialist"}]}'
   
json_object = json.loads(json_data) 
   
# Indent keyword while dumping the 
# data decides to what level  
# spaces the user wants.

data = json.dumps(json_object, indent = 3)

with open('data.txt', 'w') as outfile:
    json.dump(json_data, outfile)
    

# reading from JSON file
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Employee ID' + p['employee_id'])
        print('Name: ' + p['name'])
        print('Designation: ' + p['designation'])
        print('')