1. Configurar o ambiente
Instalar Python
Certifique-se de que o Python esteja instalado. Para verificar, execute:
# python --version
Se não estiver instalado, baixe o Python em python.org.

Instalar VSCode e a extensão Python
a-Abra o VSCode.
b-Vá para a aba de Extensões (ícone de quadrado no lado esquerdo).
c-Pesquise por Python e instale a extensão oficial.


Criar um ambiente virtual
No terminal do VSCode, execute:
# python -m venv venv

Ative o ambiente virtual:
# venv\Scripts\activate

2. Instalar bibliotecas necessárias
No terminal, instale as dependências:
# pip install selenium webdriver-manager

3. Criar o script
Crie um arquivo chamado main.py no diretório do projeto.
Adicione o seguinte código:

4. Executar o script
No terminal do VSCode, execute:
# python main.py
O script abrirá o navegador Chrome, navegará para o site, preencherá o nome e enviará o formulário.

5. Ajustar os seletores
Nome do campo: Inspecione o elemento de entrada de texto (campo "nome") no navegador (clique com o botão direito -> "Inspecionar").

ID do botão: Faça o mesmo para o botão de envio. Altere find_element(By.ID, "id_do_botao") no script para o valor correto.


6. Dicas adicionais
Use time.sleep() para dar tempo suficiente para os elementos carregarem. Para maior eficiência, use WebDriverWait:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Exemplo de espera para o elemento
nome_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "nome"))
)
Alternativa para seletores: Pode usar By.CLASS_NAME ou By.XPATH, dependendo da estrutura do HTML.

