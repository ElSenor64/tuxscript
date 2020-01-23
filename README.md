# Tux Script
A Linux Scripting IDE in the style of the Apple Script IDE.

This application is currently in the pre-alpha stage. It is currently in python in order to get a good feel for the template / form. In beta, it will be converted to C++.

The app window consists of three parts:
- Editor
- Reference Pane
- Console

    The Editor is where you type the script. It will save, auto-update, and will eventually have full color support and autofilling. It may even, sometime in the future, have command history support builtin.

    The Reference Pane allows the user to drag out pre-built code-snippets so that they don't have to memorize all the bash syntax.

    The Console Pane allows users to 1) interact with / give user input to the script, 2) view terminal output for the sake of debugging, 3) add lines to the end of your script terminal-style.

    Figure 1 - The window concept preview (as of now)
     ____________________________________________________________________________________
    | *v*                          `|`    |``                                  __  ⟑   \/|
    |_(_)___________________________|_UX___``|CRIPT_______________________________⥒⥓__/\|
    |v_Commands_(Ref)__X|v_Editor___(*~/Documents/Hello World)__________________________X|
    |v apps             | cd Documents                                                   |
    |   echo            | input_______ >> thewords.txt                                   |
    |   figlet          | read -p "Type something:" mystring                             |
    |   stegosaurus     | mystring = ${mystring}                                         |
    |   espeak          | if [ $mystring = "Nope" ]                                      |
    |   cmatrix         | then                                                           |
    |   bb              |     figlet "NOPE!"                                             |    
    |   nano            |     sleep 1s                                                   |                
    |   pi              |     stegosaurus "NOPE!"                                        |
    |   term2048        |     sleep 1s                                                   |
    |   sl              |     echo "Wait! There's more!"                                 |
    |> dialogs and input|     sleep 2s                                                   |
    |v logic            |     espeak "NOPE!"                                             |
    |   cd              | fi                                                             |
    |   ls              |                                                                |
    |   if              |                                                                |
    |   while           |                                                                |
    |   $var            |                                                                |
    |   >> tunnel       |                                                                |
    |   && run x then y |________________________________________________________________|
    |   & background    |v_Console____________________________________________________⋯_X|
    |   # ignore        |user@Computer:~/Documents$                                      |
    |> etc              |                                                                |
    |                   |                                                                |
    |                   |________________________________________________________________|
    |___________________|>|______________________________________________________________|
    |_________________________________________________________Line_x,_Column_y,_Language_|
    
read -n 1 -p "I understand (Y/n)" dewarn
dewarn=${dewarn:-y}
if [ $dewarn = y ]
then



We hope you enjoy!

Credits:
Josh L
Byron S
(Jacob H)?
(Ben L)?
(Carter H)?