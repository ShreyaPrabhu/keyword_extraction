import scispacy
import spacy

keywordExtractor = spacy.load("en_core_sci_sm")
text = "Programming is what i want to learn"
keywords = keywordExtractor(text)
print(keywords.ents)
