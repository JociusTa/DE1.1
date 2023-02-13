from random import randint

dice_results = []


class DiceRoll:
    """
    A class for rolling dice
    """

    def __init__(self, throws=3, count=5, sides=6):
        """
        Initialize the DiceRoll class with default values of 3 throws, 5 dice, and 6 sides.
        """
        self.throws = throws
        self.count = count
        self.sides = sides

    def dice_roll(self):
        """
        Roll the dice the specified number of times, storing the results in the dice_results list.
        """
        self.dice_ask_input()
        for throw in range(self.throws):
            one_dice_result = []
            for dice in range(self.count):
                result = randint(1, self.sides)
                one_dice_result.append(result)
            dice_results.append(one_dice_result)
            self.dice_truncate_list()
            self.dice_print_list()

    def dice_truncate_list(self):
        """
        Truncate the dice_results list so that it never contains more than 100 elements.
        """
        dice_results.append(dice_results[-1])
        if len(dice_results) > 100:
            dice_results.pop(0)

    def dice_print_list(self):
        """
        Print the sum of all values in dice_results and the full list of throws.
        """
        print("Sum of all values in dice_results:", sum(dice_results[-1]), "Full list of throws:", dice_results[-1])

    def dice_interface(self):
        """
        Interact with the user to allow them to roll the dice, view the list of results, or exit the program.
        """
        while True:
            user_input = input("Choose command(roll, print_list, exit): ")
            if user_input.lower() == "roll":
                self.dice_ask_input()
                self.dice_roll()
            elif user_input.lower() == "print_list":
                print(dice_results)
            elif user_input.lower() == "exit":
                break
            else:
                print("Invalid command.")

    def dice_ask_input(self):
        """
        Ask the user for the number of dice, sides, and throws, or use the default values if no input is provided.
        """
        while True:
            try:
                user_input = input(
                    'Enter integers for amount of dice, sides, amount of throws, separated by space,'
                    ' or enter for default(5 3 6)').strip()
                if not user_input:
                    count, sides, throws = self.count, self.sides, self.throws
                    break
                else:
                    count, sides, throws = map(int, user_input.split())
                    break
            except ValueError:
                print("Invalid input, please try again")
        self.count, self.sides, self.throws = count, sides, throws


dr = DiceRoll()
dr.dice_interface()
