# Produce a simple program to accept a single word as text input and then print out the pig latin translation. 


piglatin = input("What word would you like to translate?")

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l" ,"m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if input[0] == vowels: 
    print (input + "yay")

if input [0] == consonants: 
    print (input[1] + input[0] + "ay")
