import os, subprocess
from datetime import datetime, timedelta, date
import time


def raspar():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    crawler_directory = os.path.join(current_directory,'core', 'Crawler_PagueMenos')
    # Executar o comando "scrapy crawl paguemenos_crawl" no diretório correto
    resultado = subprocess.run(
        "scrapy crawl paguemenos_crawl",
        shell=True,
        cwd=crawler_directory,
        capture_output=True,
        text=True
    )
    # Verificando se houve algum erro
    if resultado.returncode == 0:
        # Saída do comando bem-sucedido
        print("Saída do comando:")
        print(resultado.stdout)
    else:
        # Ocorreu um erro na execução do comando
        print("Erro ao executar o comando:")
        print(resultado.stderr)

while True:
    hora_atual = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
    hora_definida = datetime.strptime("07:00:00", "%H:%M:%S")
    tempo_restante = hora_definida - hora_atual
    if tempo_restante.total_seconds() < 0:
        tempo_restante += timedelta(days=1)
    print("Próxima verificação de Solicitações encerradas em:", tempo_restante, end="\r")
    time.sleep(1)
    if hora_atual.time() == hora_definida.time():
        raspar()