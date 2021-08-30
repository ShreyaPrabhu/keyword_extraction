import yake

kw_extractor = yake.KeywordExtractor()
text = "i want to learn quantum physics"
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 3
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)
for kw in keywords:
    print(kw)
