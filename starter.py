import datetime
from io import TextIOWrapper
"""
The project is to begin as a simple mood tracker. It will ask everyday the mood of the individual and input it into the library of previous moods.

Later on developments will be made to produce statistics regarding the weekly, monthly, and yearly count ups of the moods.

Following this, activites that were done during the day can also be analyzed.

Finally a GUI to make the mood tracker interactive for the user.
Aleksandra Kalas
Created: 01/01/2023
Completed: --/--/----
"""
# Dictionary to keep track of moods that were inputted by user
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
moods = {}

def userInput(moodText: TextIOWrapper) -> None:
    """
    Ask for user input for their mood and add to the corresponding month in moods dictionary.
    """
    print("Welcome to your mood tracker Aleksandra!\n We hope that you are doing well. Please enter how you are feeling based on the following scale:\n")
    print("Sad | Irritable | Angry | Withdrawn | Sociable | Calm | Happy")
    m = input("How are you feeling today?")
    s = datetime.date.today().month
    
    # file is open for reading
    if moodText.readline() == datetime.date.today().year: # we are in the correct year
        # loop through text looking for todays month
        # check if we have already inputted a mood for today
        # if we haven't  
        pass 

    else: # either wrong year or need to add "new" year file
        pass

    # This code will become irrelevant once the above is completed
    if months[s - 1] in moods.keys():
        moods[months[s - 1]].append(m)
    else:
        moods[months[s - 1]] = [m]

    print(moods)
    

    
def main() -> None:
    continuation = input("Would you like to open the mood tracker? Please enter Y for yes or N for no")
    while (continuation == 'Y' or continuation == 'y' or continuation == 'Yes' or continuation == 'yes'):
        moodFile = open("moods.txt")
        userInput(moodFile)
        continuation = input("Would you like to open the mood tracker? Please enter Y for yes or N for no")
    print('Have a nice day!')

main()


