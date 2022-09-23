piglatin = input("What word would you like to translate?")
# read the word, identify first letter, move first letter to last place + ay

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l" ,"m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if piglatin[0] in vowels: 
    print (piglatin + "yay")

if piglatin[0] in consonants: 
    print (piglatin[1:] + piglatin[0] + "ay")
