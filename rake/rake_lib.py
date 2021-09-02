import RAKE
import operator

stop_dir = "stoplist.txt"
rake_object = RAKE.Rake(stop_dir)
text = "I want to learn advanced machine learning courses"

keywords = rake_object.run(text)
print ("keywords: ", keywords)
