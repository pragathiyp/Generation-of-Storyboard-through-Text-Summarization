from lsa_summarizer import LsaSummarizer
from nltk.corpus import stopwords

source_file = "new.txt"

with open(source_file, "r", encoding='utf-8') as file:
    text = file.readlines()

print(type(text))

summarizer = LsaSummarizer()

stopwords = stopwords.words('english')
summarizer.stop_words = stopwords

summary = []

for line in text:
    summary.append(" ".join(summarizer(line, 1)))

print("====== Original text =====")
print(text)
print("====== End of original text =====")

print("\n========= Summary =========")
print("\n".join(summary))
print("========= End of summary =========")
