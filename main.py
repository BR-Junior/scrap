import json
import csv

emails = []

with open('data/result.json') as json_file:
  data = json.load(json_file)

  with open('emails.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email', 'Vaga'])
    for post in data['messages']:
      for text in post['text']:
        # get type igual email
        if type(text) != str:
          if text.get('type') == 'email':
            if text['text'] not in emails:
                emails.append(text['text'])          
                writer.writerow([text['text'], post])