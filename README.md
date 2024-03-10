
# AirBnB_clone project

The Airbnb Console project is a command-line interface(CLI) designed to manage and in interact with Airbnb property listings. This command interpreter provides users with the ability to create, update and delete bookings and listings.

## Command Interpreter

The command interpreter is a Python based CLI that allows users to interact with the Airbnb console. It provides commands for Airbnb listings, bookings and reservations from their terminal.

Some commands that are aavailable are:

- show
- create
- destroy
- count
- all
- update

## How to start

To start the Airbnb console:

Clone the repository in your local machine

## How to use it
  
1. Run the console

``
/AirBnB_clone$ ./console.py
``

2. This prompt should appear:

``
(hbnb)
``

3. Then you can implement the recognizable commands the interpreter does.

This are the available commands and what they do:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **help <command\>** | Provides a text describing how to use a command.  |
| **create <class name\>** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **show <class name\> <id\>** | Prints the string representation of an instance based on the class name and `id`  |
| **destroy <class name\> <id\>** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **all <class name\>** | Prints all string representation of all instances based or not on the class name.  |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **<class name\>.count()** | Retrieve the number of instances of a class.  |

## Examples

It should work in both interactive and interactive mode

The **interactive mode**:

``
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
``

The **non-interactive** mode

``
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
``

## AUTHOR

Agatha Mwaniki
