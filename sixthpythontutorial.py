import spacy
import pdfminer
import re
import os
import pandas as pd

import pdf2text
def convert_pdf(f):
 output_filename = os.path.basename(os.path.splitext(f)[0]) + ".xtx"
 output_filepath = os.path.join("output/txt/", output_filename)
 pdf2text.main(args = (f, "--outfile", output_filepath))
 print(output_filepath + " saved successfully!!!")
 return open(output_filepath).read()


#os.path.splitext("AbdulMajed.pdf")[0]
nlp = spacy.load("en_core_web_sm")
result_dist = {"name": [], "phone": [], "emails": [], "skills": []}
names = []
phones = []
emails = []
skills = []

def parse_content(text):
 skillset = re.compile("python| java| sql|hadoop | tableau")
 phone_num = re.compile()
 doc = nlp(text)
 name = [entity.text for entity in doc.ents if entity.label_ is "PERSON"][0]
 print(name)
 email = [word for word is doc if word.like_email == True][0]
 print(email)
 phone = str(re.findall(phone_num, text.lowe()))
 skills_list = re.findall(skillset, text.lower())
 unique_skills_list = str(set(skills_list))
 names.append(name)
 emails.append(email)
 phones.append(phone)
 skills.append(unique_skills_list)
 print("Extraction completed!")

for file in os.listdir('resumes/'):
 if file.endswith('.pdf'):
  print("Reading..." + file)
  txt = convert_pdf(os.path.join('resumes/',file))
  parse_content(txt)
