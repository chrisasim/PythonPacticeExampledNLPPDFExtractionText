import spacy
nlp = spacy.load("en_core_web_sm")
text = ("Google was initially funded by an August 1998 contribution of 100000 dollars from Andy")
print(text)
doc = nlp(text)
for token in doc:
 print(token)
for token in doc:
 if token.pos == "NOUN":
  print(token)
for entity in doc.ents:
 print(entity.text, entity.label_)

