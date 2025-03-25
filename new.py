import time

DEBUG = True

# debug functions
def _debug_message(error_on: str,
                    message: str):
    print(f"\n/!\\ DEBUG --\n\tERROR ON:\t`{error_on}`\n\tMESSAGE:\t\"{message}\"\n/!\\\n")

# utility functions
def get_input(prompt="> "):
    return input(prompt).strip().lower()


# utility classes
class CONTROLLER:
    """
    The CONTROLLER class is used as the base class for inheritance to subclasses of type:
      - NPC
      - Player
    As well as their respective subclasses.

    Args:
      - name: str [default='NONE']
      - current_health: int [default=0] [bounds:ch<=mh, ch>=0]
      - max_health: int [default=1] [bounds:mh>0]

    funcs:
      - set/get name, current_health, max_health
      - __debug : returns the value of all known class variables
    """
    def __init__(self,
                 name: str="NONE",
                 max_health: int=1,
                 current_health: int=0):
        self.__name = "NONE"
        self.__max_health = 1
        self.__current_health = 0

        self.set_name(name)
        self.set_max_health(max_health)
        self.set_current_health(current_health)

    # information functions
    def set_name(self,
                 name: str):
        self.__name = name.strip().title()
    def get_name(self):
        return self.__name


    def set_max_health(self,
                       max_health: int=1):
        # max health greater than 0 and is an integer
        if max_health > 0 and isinstance(max_health, int):
            self.__max_health = max_health
            # ensure current health does not exceed new max health
            if self.get_current_health() > max_health:
                self.set_current_health(max_health)
        else:
            self.__max_health = 1
            if DEBUG:
                _debug_message(error_on="`set_max_health",
                                message=f"`max_health` var could not be assigned.")
    def get_max_health(self):
        return self.__max_health


    def set_current_health(self,
                           current_health: int=0):
        if current_health >= 0 and current_health <= self.get_max_health():
            self.__current_health = current_health
        else:
            self.__current_health = -999

            if DEBUG:
                _debug_message(error_on="set_current_health",
                                message=f"`current_health` var could not be assigned.")
    def get_current_health(self):
        return self.__current_health


    def get_full_health(self,
                       seperator: str="/",
                       containers: list=['(', ')']):
        return f"{containers[0]}{self.get_current_health()}{seperator}{self.get_max_health()}{containers[1]}"


    # dialogue functions
    def dialogue(self,
                 message: list=["NONE"],
                 word_delay: float=0.3,
                 character_delay: float=0.08):
        print(f"{self.get_name()}: ", end="\"")
        for idx, line in enumerate(message):
            words = line.split()
            for index, word in enumerate(words):
                for char in word:
                    print(char, end='', flush=True)
                    time.sleep(character_delay)

                # if it is not the last word in `words` and there are still more lines to print
                if index != len(words) - 1 and len(words) - 1 > 0:
                    print(" ", end='')
                else:
                    print("", end='')

            if idx != len(message) - 1:
                print(" ", end='', flush=True)
            time.sleep(word_delay)
        print("\"")


    def __repr__(self):
        return f"[\n\tname: {self.get_name()}\n\thealth: {self.get_full_health()}\n]"

controller = CONTROLLER(
    name="mr. player",
    max_health=10,
    current_health=4
)
print(controller)

controller.set_current_health(controller.get_current_health() - 1)
controller.dialogue(
    message=['Ouch!', 'That hurt.', "Please don't do that again!"],
    word_delay=0.3,
    character_delay=0.08
)
print(controller)