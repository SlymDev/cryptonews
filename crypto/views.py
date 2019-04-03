from django.shortcuts import render

def home(request):
	import requests
	import json

	#Prices (top 5)
	prices_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
	prices = json.loads(prices_request.content)

	#News
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news = json.loads(news_request.content)

	return render(request, "home.html", {'news': news, 'prices': prices})

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote'].upper()
		result_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
		result = json.loads(result_request.content)
		return render(request, "prices.html", {'quote': quote, 'result': result})
	else:
		notfound = "Please enter a currency abreviation into the form."
		return render(request, "prices.html", {'notfound': notfound})