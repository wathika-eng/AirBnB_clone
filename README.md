Interactive Mode:
Run the Shell Script:

Execute the shell script ./console.py to start the interactive mode.
Shell Prompt (hbnb):

The presence of (hbnb) indicates that the shell is ready to receive commands.
Help Command:

Typing help within the shell prompts the display of documented commands.
User Interaction:

The user can then enter various commands and interact with the shell.
Quit Command:

Typing quit exits the shell, returning to the terminal.
Example:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-Interactive Mode:
Command Input via Echo:

Instead of manually entering commands, input commands via a pipeline using echo.
Example Commands:

Examples include piping the command help into the shell script.
Example:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
Non-Interactive Mode with File Input:
Create a File with Commands:

Create a file (e.g., test_help) containing commands (e.g., help).
Display File Contents with Cat:

Use cat to display the contents of the file.
Pipe File Contents into Shell Script:

Pipe the file contents into the shell script to simulate non-interactive mode with file input.
Example:

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
