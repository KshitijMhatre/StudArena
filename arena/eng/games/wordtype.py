import nltk
import nltk.data
import random

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("eng/games/textData/test.txt")
data = fp.read()

dataset = [line for line in tokenizer.tokenize(data)]


def challenge():
    lines = random.choice(dataset)
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    is_verb = lambda pos: pos[:2] == 'VB'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(lines)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)] 

    
    return {
        'question':lines,
        'nouns':nouns,
        'verbs':verbs
    }

if __name__=='__main__':
    print(challenge())