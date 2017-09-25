# Laboratorio 3
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

import LinkedList

# To execute this code, you need to import
# the LinkedList.py file in this directory.

def excercise_2():

    def process_token(string):

        if string == "":
            return ""

        newString = LinkedList.LinkedList()

        placeBefore = False
        substr = ""
        for character in string:

            if character == "[":
                newString.add_at_start(substr) if placeBefore else newString.add(substr)
                substr = ""
                placeBefore = True
            elif character == "]":
                newString.add_at_start(substr) if placeBefore else newString.add(substr)
                substr = ""
                placeBefore = False
            else:
                substr += character

        newString.add_at_start(substr) if placeBefore else newString.add(substr)

        finalStr = ""
        current = newString.head
        while current != None:
            finalStr += current.data
            current = current.next

        return finalStr

    proccessed_tokens = []
    tokens = []
    token = input()
    while token != "EOF":
        proccessed_tokens.append(process_token(token))
        tokens.append(token)
        token = input()

    for p in proccessed_tokens:
        print(p)

excercise_2()
