import nltk
from nltk import CFG
from nltk.parse.chart import BottomUpChartParser,TopDownChartParser


grammer=CFG.fromstring("""
                           S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "Rahil" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my" | "his"
    N -> "dog" | "cat" | "telescope" | "park" | "Moon" | "terrace"
    P -> "in" | "on" | "by" | "with" | "from"
                       """)


sentence="Rahil saw the Moon with the telescope from his terrace".split()

def parser(parser,name):
    print(f"{name} parsing")
    for tree in parser.parse(sentence):
        print(tree)
        tree.pretty_print()
        tree.draw()
        
        
parser(BottomUpChartParser(grammer),"bottom-up")
parser(TopDownChartParser(grammer),"bottom-up")