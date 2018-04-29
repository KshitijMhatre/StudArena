import nltk

aplines = 'lines is some string of words'

# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
is_verb = lambda pos: pos[:2] == 'VB'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)] 

print(nouns)
print(verbs)