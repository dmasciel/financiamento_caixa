```markdown
# Automação Web com Selenium

Este projeto demonstra um exemplo simples de automação web usando Selenium em Python.

## 1. Configuração do Ambiente

### Instalar Python

Certifique-se de que o Python esteja instalado. Para verificar, execute:

```bash
python --version
```

Se não estiver instalado, baixe o Python em [python.org](https://www.python.org/).

### Instalar VSCode e a extensão Python

1. Abra o VSCode.
2. Vá para a aba de Extensões (ícone de quadrado no lado esquerdo).
3. Pesquise por "Python" e instale a extensão oficial da Microsoft.

### Criar um Ambiente Virtual

No terminal do VSCode, execute:

```bash
python -m venv venv
```

Ative o ambiente virtual:

* **Windows:**
```bash
venv\Scripts\activate
```
* **macOS/Linux:**
```bash
source venv/bin/activate
```

## 2. Instalar Bibliotecas Necessárias

No terminal, instale as dependências:

```bash
pip install selenium webdriver-manager
```

## 3. Criar o Script

Crie um arquivo chamado `main.py` no diretório do projeto.
Adicione o seu código Python para automação web com Selenium neste arquivo.  Um exemplo básico seria:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("URL_DO_SITE")

# Encontre os elementos e interaja com eles (Exemplo)
nome_input = driver.find_element(By.NAME, "nome")
nome_input.send_keys("Seu Nome")

botao_submit = driver.find_element(By.ID, "id_do_botao")
botao_submit.click()

# ... restante do seu código ...

driver.quit()
```

## 4. Executar o Script

No terminal do VSCode, execute:

```bash
python main.py
```

O script abrirá o navegador Chrome, navegará para o site especificado no código e executará as ações definidas.

## 5. Ajustar os Seletores

* **Nome do campo:** Inspecione o elemento de entrada de texto (campo "nome") no navegador (clique com o botão direito -> "Inspecionar"). Utilize o atributo `name`  no seu código.
* **ID do botão:** Faça o mesmo para o botão de envio.  Utilize o atributo `id` no seu código.  Altere `find_element(By.ID, "id_do_botao")` no script para o ID correto.

## 6. Dicas Adicionais

* **Tempo de espera:** Use `time.sleep()` para dar tempo suficiente para os elementos carregarem. Para maior eficiência, use `WebDriverWait`:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Exemplo de espera para o elemento
nome_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "nome"))
)
```

* **Alternativa para seletores:** Pode usar `By.CLASS_NAME`, `By.XPATH`, `By.CSS_SELECTOR`, etc., dependendo da estrutura do HTML.  `By.ID` e `By.NAME` são geralmente preferíveis quando disponíveis.
```
