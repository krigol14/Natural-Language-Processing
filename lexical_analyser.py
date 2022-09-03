from nltk.tokenize import sent_tokenize, word_tokenize

# create a string variable containing the story in the 'story.txt' file, after we open it
with open("story.txt", "r") as story_file:
    story = story_file.read().replace('\n', '')

# operate at sentence level using the sentence tokenizer directly
print("SENTENCE TOKENIZER: ")
tokens = sent_tokenize(story)
for token in tokens:
    print("Sentence " + str(tokens.index(token) + 1) + ": " + str(token))

# operate at word level using the word tokenizer 
print("\nWORD TOKENIZER: ")
word_tokens = [word_tokenize(t) for t in tokens]
for word_token in word_tokens:
    print("Words in sentence " + str(word_tokens.index(word_token) + 1) + ": " + str(word_token))
