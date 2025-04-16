## SCRIPT PARA ANALISE DE ARQUIVOS JAVASCRIPT.

import re
import os
import requests

# Cria a pasta dos relatórios se não existir
output_dir = '/opt/pentest/jsanalitic/relatorios-js'
os.makedirs(output_dir, exist_ok=True)

# Expressões de busca
regex_patterns = {
    'API Keys': r'(?i)(api[_-]?key|apikey|bearer|token)[\'"\s:=]+([A-Za-z0-9_\-]{10,})',
    'Endpoints': r'https?://[^\s\'"]+',
    'Emails': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'Possíveis Credenciais': r'(user(name)?|pass(word)?|senha|login)[\'"\s:=]+[^\s\'"]+',
    'Comentários': r'//.*|/\*[\s\S]*?\*/',
    'Chaves JWT': r'eyJ[A-Za-z0-9\-_]+?\.[A-Za-z0-9\-_]+?\.[A-Za-z0-9\-_]+',
    'Paths Suspeitos': r'(/[a-zA-Z0-9_\-./]{3,})'
}

def analisar_js(url):
    resultados = {categoria: set() for categoria in regex_patterns}

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f'Erro ao acessar {url}')
            return None
        content = response.text

        for categoria, pattern in regex_patterns.items():
            matches = re.findall(pattern, content)
            if matches:
                if isinstance(matches[0], tuple):
                    for m in matches:
                        resultados[categoria].add(m[1] if len(m) > 1 else m[0])
                else:
                    resultados[categoria].update(matches)

        return resultados

    except Exception as e:
        print(f'Erro ao processar {url}: {e}')
        return None


# Lendo a lista de JS
with open('/opt/pentest/jsanalitic/jsativos.txt', 'r') as f:
    urls = [linha.strip() for linha in f if linha.strip()]

for url in urls:
    print(f'Analisando: {url}')
    resultados = analisar_js(url)
    if resultados:
        nome_arquivo = url.split('/')[-1].split('?')[0] or 'arquivo'
        output_path = os.path.join(output_dir, f'{nome_arquivo}_report.txt')

        with open(output_path, 'w') as f_out:
            f_out.write(f'URL Analisada: {url}\n\n')
            for categoria, dados in resultados.items():
                f_out.write(f'[{categoria}]\n')
                if dados:
                    for item in dados:
                        f_out.write(f'{item}\n')
                else:
                    f_out.write('Nada encontrado\n')
                f_out.write('\n')

print('\nAnálise finalizada. Relatórios salvos em:')
print(output_dir)

