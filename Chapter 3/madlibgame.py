jkl'''
Created on Jan 20, 2017

@author: 19augusthummert
'''
print("THE MAD LIB GAME")
print("Enter Answers to the Following...\n")

noun1 = input("Enter a noun.. ")
noun2 = input("Enter a verb.. ")
noun3 = input("Enter another verb... ")
noun4 = input("Enter a noun.. ")
noun5 = input("Enter verb that associates with running.. ")
noun6 = input("Enter an item in your house.. ")
noun7 = input("Enter a verb ")
noun8 = input("Enter a noun.. ")
noun9 = input("Enter a noun.. ")
noun10 = input("Enter a verb.. ")
noun11 = input("Enter a noun.. ")
noun12 = input("Enter the final word and verb.. ")
story = """
    One day, Gerald and Piggie decided to go on a NOUN1.
    Piggie! "We will need to gather many things!" said Gerald who began to
    NOUN2. "Will we NOUN3?" Asked Piggie. "Of course" said Gerald. "So we will
    need to pack NOUN4." Piggie NOUN5 home trying to find NOUN6 to take with them.
    Gerald NOUN7 in his closet to get a NOUN8 in case it rained. "I think we might need
    NOUN8 so we don't get too hungry." Piggie said when she returned. They made sure
    to pack NOUN9 to snack on. "I really hope we get to NOUN10 in the ocean when we
    get there!" Piggie said. So Gerald and Piggie jumped in their NOUN11 and left.
    "Maybe we could NOUN12 after this!" said Piggie. "I guess so." said Gerald.

        """

story = story.replace("NOUN1", noun1)
story = story.replace("NOUN2", noun2)
story = story.replace("NOUN3", noun3)
story = story.replace("NOUN4", noun4)
story = story.replace("NOUN5", noun5)
story = story.replace("NOUN6", noun6)
story = story.replace("NOUN7", noun7)
story = story.replace("NOUN8", noun8)
story = story.replace("NOUN9", noun9)
story = story.replace("NOUN10", noun10)
story = story.replace("NOUN11", noun11)
story = story.replace("NOUN12", noun12)




file = open("madlib.txt", "w")
file.writelines(story)
file.close()
