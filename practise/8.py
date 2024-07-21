import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')


def get_antonums_sys(word):
    sysnonyms,antonyms=set(),set()
    for sys in wordnet.synsets(word):
        for lemma in sys.lemmas():
            sysnonyms.add(lemma.name())
            for ant in lemma.antonyms():
                antonyms.add(ant.name())
    return sysnonyms,antonyms
    
word=input("enter the word :")

synonymns,antonyms=get_antonums_sys(word)

print(synonymns)
print(antonyms)