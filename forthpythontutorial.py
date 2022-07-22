#pdf to text to natural language processing to structured tabular format to csv
import pdfminer #pdf to text
import spacy #nlp in the industry there are a lot of features for spacy nlp, language supporters, a lot of natural language processing
import re #regex
import os #os file path
import pandas as pd #output csv


nlp = spacy.laod("en_core_web_sm")
text = "Best Python Course"
re.match("Best", text)
re.match("Best|Good", text)
text2 = "Good Python Course"
re.match("Best| Good", text2)
re.search("Best|Good", text2)
re.findall("AAAAA", text2)

