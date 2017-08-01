from django.shortcuts import render
import krakenex

k = krakenex.API()
k.load_key('kraken.key')

# Create your views here.
def splash(request):
    def price_scrape(base, quote):
        url = 'https://api.cryptonator.com/api/ticker/' + base +'-' + quote
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        price = data['ticker']['price']
        volume = data['ticker']['volume']
        Price.objects.create(entry = random.randint(1,10), xbt = random.randint(1,10), eth =random.randint(1,10))
        return price, volume
    balance = k.query_private('Balance')['result'] #This will need to be some sort of dictionary in order to be passed
    balance_dic = {'result': balance}
    return render(request, 'home/splash.html', balance_dic)