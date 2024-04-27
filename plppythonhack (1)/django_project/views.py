import requests
from django.http import response
from django.shortcuts import render

def home(request):
  
  response = requests.get('https://gutendex.com/books?languages=fr,en')
  data = response.json()
  results = data["count"]

  

  response2 = requests.get('https://gutendex.com/books?searchquery=harry')
  data2 = response2.json()
  results2 = data2["count"]

  response3 = requests.get('https://gutendex.com/books?topic=Horror Tales')
  data3 = response3.json()
  results3 = data3["results"]
  
  
  return render(request, 'templates/index.html', {'results': results, 'results2': results2, 'results3': results3})
  