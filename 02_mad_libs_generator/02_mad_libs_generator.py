import sys

Story = "Once upon a time there was a %s %s who %s %s the fair lady!\n"
noun1 = raw_input("Please Type a Noun:\n")
adjective1 = raw_input("Please Type an Adjective:\n")
verb1 = raw_input("Please Type a Verb:\n")
adverb1 = raw_input("Please Type an Adverb:\n")
print("\n")
print(Story % (adjective1, noun1, adverb1, verb1))