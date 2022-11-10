 #this program is used to translate english to french and french to english.

from fnmatch import translate


English_to_French={
  "water": "eau",
  "pen": "stylo",
  "battle": "Comba",
  "botle": "bouteille",
  "butter": "beurre",
  "house": "maison",
  "computer": "ordinateur",
  "plum": "prune"
}
 
French_to_English ={
  "eau" : "water",
  "stylo" : "pen",
  "combat" : "battle",
  "bouteille" : "botle",
  "beurre" : "butter",
  "maison" : "house",
  "ordinateur" : "computer",
  "brune" : "Plum"
 }
Language = str(input("Enter the translate either french or english: \n"))
Word = str(input("Enter the word you need the translation  the into chosen language: \n"))
print (Word)
if Language == "french":
  if Word in English_to_French:
    translate = English_to_French[Word]
    print(f"the translation of {Word} in french is {translate}")
  else: 
    print(f"{Word} is not in my memory")
elif Language == "english":
  if Word in French_to_English:
    translate = French_to_English[Word]
    print(f"the translation of {Word} in english is {translate}")
  else:
    print(f"{Word} is not in my memory")
else:
  print("please enter french or english")



