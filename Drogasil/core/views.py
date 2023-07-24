from django.shortcuts import render, redirect
import requests, json, os
from asgiref.sync import sync_to_async
from django.views.decorators.http import require_GET
from .forms import PesquisaForm
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        form = PesquisaForm(request.POST, request.FILES)
        if form.is_valid():
            search = form.cleaned_data['search']
            products = drogasil(request, search)
            products_list = products[0]
            products_pagueMenos = products[1]
            return render(request, 'drogasil.html', {'products_list': products_list, 'products_pagueMenos': products_pagueMenos})
        else:
            return (redirect('index'))
    else:
        return (redirect('index'))

@require_GET
async def drogasil(request, search):
    search_url = f'https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGASIL/channel/SITE/product/search/live?term={search}&tokenCart=JORH5eyXMF9F7mqV2SDV1K9ZiHJeWrGY&limit=100&sort_by=price:asc&origin=searchSuggestion'
    file_name = f"paguemenos_products_{datetime.now().date()}.json"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    response = requests.get(url=search_url)
    response_data = json.loads(response.content)
    products_list = response_data.get('results').get('products')
    pagueMenos = []

    async def run_commands_async():
        try:
            file_path = os.path.join(current_directory, "Crawler_PagueMenos", "crawler", "raw", file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                response_data_pm = json.load(file)
                for item in response_data_pm:
                    if str(search).upper() in str(item['name']).upper():
                        image_url_list = item['imageUrl']
                        if isinstance(image_url_list, list) and image_url_list:  
                            image_url = image_url_list[0]  
                            image_filename = image_url.split('/ids/')[-1] 
                            modified_image_url = f"//paguemenos.vtexassets.com/arquivos/ids/{image_filename}"
                            item['imageUrl'] = modified_image_url  
                            pagueMenos.append(item)
        except IOError:
            pass
        finally:
            return (products_list, pagueMenos)
    # Execute the function asynchronously
    (products_list, pagueMenos) = await sync_to_async(run_commands_async)()
    return (products_list, pagueMenos)
