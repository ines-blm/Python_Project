
def copy(file):
  with open('story.txt', 'r') as firstfile, open('story_copy.txt', 'a') as secondfile:  
    for line in firstfile: 
        secondfile.write (line) 

copy('file')
