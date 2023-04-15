# Haunted Mansion

## JSON Files
JSON (JavaScript Object Notation) is a really easy way to keep store data for code to use without cluttering the source code. In this project JSON is used to store the following:
- Rooms
- Items
- Enemies
- Player Data

JSON data is represented like this:
` 
{
    "propertyName": "stringValue",
    "numberProp": 2,
    "propWithArray": [ "Henlo", "Stinky", 5 ],
    "boolProp": false,
    "objectProp": {
        "firstWord": "Hello",
        "secondWord": "World"
    }
}
`

The object is denoted by the outter curly braces that contain all of the information inside. Objects are always surrounded by curly braces. Within the braces are *key value pairs*. The keys must be contained within quotation marks and followed by a colon. The value can be either a string, which needs quotes around it, a number, a boolean (true/false), an array, or another object.

I will be using this site to figure out how to parse JSON files with python:
https://www.geeksforgeeks.org/read-json-file-using-python/
