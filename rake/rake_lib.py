import RAKE
import operator

# Reka setup with stopword directory
stop_dir = "stoplist.txt"
rake_object = RAKE.Rake(stop_dir)
text = "I am interested in Quantum Physics"

keywords = rake_object.run(text)
print ("keywords: ", keywords)
