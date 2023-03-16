import json

 #EHR patient data mockup
patient = {
    "name": "Asia",
    "allergies": " ".join(['Nuts']),
    "doctor_identifier": "BOH",
    "doctor_surname": "Angela",
    "reservations": " ".join(['Monday, 13, 11:00h']),
    "medications": " ".join(['Tachipirina', 'Oki']),
    "doctor": {
        "name": "Giovanni",
        "surname": "Rossi",
        "phone_number": "3345781609",
        "email": "giovannirossi@gmail.com"
    }
}

#this dictionary contains personal information
personal_dictionary = {
    ("personal information", "allergies", "food"): patient["name"] + ", you're allergic to " + patient["allergies"]  + ", be sure not to eat any of those foods.",
    ("personal information", "doctor", ): "Your doctor information and contacts are: \n"  + json.dumps(patient["doctor"], indent = 4),
    ("personal information", "prescriptions", "medications"): patient["name"]+ ", your prescriptions are: "+  patient["medications"],
    ("personal information","renew", "prescription" ): "You can text or call your doctor and ask to have the renewal. If you want, I can help you finding contacts of your doctor.",
    ("reservation", "cancel", "book", "appointment", "doctor", "information") : "Your reservation are " + patient["reservations"] + ". For any issue or information regarding your reservations you can text or email you doctor at " + patient["doctor"]["email"],
    ("personal information", "protection", "data"): "Yes, your data can only be accessed by healthcare professionals and are protected in the better way possible.",
    ("personal information", "digital skills"): "Digital skills are a set of knowledge and competencies of an individual in knowing how to use ICT technologies in different context and situations.",
    ("information", "chatbot"): "You can ask me information about your doctor, your reservations, your medications and many others. Also, I can explain to you the functioning of the EHR, to increase your knowledge and help you understand all the system!",
    ("chatbot", "work"): "Basically, I understand what you ask to me and I try to give you answers in the better way possible. ",
    ("personal information", "doctor", "number"): patient["name"] + ", your doctor phone number is " + patient["doctor"]["phone_number"],
}

#this dictionary contains general information
dictionary = {
    ("information", "allergies", "help") : "I can suggest you to look at this website: https://www.epicentro.iss.it/allergie/. It contains certificated information from the Istituto Superiore di Sanità about allergies in general and it may be useful to you.",
    ("information", "pollen") : "I suggest you to give a look at this website: https://www.fmach.it/Servizi-Generali/Informazioni-pollini/Bollettino-Pollini. It is made by Edmund Mach Foundation, it measures the level of pollen in the air for the territory of Trentino. Hope it is helpful! ", 
    ('allergies', 'allergic', 'contraindications', 'food'): patient["name"] + ", you're allergic to " + patient["allergies"]  + ", be sure not to eat any of those foods. If you want to know more about allergies, I can help you do some search.",
    ("contraindications", "drugs", "medications", "information") : "Ok, for any information about medications composition I can suggest you to read the medication leaflet. In case you are missing it, you can search your medication in this website: https://farmaci.agenziafarmaco.gov.it/bancadatifarmaci/cerca-farmaco. If the medication is giving you any kind of problems, I suggest you to reach out your doctor, who can give you more precise information and, in case, change the prescription.",
    ("eat","contraindications") : 'If you want to know anything about your allergies just ask me "tell me about my allergies" ',
    ("reservation", "cancel", "book", "appointment", "doctor", "information") : "To modify you reservations, go to the dedicated section. There you can find all the informations about the procedure to manage them.",
    ("prescriptions", "medications", "information"): patient["name"]+ ", your prescriptions are: "+  patient["medications"],
    ("vaccine", "information") : "To know more about vaccines, you should visit this website: https://www.salute.gov.it/portale/vaccinazioni/menuContenutoVaccinazioni.jsp?lingua=italiano&area=vaccinazioni&menu=fasce",
    ("information", "protection", "data"): "Yes, your data can only be accessed by healthcare professionals and are protected in the better way possible.",
    ("information", "digital skills"): "Digital skills are a set of knowledge and competencies of an individual in knowing how to use ICT technologies in different context and situations.",
    ("help", "chatbot"): "You can ask me information about your doctor, your reservations, your medications and many others. Also, I can explain to you the functioning of the EHR, to increase your knowledge and help you understand all the system!",
    ("improve", "digital skills"): "There are a lot of initiatives to which you can take part to enhance your digital skills.",
}

#this dictionary contains EHR information
ehr_dictionary = {
    ( "ehr", "information", "electronic health record") : "The Electronic Health Record (FSE) is the set of digital information and documents that concern your health, such as medical reports and prescriptions. These data and documents are produced on the occasion of present or past clinical events, such as a specialist visit, a laboratory test or upon discharge from the hospital. You can imagine your Electronic Health File (FSE) as a folder that contains your health records.",
    ( "ehr","electronic health record", "do",  "system") : "You can: consult your reports and pharmaceutical prescriptions; \nbook visits (with or without a prescription) and other specialist services, such as blood tests; access television visits; keep a diary about your health; pay for health services online; change or revoke your general practitioner or pediatrician of choice; consult waiting times in the emergency room, look for pharmacies, parapharmacies and doctor's surgeries."
}