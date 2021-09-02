import scispacy
import spacy

keywordExtractor = spacy.load("en_core_web_sm")
text = "I want to learn quantum physics"
keywords = keywordExtractor(text)
print(keywords.ents)
