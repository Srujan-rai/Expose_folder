import nltk
from nltk import CFG
from nltk.parse.chart import BottomUpChartParser, TopDownChartParser

# Defining the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "Rahil" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my" | "his"
    N -> "dog" | "cat" | "telescope" | "park" | "Moon" | "terrace"
    P -> "in" | "on" | "by" | "with" | "from"
""")

# Defining a proper sentence
sentence = "Rahil saw the Moon with the telescope from his terrace".split()

# Parsing function
def parse_and_print(parser, name):
    print(f"{name} Parsing:")
    for tree in parser.parse(sentence):
        print(tree)
        tree.pretty_print()
        tree.draw()

# Bottom-Up Parsing
parse_and_print(BottomUpChartParser(grammar), "Bottom-Up")

# Top-Down Parsing
parse_and_print(TopDownChartParser(grammar), "Top-Down")
