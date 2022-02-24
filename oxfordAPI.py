import requests
from pprint import pprint as print


app_id = '87ed8575'
app_key = '02c42543e11e4756ae17dfa599cb1b30'
language = 'en-gb'

word_id = 'have'
url = f'https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}'

response = requests.get(url, headers={'app_id': app_id, 'app_key':app_key})

#_____Checking the response____
# print(response.status_code)

jsondata = response.json()

# print(jsondata['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get['audioFile'])
# print('           ')
# print(jsondata['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print(jsondata['results'][1]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print(jsondata['results'][2]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print('            ')
#number = len(jsondata['results'][0]['lexicalEntries'][0]['entries'])
#x = []

#for i in range(0, number):
    #print(jsondata['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions'][0])


print(jsondata['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text'])
























