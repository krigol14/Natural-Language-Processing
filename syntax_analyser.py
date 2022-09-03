import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# create a grammar containing only the words needed to analyse the story in the 'story.txt'/ 'story2.txt' files
grammar = nltk.CFG.fromstring("""
S -> NP VP 
NP -> PN | DET N | N 
VP -> IV | IV ADV | AV ADJ | TV PN NP | V NP 
DET -> 'the'
ADJ -> 'scared' | 'bad' | 'sad'
N -> 'cat' | 'dog' | 'food' | 'money' | 'thief' | 'owner' | 'police' | 'shop'
AV -> 'is'
IV ->
TV ->
V -> 'chased' | 'hates' | 'needs' | 'has' | 'gives' | 'calls' | 'enters' | 'arrests'
PN ->
ADV ->
""") 

# create a string variable containing the story in the 'story.txt' file, after we open it
with open("story2.txt", "r") as story_file:
    story = story_file.read().replace('\n', '')

# tokenize the sentences in the story
tokens = sent_tokenize(story)
stopwords=['.','\'']

# further tokenize the sentences into words
for token in tokens: 
    word_tokens = nltk.word_tokenize(token) 
    for word in list(word_tokens): 
        if word in stopwords: 
            word_tokens.remove(word) 
    
    print(word_tokens) 
    parser = nltk.ChartParser(grammar) 
    for tree in parser.parse(word_tokens): 
        print(tree) 
        print("\n")
        tree.draw()
