'''
CEASAR CIPHER
Gabrielle Gipaya
May , 2025

add the pseudocode n stuff later

'''

#SETUP

import microbit

# the * is what exits the program
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "*"]

original_message_idx = []
original_message = []
shiftedMessage = []
index = 0
key  = 0

#FUNCTIONS

#fruitful function that shifts a letter given by the shift amount
def shifting(letter, shift):
    
    #if the letter is the submit button, return as is
    if letter == "*":
        return letter
    
    #shift if in alphabet
    if letter in alphabet:
        
        #current index of letter
        index = alphabet.index(letter)
        
        #calculate NEWW INDEX by adding the shift and dividing by length of alphabet
        #if index is 26 and shift is 3, 26 + 3 = 29, modulo to go back to index 1, which isB 
        new_index = (index + shift) % 26
        
        return alphabet[new_index]
        
        
    return letter

#non-fruitful
def display_microbit(message):
    for letter in shiftedMessage:
        microbit.display.show(letter)
        microbit.sleep(500)
    
#START & SELECTING MODE
    
microbit.display.scroll("CAESAR CIPHER")

print("""
-------> CAESAR CIPHER <-------

1. Welcome to the Caesar Cipher!
This program lets you encrypt(cipher) or descypt(decipher) a message to display it on the computer's output.
you are given an option:
- if you choose "A" you Decipher/Decrypt.
- if you choose "B" you Cipher/Encrypt.
after you've submmited your message using the microbit, it will be displayed on the microbit of the computer's output
based on your choice.


2. - If you want to encrypt, Click A
- If you want to decrypt, Click B

""")

microbit.display.show(microbit.Image.HAPPY)

#KEY/SHIFT
key  = 0
print("""
1. Set your Key
2. Click A or B to continue
"""
) 
while True:
    if pin0.is_touched():
        shift = (shift + 1) % len(alphabet) #set limit to 0-25
        display.show(str(shift))
        sleep(300)
    elif button_a.was_pressed() or button_b.was_pressed():
        break

#ENCRYPT/DECRYPT
mode = None
print("""
1. Choose your Mode
-Click A to Encrypt
-Click B to Decrypt
""")
while mode is None:
    if microbit.button_a.was_pressed():
        mode = "encrypt"
        microbit.display.scroll("MODE: E")
        break
    elif microbit.button_b.was_pressed():
        mode = "decrypt"
        shift = -shift
        microbit.display.scroll("MODE: D")
        break
    

    

microbit.display.scroll("INPUT MSG")

#INPUT
    
microbit.display.show(alphabet[0])

while True:
    
    if microbit.button_a.was_pressed():
        index = (index + 1) % len(alphabet)
    
        microbit.display.show(alphabet[index])
        
    #INPUT
    elif microbit.button_b.was_pressed():
        letter = alphabet[index]
        if letter == "*":
            break
        
        else:
            original_message.append(letter)
            original_message_idx.append(index)
            microbit.display.show(alphabet[0])

            
#EXECUTING THE CIPHER
for i in original_message:
    new_letter = shifting(i, shift)
    shiftedMessage.append(new_letter)
    
microbit.display.show(microbit.Image.HAPPY)

print("""
Where would you like to see your message?

A + B -> Both
A -> Only on Microbit
B -> Only on Computer Ouptut

""")

#OUTPUT

display = None
while display is None:
    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        display = "both"
    elif microbit.button_a.was_pressed():
        display = "microbit"
    elif microbit.button_b.was_pressed():
        display = "computer"
        
if display == "microbit":
    display_microbit(shiftedMessage)
elif display == "computer":
    print("Original Message:", "".join(original_message))
    print("Translated Message:", "".join(shiftedMessage))
elif display == "both":
    print("Original Message:", "".join(original_message))
    print("Translated Message:", "".join(shiftedMessage))
    show_message_on_microbit(shiftedMessage)
    
        
            
'''
exceptional section, try without exceptional first
'''
