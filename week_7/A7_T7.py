'''
The program must handle:

3 x Rotors with 26 positions (A-Z)
1 x Reflector - Types A, B & C
0 x Plugboard. Prompt is required, but no need to implement.
The order of machine operations described:

User presses letter on the keyboard
Keypress is passed via plugboard (skipped in this exercise)
Rotate the wheels (positions)
Scramble current letter using “Forward pass-through” process
Iterate through rotors in order 1-3
Create offset using current rotor position and the letter
Use the offset to shift the given letter in alphabets
Scramble current letter using using the reflector
Scramble current letter using “Reverse pass-through” process
Iterate through rotors in reverse order
Change current letter based on each wheel position offset
In this program, user inserts row and the scrambling starts always from positions [0, 0, 0]. So enter press means that the program must reset the positions before scrambling the inserted text. The Enigma machine will shut down if the user enters an empty line.

Recommended datastructures:

Rotors(characters): list[str]
Positions(rotor positions): list[int]
Reflector: str
'''

# no idea!