Análise de JavaScript

Este repositório contém um script em Python para análises rápidas de arquivos JavaScript (.js), útil em atividades de segurança e reconhecimento.
📁 Preparação do ambiente

    Clone o repositório:

git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio

Crie uma pasta para armazenar os resultados: O script salvará os resultados em uma pasta local. Crie-a com:

    mkdir resultados

    Configure o script:

        Edite a variável output_dir no script janalitic.py, definindo o caminho da pasta onde os resultados serão salvos.

        Na seção Lendo a lista de JS, indique o caminho do arquivo que contém a lista de URLs dos arquivos .js.

🚀 Execução
Para executar o script, use:

python3 janalitic.py

O script fará a análise automática dos arquivos listados.
🛠️ Gerando a lista de arquivos JS

Você pode utilizar ferramentas como waybackurls para encontrar arquivos .js públicos de um domínio.
🔹 Comando básico:
echo "alvo.com.br" | waybackurls | grep '.js' | anew jslista.txt

🔹 Com filtro mais refinado:
echo "alvo.com.br" | waybackurls | grep -E "\.js(?:onp?)?$" | anew jslista.txt

🔹 Validar URLs que retornam status 200:
xargs -a dominios.txt -I@ sh -c 'echo "@" | waybackurls | grep -E "\.js(?:onp?)?$"' | anew js.txt

📌 Observação

Certifique-se de que todas as ferramentas necessárias (como waybackurls, anew, xargs, etc.) estejam instaladas no seu ambiente.
