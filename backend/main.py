from flask import Flask, json, request
from flask_cors import CORS
from dictionary import dictionary, personal_dictionary, ehr_dictionary
from numpy import extract, array
from transformers import pipeline
import re
#create a classifier based on BART model 
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

#define label dictionary
candidate_labels = ["allergies", "allergic","eat", "food", "information", "personal information", "help", "pollen", "level", "prescriptions", "medication", "renew", 
                    "contraindications", "drugs", "vaccine", "cerification", "reservation", "appointment", "cancel", "date", "doctor", "number", "address", "email"
                    "visiting hours", "ehr", "system","electronic health record", "data", "protection", "digital skills", "do", "chatbot", "work",
                    ]


#web server
api = Flask(__name__)
CORS(api)

#endpoint api
@api.route('/api', methods=['POST'])
def post_message():
  data = request.get_json()
  final_response = "test"
  relevant_topics = []
  print(data["message"])
  topics = classifier(data["message"], candidate_labels, multi_class=True)
  print("topics: ", topics)
  choosenDictionary = {}
  value = 0.7
  #check if personal information
  # personal_info= topics["labels"].index("personal information")
  # print("personal info score: ", topics["scores"][personal_info])
  if re.search("ehr", data["message"], re.IGNORECASE) or re.search("electronic health record", data["message"], re.IGNORECASE): 
     print("EHR")
     choosenDictionary = ehr_dictionary
     value = 0.55 
     relevant_topics = parse_resuts(topics, value)
  else: 
      relevant_topics = parse_resuts(topics, value)
      if "personal information" in relevant_topics: 
         choosenDictionary = personal_dictionary
         print("using personal information dictionary")
      else:
         choosenDictionary = dictionary
         print("using normal dictionary")

  numberOfTopics = 0 
  keyList = list(choosenDictionary.keys())
  print(keyList)
  for key in choosenDictionary: 
     commonTopics = 0
     for topic in relevant_topics: 
        if topic in key: 
           print("MATCH FOUND", topic, key)
           commonTopics=commonTopics+1
     print(key, "has ", commonTopics, " topics in common with", relevant_topics)
     if commonTopics > numberOfTopics:
        final_response = choosenDictionary[key]
        numberOfTopics=commonTopics
     
  print("choosen: ", final_response)

  return json.dumps({"message": final_response}), 200

#for each topic decide which are valid and which are not
def parse_resuts(topics, value):
  res = []
  nparr_scores = array(topics["scores"])
  parsedarray = extract(nparr_scores>value, nparr_scores)

  for elem in parsedarray:
    index = topics["scores"].index(elem)
    res.append(topics["labels"][index])
  return res 

#main
if __name__ == '__main__':
    api.run()