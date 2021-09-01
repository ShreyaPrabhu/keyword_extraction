from rake_nltk import Rake

r = Rake()

text = "I want to learn advanced machine learning courses"
r.extract_keywords_from_text(text)
keyword_extracted = r.get_ranked_phrases()
print(keyword_extracted)
