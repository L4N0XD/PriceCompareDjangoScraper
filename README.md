### PriceCompare - Drogasil/PagueMenos

Esse projeto tem como finalidade obter os preços dos produtos pesquisados e comparar os valores entre eles nos sites da Drogasil (Utilizando a API) e da PagueMenos, utilizando uma técnica de raspagem de dados utilizando o módulo **Scrapy** do Python.

Para a melhor visualização dos dados de Saída e melhor fluidez e facilidade de acesso, foi utilizado o framework Django. 

### Como utilizar:

1- Dois cliques em "Requirements.bat" para instalar os módulos necessários.
2- Abrir o CMD
3- digitar o seguinte comando: cd "caminho para a pasta Drogasil"
4- digitar o seguinte comando: python scrapy.py (O script fará uma raspagem todos os dias às 7h da manhã, caso não seja executado, será retornado à página apenas os dados constantes da Drogasil)
5- digitar o seguinte comando: python manage.py runserver
6- Abrir o link do servidor e ser feliz.
