This is the minimum viable solution to the DE 1.1 project
# DiceRoll
DiceRoll is a python class that implements a dice-rolling interface. It allows the user to roll multiple dice, with a specified number of sides, a specified number of times. The program also keeps track of the result of each throw and provides an interface to print the list of all throws and their sum.

## Usage
To use the DiceRoll class, simply create an instance of the class, and then call the dice_interface() method. This will present the user with a menu to roll the dice, print the list of throws, or exit the program. The program uses default values of 5 dice, 6 sides each, and 3 throws. However, the user can specify their own values for these parameters by entering integers for the number of dice, the number of sides, and the number of throws, separated by spaces, when prompted.

## Example
Here's an example of how to use the DiceRoll class:

 from DiceRoll import DiceRoll
 dr = DiceRoll()
 dr.dice_interface()
This will present the user with the following menu:

Choose command(roll, print_list, exit): 
The user can then enter roll to roll the dice, print_list to print the list of throws, or exit to exit the program.

## DiceRoll class
The DiceRoll class has the following methods:

### dice_roll(): rolls the dice as specified by the number of dice, number of sides, and number of throws. The results of each throw are stored in the dice_results list.

### dice_truncate_list(): keeps the dice_results list from growing too large by removing the first item in the list if the length of the list exceeds 100 items.

### dice_print_list(): prints the full list of throws and the sum of all values in the dice_results list.

### dice_interface(): presents the user with a menu to roll the dice, print the list of throws, or exit the program.

### dice_ask_input(): prompts the user to enter values for the number of dice, number of sides, and number of throws. If the user enters invalid input or simply presses enter, the default values of 5 dice, 6 sides each, and 3 throws are used.